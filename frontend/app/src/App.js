import React, { useState } from "react";
import WorkflowGraph from "./WorkflowGraph";

function App() {

  const [goal, setGoal] = useState("");
  const [result, setResult] = useState([]);
  const [loading, setLoading] = useState(false);

  const [logs, setLogs] = useState([]);
  const [confidence, setConfidence] = useState(null);
  const [simulateFailure, setSimulateFailure] = useState(false);
  const [tasks, setTasks] = useState([]);

  const initialAgents = [
    { name: "Architect", status: "idle" },
    { name: "Auditor", status: "idle" },
    { name: "Executor", status: "idle" },
    { name: "Sentinel", status: "idle" },
    { name: "Historian", status: "idle" }
  ];

  const [agents, setAgents] = useState(initialAgents);

  const updateAgent = (index, status) => {
    setAgents((prev) => {
      const updated = [...prev];
      updated[index].status = status;
      return updated;
    });
  };

  const resetAgents = () => setAgents(initialAgents);

  const runWorkflow = async () => {

    setLoading(true);
    resetAgents();
    setResult([]);
    setLogs([]);
    setConfidence(null);
    setTasks([]);

    try {
      updateAgent(0, "running");
      setTimeout(() => updateAgent(0, "completed"), 800);
      setTimeout(() => updateAgent(1, "running"), 800);
      setTimeout(() => updateAgent(1, "completed"), 1600);
      setTimeout(() => updateAgent(2, "running"), 1600);
      setTimeout(() => updateAgent(2, "completed"), 2400);
      setTimeout(() => updateAgent(3, "running"), 2400);
      setTimeout(() => updateAgent(3, "completed"), 3200);
      setTimeout(() => updateAgent(4, "running"), 3200);
      setTimeout(() => updateAgent(4, "completed"), 4000);

      const response = await fetch("http://127.0.0.1:8000/workflow", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          goal: goal,
          simulate_failure: simulateFailure
        })
      });

      const data = await response.json();

      setResult(data.result?.result || []);
      setLogs(data.result?.logs || []);
      setConfidence(data.result?.confidence || null);
      setTasks(data.result?.tasks || []);

    } catch (error) {
      console.error(error);
    }

    setLoading(false);
  };

  const glassCard = {
    background: "rgba(255,255,255,0.7)",
    backdropFilter: "blur(10px)",
    padding: "20px",
    borderRadius: "16px",
    boxShadow: "0 8px 24px rgba(0,0,0,0.08)",
    marginBottom: "20px"
  };

  return (
    <div style={{
      minHeight: "100vh",
      padding: "40px",
      fontFamily: "Inter, sans-serif",
      background: "linear-gradient(135deg, #eef2ff, #f0f9ff)"
    }}>

      {/* HEADER */}
      <div style={{
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
        marginBottom: "30px"
      }}>
        <h1 style={{
          fontSize: "32px",
          fontWeight: "800",
          background: "linear-gradient(to right, #4f46e5, #06b6d4)",
          WebkitBackgroundClip: "text",
          WebkitTextFillColor: "transparent"
        }}>
          🚀 SentinelFlow AI
        </h1>

        <span style={{
          fontSize: "14px",
          color: "#6b7280"
        }}>
          Enterprise AI Orchestrator
        </span>
      </div>

      {/* QUICK DEMO */}
      <div style={glassCard}>
        <h3>⚡ Quick Demo</h3>

        <div style={{ display: "flex", gap: "12px", flexWrap: "wrap" }}>
          {[
            "Vendor Payment",
            "Employee Onboarding",
            "Contract Review",
            "Loan Approval",
            "IT Access Setup"
          ].map((item, i) => (
            <button
              key={i}
              onClick={() => setGoal(item)}
              style={{
                padding: "10px 16px",
                borderRadius: "999px",
                border: "none",
                background: "#4f46e5",
                color: "#fff",
                cursor: "pointer",
                transition: "0.3s"
              }}
              onMouseOver={(e) => e.target.style.background = "#4338ca"}
              onMouseOut={(e) => e.target.style.background = "#4f46e5"}
            >
              {item}
            </button>
          ))}
        </div>
      </div>

      {/* INPUT */}
      <div style={glassCard}>
        <h3>Workflow Input</h3>

        <div style={{ display: "flex", gap: "10px", flexWrap: "wrap" }}>

        <div style={{ marginTop: "12px" }}>
  <label style={{
    display: "flex",
    alignItems: "center",
    gap: "8px",
    fontSize: "14px",
    cursor: "pointer",
    color: "#374151"
  }}>
    <input
      type="checkbox"
      checked={simulateFailure}
      onChange={() => setSimulateFailure(!simulateFailure)}
      style={{
        width: "16px",
        height: "16px",
        cursor: "pointer"
      }}
    />
    Simulate Failure
  </label>
</div>
          <input
            value={goal}
            onChange={(e) => setGoal(e.target.value)}
            placeholder="Describe your workflow..."
            style={{
              flex: 1,
              padding: "12px",
              borderRadius: "10px",
              border: "1px solid #ddd"
            }}
          />

          <button
            onClick={runWorkflow}
            style={{
              padding: "12px 20px",
              borderRadius: "10px",
              background: "linear-gradient(to right, #4f46e5, #06b6d4)",
              color: "#fff",
              border: "none",
              fontWeight: "600",
              cursor: "pointer"
            }}
          >
            🚀 Run
          </button>
          {loading && <p style={{ marginTop: "10px" }}>⏳ Running workflow...</p>}
        </div>

        {confidence && (
          <div style={{
            marginTop: "10px",
            padding: "10px",
            borderRadius: "8px",
            background: "#e0e7ff",
            color: "#3730a3"
          }}>
            🧠 Confidence: {Math.round(confidence * 100)}%
          </div>
        )}
      </div>

      {/* AGENTS */}
      <div style={glassCard}>
        <h3>🤖 Agent Status</h3>

        <div style={{
          display: "grid",
          gridTemplateColumns: "repeat(auto-fit, minmax(160px,1fr))",
          gap: "10px"
        }}>
          {agents.map((a, i) => (
            <div key={i} style={{
              padding: "12px",
              borderRadius: "12px",
              background: "#fff",
              display: "flex",
              justifyContent: "space-between",
              border: "1px solid #eee"
            }}>
              {a.name}
              <span style={{
                padding: "4px 8px",
                borderRadius: "999px",
                background: a.status === "completed" ? "#dcfce7" :
                           a.status === "running" ? "#fef3c7" : "#eee"
              }}>
                {a.status}
              </span>
            </div>
          ))}
        </div>
      </div>

      {/* GRAPH */}
      <div style={glassCard}>
        <h3>📊 Workflow Graph</h3>
        <WorkflowGraph agents={agents} />
      </div>

      {/* RESULTS */}
      <div style={glassCard}>
        <h3>Execution Result</h3>
        {result.map((r, i) => (
          <div key={i}>
            ✔ {r.step}
          </div>
        ))}
      </div>

      {/* TASKS */}
      <div style={glassCard}>
        <h3>📋 AI Generated Tasks</h3>
        {tasks.map((t, i) => (
          <div key={i}>
            • {t.task} ({t.owner})
          </div>
        ))}
      </div>

      {/* LOGS */}
      <div style={{
        background: "#0f172a",
        color: "#22c55e",
        padding: "15px",
        borderRadius: "12px",
        fontFamily: "monospace"
      }}>
        <h3>Execution Logs</h3>
        {logs.map((log, i) => <div key={i}>{log}</div>)}
      </div>

      {/* FOOTER */}
      <div style={{
        marginTop: "40px",
        display: "flex",
        justifyContent: "space-between"
      }}>
        <span>© Ravindra Suthar</span>

        <a
  href="https://github.com/Ravindra8829"
  target="_blank"
  rel="noopener noreferrer"
>
  GitHub
</a>

<a
  href="https://www.linkedin.com/in/ravindra-suthar/"
  target="_blank"
  rel="noopener noreferrer"
>
  LinkedIn
</a>
      </div>

    </div>
  );
}

export default App;