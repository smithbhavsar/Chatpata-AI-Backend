from pydantic import BaseModel
from typing import Optional

# Customer Schema
class CustomerSchema(BaseModel):
    name: str
    email: Optional[str] = None
    phone: str
    address: Optional[str] = None

# Restaurant Schema
class RestaurantSchema(BaseModel):
    name: str
    address: str
    phone: str
    email: str
    logo: Optional[str] = None
    operating_hours: Optional[dict] = None

# Menu Item Schema
class MenuItemSchema(BaseModel):
    name: str
    description: str
    price: float
    category: str
    image: Optional[str] = None
    is_available: bool = True
    is_vegetarian: bool = False
    is_vegan: bool = False
    is_gluten_free: bool = False
    restaurant_id: str
