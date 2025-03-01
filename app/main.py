from fastapi import FastAPI
from app.routes import customers, restaurants, menu_items

app = FastAPI(title="Chatpata AI Backend")

# Include API routes
app.include_router(customers.router, prefix="/customers", tags=["Customers"])
app.include_router(restaurants.router, prefix="/restaurants", tags=["Restaurants"])
app.include_router(menu_items.router, prefix="/menu-items", tags=["Menu Items"])

@app.get("/")
def home():
    return {"message": "Chatpata AI API is running!"}
