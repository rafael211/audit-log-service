from fastapi import FastAPI

app = FastAPI(title="Audit Log Service")


@app.get("/")
def health_check():
    return {"status": "ok"}
