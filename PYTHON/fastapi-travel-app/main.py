from fastapi import FastAPI
import uvicorn
from travel_app.endpoints.travel_api import route

app = FastAPI()

app.include_router(route, prefix="/api")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
