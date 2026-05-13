from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Customer Support AI Agent API is running"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }
