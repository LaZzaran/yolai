from fastapi import FastAPI
from routers import presentation_router

app = FastAPI()

# Rota tanımlamaları
app.include_router(presentation_router.router)