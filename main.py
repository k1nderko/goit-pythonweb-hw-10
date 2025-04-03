from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.contacts import router as contacts_router
from src.api.auth import router as auth_router

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(contacts_router)
app.include_router(auth_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Contact API"}
