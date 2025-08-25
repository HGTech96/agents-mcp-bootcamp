from fastapi import FastAPI

app = FastAPI(title="Agents + MCP Bootcamp API", version="0.1.0")

@app.get("/health", tags=["system"])
async def health():
    return {"status": "ok"}
