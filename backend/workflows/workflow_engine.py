from langgraph.graph import StateGraph
from typing import TypedDict, List

from backend.agents.architect_agent import architect_plan
from backend.agents.executor_agent import execute_step
from backend.agents.auditor_agent import audit_step
from backend.agents.sentinel_agent import handle_failure
from backend.agents.historian_agent import store_memory


class WorkflowState(TypedDict):
    goal: str
    steps: list
    current_step: str
    result: list
    logs: list
    simulate_failure: bool
    confidence: float
    workflow_type: str


def architect_node(state: WorkflowState):

    goal = state["goal"].lower()
    state["logs"].append(f"🧠 Architect: Understanding goal → {goal}")

    if any(x in goal for x in ["payment", "vendor", "invoice"]):
        steps = [
            "Validate invoice data",
            "Verify vendor credentials",
            "Check tax compliance",
            "Perform fraud detection",
            "Validate payment limits",
            "Cross-check vendor history",
            "Approve transaction",
            "Execute payment",
            "Generate receipt",
            "Send confirmation email",
            "Log financial record",
            "Update accounting system",
            "Archive transaction"
        ]

    elif any(x in goal for x in ["onboarding", "employee", "hr"]):
        steps = [
            "Collect employee details",
            "Verify documents",
            "Create employee account",
            "Assign system access",
            "Allocate equipment",
            "Setup payroll",
            "Enroll benefits",
            "Create email account",
            "Grant tool access",
            "Send onboarding email",
            "Schedule orientation",
            "Assign mentor",
            "Update HR system",
            "Archive onboarding record"
        ]

    elif any(x in goal for x in ["contract", "legal"]):
        steps = [
            "Extract contract terms",
            "Validate clauses",
            "Check legal compliance",
            "Identify risks",
            "Cross-check regulations",
            "Verify parties involved",
            "Flag inconsistencies",
            "Suggest modifications",
            "Approve contract",
            "Generate summary",
            "Store legal document",
            "Notify stakeholders",
            "Archive contract"
        ]

    else:
        steps = [
            "Analyze request",
            "Break into tasks",
            "Validate inputs",
            "Execute operations",
            "Monitor progress",
            "Check compliance",
            "Handle errors",
            "Retry failed steps",
            "Validate output",
            "Store results",
            "Notify stakeholders",
            "Generate report"
        ]

    state["steps"] = steps
    return state


def auditor_node(state: WorkflowState):

    if not state["steps"]:
        return state

    step = state["steps"].pop(0)
    state["logs"].append(f"🔍 Auditor: Validating {step}")

    audit = audit_step(step)

    if audit["status"] != "approved":
        state["logs"].append(f"❌ Auditor rejected {step}")
        raise Exception("Audit failed")

    state["current_step"] = step
    return state


import random

import random
import time

def executor_node(state: WorkflowState):

    step = state["current_step"]

    # Simulate execution time
    execution_time = round(random.uniform(0.5, 2.5), 2)

    confidence = round(random.uniform(0.75, 0.98), 2)
    risk = round(1 - confidence, 2)

    state["logs"].append(
        f"⚙️ Executor: {step} | Time: {execution_time}s | Confidence: {confidence} | Risk: {risk}"
    )

    # 🔥 SLA Monitoring
    if execution_time > 2.0:
        state["logs"].append("⏱ SLA Monitor: High latency detected ⚠️")

    if risk > 0.2:
        state["logs"].append("⚠ Risk Monitor: Potential bottleneck detected")

    # Failure simulation
    if state["simulate_failure"] and len(state["result"]) == 2:
        state["logs"].append(f"❌ Execution failed at {step}")
        raise Exception("Execution failed")

    state["result"].append({
        "step": step,
        "status": "completed",
        "confidence": confidence,
        "risk": risk,
        "time": execution_time
    })

    return state


def sentinel_node(state: WorkflowState):

    step = state["current_step"]

    state["logs"].append(f"🛡 Sentinel: Failure detected at {step}")

    recovery_strategy = [
        "Retry with backup API",
        "Switch to alternative workflow",
        "Use cached data fallback"
    ]

    strategy = random.choice(recovery_strategy)

    state["logs"].append(f"🛡 Sentinel: Applying strategy → {strategy}")
    state["logs"].append("🛡 Sentinel: Recovery successful")

    state["result"].append({
        "step": step,
        "status": "recovered",
        "confidence": 0.85,
        "risk": 0.15
    })

    return state


def historian_node(state: WorkflowState):
    state["logs"].append("📚 Historian: Storing workflow memory")
    store_memory(state["goal"], str(state["result"]))
    return state


# ✅ ADD HERE 👇 (STEP 2 FUNCTION)
def meeting_intelligence(goal: str):

    return [
        {"task": "Prepare project report", "owner": "Manager", "status": "pending"},
        {"task": "Review compliance", "owner": "Auditor", "status": "pending"},
        {"task": "Execute payment", "owner": "Finance Team", "status": "pending"},
        {"task": "Send confirmation email", "owner": "System", "status": "pending"}
    ]


# EXISTING FUNCTION
def run_workflow(goal: str, simulate_failure: bool = False):

    state = {
        "goal": goal,
        "steps": [],
        "current_step": "",
        "result": [],
        "logs": [],
        "simulate_failure": simulate_failure,
        "confidence": 0.9
    }

    # Run architect
    state = architect_node(state)

    # 🔥 LOOP THROUGH ALL STEPS
    while state["steps"]:

        try:
            state = auditor_node(state)
            state = executor_node(state)

        except Exception:
            state = sentinel_node(state)

    state = historian_node(state)

    tasks = meeting_intelligence(goal)

    return {
    "result": state["result"],
    "logs": state["logs"],
    "confidence": state["confidence"],
    "tasks": tasks
}