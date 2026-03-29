from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from backend.workflows.workflow_engine import run_workflow

app = FastAPI(title="SentinelFlow AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class WorkflowRequest(BaseModel):
    goal: str
    simulate_failure: bool = False


@app.get("/")
def home():
    return {"message": "SentinelFlow AI Running"}


@app.post("/workflow")
def start_workflow(req: WorkflowRequest):
    result = run_workflow(req.goal, req.simulate_failure)
    return {"result": result}