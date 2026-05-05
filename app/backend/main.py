from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "DevOps CI/CD + GitOps Project Running"}

@app.get("/health")
def health():
    return {
        "status": "OK",
        "system": "Healthy"
    }

@app.get("/deploy-status")
def deploy_status():
    return {
        "status": "success",
        "pipeline": "CI/CD + Terraform + Kubernetes",
        "message": "Deployment pipeline is working fine"
    }