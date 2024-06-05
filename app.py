# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from textResponse.router.textResponseRouter import router as textResponseRouter
from onboarding.router.onboardingRouter import router as onboardingRouter
from textResponse.router.chatsRouter import chats_router

app = FastAPI()

# Agrega las rutas de la API
app.include_router(textResponseRouter, tags=["Text Response"], prefix="/api/v1/textResponse")
app.include_router(onboardingRouter, tags=["Onboarding"], prefix="/api/v1/onboarding")
app.include_router(chats_router, tags=["Chat"], prefix="/api/v1")

# Lista de orígenes permitidos
origins = [
    "http://10.0.2.2:3000",  # Android emulator
    "http://localhost:3000",  # iOS emulator
    "https://sparkai-desarrollo.up.railway.app",  # URL de tu servidor
    # otras direcciones de origen permitidas
]

# Agrega el middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



