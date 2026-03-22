from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.workflows.workflow_engine import run_workflow

app = FastAPI(title="SentinelFlow AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "SentinelFlow AI Running"}

@app.post("/workflow")
def start_workflow(data: dict):
    result = run_workflow(data["goal"])
    return {"result": result}