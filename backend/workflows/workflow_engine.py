from typing import TypedDict, List
import random
import time

from backend.agents.architect_agent import architect_plan
from backend.agents.executor_agent import execute_step
from backend.agents.auditor_agent import audit_step
from backend.agents.sentinel_agent import handle_failure
from backend.agents.historian_agent import store_memory


# =========================
# STATE STRUCTURE
# =========================
class WorkflowState(TypedDict):
    goal: str
    steps: List[str]
    current_step: str
    result: list
    logs: list
    simulate_failure: bool
    confidence: float


# =========================
# ARCHITECT
# =========================
def architect_node(state: WorkflowState):

    goal = state["goal"].lower()
    state["logs"].append(f"🧠 Architect: Planning workflow for → {goal}")

    if any(x in goal for x in ["payment", "vendor"]):
        steps = [
            "Validate invoice",
            "Verify vendor",
            "Check compliance",
            "Fraud detection",
            "Approve payment",
            "Execute transaction",
            "Generate receipt",
            "Send confirmation"
        ]
    elif "onboarding" in goal:
        steps = [
            "Collect employee data",
            "Verify documents",
            "Create account",
            "Assign access",
            "Setup payroll",
            "Send welcome email"
        ]
    else:
        steps = [
            "Analyze request",
            "Break into tasks",
            "Validate inputs",
            "Execute operations",
            "Store results"
        ]

    state["steps"] = steps
    return state


# =========================
# AUDITOR
# =========================
def auditor_node(state: WorkflowState):

    if not state["steps"]:
        return state

    step = state["steps"].pop(0)
    state["logs"].append(f"🔍 Auditor: Validating → {step}")

    audit = audit_step(step)

    if audit["status"] != "approved":
        state["logs"].append(f"❌ Auditor rejected: {step}")
        raise Exception("Audit failed")

    state["current_step"] = step
    return state


# =========================
# EXECUTOR
# =========================
def executor_node(state: WorkflowState):

    step = state["current_step"]

    execution_time = round(random.uniform(0.5, 2.5), 2)
    confidence = round(random.uniform(0.8, 0.98), 2)
    risk = round(1 - confidence, 2)

    state["logs"].append(
        f"⚙️ Executor: {step} | time={execution_time}s | confidence={confidence}"
    )

    # SLA Monitoring
    if execution_time > 2:
        state["logs"].append("⏱ SLA Warning: High latency")

    if risk > 0.2:
        state["logs"].append("⚠ Risk Alert: Potential issue detected")

    # 🔥 SIMULATE FAILURE (random step)
    if state["simulate_failure"] and random.randint(2, 4) == len(state["result"]):
        state["logs"].append(f"❌ Execution failed at {step}")
        raise Exception("Execution failure")

    state["result"].append({
        "step": step,
        "status": "completed",
        "confidence": confidence,
        "time": execution_time
    })

    return state


# =========================
# SENTINEL (RECOVERY)
# =========================
def sentinel_node(state: WorkflowState):

    step = state["current_step"]

    state["logs"].append(f"🛡 Sentinel: Failure detected at {step}")

    strategies = [
        "Retry with fallback",
        "Switch to backup process",
        "Use cached data"
    ]

    strategy = random.choice(strategies)

    state["logs"].append(f"🛡 Applying recovery → {strategy}")
    state["logs"].append("🛡 Recovery successful")

    state["result"].append({
        "step": step,
        "status": "recovered",
        "confidence": 0.85
    })

    return state


# =========================
# HISTORIAN
# =========================
def historian_node(state: WorkflowState):

    state["logs"].append("📚 Historian: Saving workflow history")
    store_memory(state["goal"], str(state["result"]))

    return state


# =========================
# TASK GENERATOR
# =========================
def generate_tasks(goal: str):

    return [
        {"task": "Review output", "owner": "Manager"},
        {"task": "Validate compliance", "owner": "Auditor"},
        {"task": "Execute final step", "owner": "Executor"},
        {"task": "Send report", "owner": "System"}
    ]


# =========================
# MAIN WORKFLOW
# =========================
def run_workflow(goal: str, simulate_failure=False):

    state: WorkflowState = {
        "goal": goal,
        "steps": [],
        "current_step": "",
        "result": [],
        "logs": [],
        "simulate_failure": simulate_failure,
        "confidence": round(random.uniform(0.85, 0.98), 2)
    }

    # Step 1: Plan
    state = architect_node(state)

    # Step 2: Execute loop
    while state["steps"]:
        try:
            state = auditor_node(state)
            state = executor_node(state)

        except Exception as e:
            state["logs"].append(f"❌ Error: {str(e)}")
            state = sentinel_node(state)

    # Step 3: Save history
    state = historian_node(state)

    # Step 4: Generate tasks
    tasks = generate_tasks(goal)

    return {
        "result": state["result"],
        "logs": state["logs"],
        "confidence": state["confidence"],
        "tasks": tasks
    }