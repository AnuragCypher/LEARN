from typing import Generator
from fastapi import FastAPI
import uvicorn
from my_app.endpoints.my_apis import route
from my_app.midddlewares.logging_middleware import MyMiddleWare


app = FastAPI()
app.add_middleware(MyMiddleWare)


app.include_router(route, prefix="/api")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
