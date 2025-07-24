import uvicorn
from fastapi import FastAPI, Request, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

from database import engine
from routers import users, products, orders # Add other routers as needed

#Import models for database creation
from models import Base

app = FastAPI(title="Project Build a Modern E-commerce Platform", version="0.1.0", openapi_url="/openapi.json", docs_url="/docs")

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  # Replace with your allowed origins in production
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# Database Initialization
Base.metadata.create_all(bind=engine)

# Router registration
app.include_router(users.router)
app.include_router(products.router)
app.include_router(orders.router) # Add other routers here

# Health check endpoint
@app.get('/health', status_code=status.HTTP_200_OK)
def health_check():
    return {'status': 'OK'}

# Static file serving
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")
    @app.get("/{{file_path:path}}")
    async def serve_frontend(file_path: str, request: Request):
        if file_path.startswith("api"):
            return await request.app.state.router.dispatch(request)
        static_file = os.path.join("static", file_path)
        if os.path.isfile(static_file):
            return FileResponse(static_file)
        return FileResponse("static/index.html")
else:
    print("Warning: 'static' directory not found. Frontend assets will not be served.")

# Exception Handling
@app.exception_handler(Exception)
def handle_exception(request: Request, exc: Exception):
    # Log the exception details
    print(f"An error occurred: {exc}")
    return HTTPException(status_code=500, detail="Internal Server Error")

# Run the application (for development)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
