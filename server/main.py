from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from middlewares.exception_handlers import catch_exception_middleware
from routes.upload_pdfs import router as upload_router
from routes.ask_queries import router as ask_router


app = FastAPI(title="Medical Assistant App",description="API for medical chatbot")

#CORSSETUP
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_headers=["*"],
    allow_credentials=["*"],
    allow_methods=["*"]
)

#middleware exception handlers
app.middleware("http")(catch_exception_middleware)

#routers
#1. upload pdfs
app.include_router(upload_router)
#2. ask queries
app.include_router(ask_router) 