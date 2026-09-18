from fastapi import FastAPI

app = FastAPI(title="Agro Predict Backend")


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
