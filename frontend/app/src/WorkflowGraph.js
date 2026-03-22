import React from "react";
import ReactFlow, { Background, Controls } from "reactflow";
import "reactflow/dist/style.css";

const WorkflowGraph = ({ agents }) => {

  const getColor = (status) => {
    if (status === "completed") return "#4CAF50";
    if (status === "running") return "#FFA500";
    return "#999";
  };

  const nodes = [
    {
      id: "1",
      data: { label: "Architect" },
      position: { x: 50, y: 50 },
      style: { background: getColor(agents[0]?.status), color: "white" }
    },
    {
      id: "2",
      data: { label: "Auditor" },
      position: { x: 250, y: 50 },
      style: { background: getColor(agents[1]?.status), color: "white" }
    },
    {
      id: "3",
      data: { label: "Executor" },
      position: { x: 450, y: 50 },
      style: { background: getColor(agents[2]?.status), color: "white" }
    },
    {
      id: "4",
      data: { label: "Sentinel" },
      position: { x: 300, y: 150 },
      style: { background: getColor(agents[3]?.status), color: "white" }
    },
    {
      id: "5",
      data: { label: "Historian" },
      position: { x: 300, y: 250 },
      style: { background: getColor(agents[4]?.status), color: "white" }
    }
  ];

  const edges = [
    { id: "e1-2", source: "1", target: "2" },
    { id: "e2-3", source: "2", target: "3" },
    { id: "e3-4", source: "3", target: "4" },
    { id: "e4-5", source: "4", target: "5" }
  ];

  return (
    <div style={{ height: 350, border: "1px solid #ddd", marginTop: "20px" }}>
      <ReactFlow nodes={nodes} edges={edges} fitView>
        <Background />
        <Controls />
      </ReactFlow>
    </div>
  );
};

export default WorkflowGraph;