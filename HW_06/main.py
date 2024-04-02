from database import SessionLocal
from uvicorn import run as uvi_run
import project.models
from fastapi import FastAPI
from project.routers import router as user_router
from project.routers import router as order_router
from project.routers import router as product_router


app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.include_router(user_router)
app.include_router(order_router)
app.include_router(product_router)

if __name__ == "__main__":
    uvi_run("main:app", host="127.0.0.1", port=8000, reload=True)
