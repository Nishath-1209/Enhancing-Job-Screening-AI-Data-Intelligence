# Main Orchestration File
print("AI Job Screening System Running...")
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "AI Job Screening System is Working Successfully!"}
