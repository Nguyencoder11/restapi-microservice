from fastapi import FastAPI, Request
import httpx

app = FastAPI(title="API Gateway")

SERVICES = {
    "users": "http://user-service:8000",
    "auth": "http://auth-service:8001",
    "products": "http://product-service:8002",
}

@app.api_route("/{service}/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def gateway(service: str, path: str, request: Request):
    if service not in SERVICES:
        return {"error": "Service not found"}

    async with httpx.AsyncClient() as client:
        url = f"{SERVICES[service]}/{path}"
        body = await request.body()
        response = await client.request(
            request.method,
            url,
            content=body,
            headers=request.headers
        )
        return response.json()