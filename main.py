from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="SaaS Backend",
    description="Backend + AI Event SaaS Platform",
    version="1.0.0"
)  #This matters in interviews!

app.include_router(router)

@app.get("/")
def root():
    return {"message": "SaaS Backend is Alive"}