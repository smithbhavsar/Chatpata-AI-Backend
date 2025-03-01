from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import customers, restaurants, menu_items

app = FastAPI(title="Chatpata AI Backend")

# Allow frontend (React app) to access the backend
origins = [
    "http://localhost:5173",  # React Dev Server
    "https://your-production-frontend.com"  # Add production frontend domain
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow only specific origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, PUT, DELETE)
    allow_headers=["*"],  # Allow all headers
)

# Include API routes
app.include_router(customers.router, prefix="/customers", tags=["Customers"])
app.include_router(restaurants.router, prefix="/restaurants", tags=["Restaurants"])
app.include_router(menu_items.router, prefix="/menu-items", tags=["Menu Items"])

@app.get("/")
def home():
    return {"message": "Chatpata AI API is running!"}
