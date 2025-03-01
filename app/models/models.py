from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Text, JSON, DateTime, Float
from sqlalchemy.sql import func
from .database import Base

# Customers Table
class Customer(Base):
    __tablename__ = "customers"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=True)
    phone = Column(String, nullable=False, unique=True)
    address = Column(Text, nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

# Restaurants Table
class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    address = Column(Text, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    logo = Column(Text, nullable=True)
    operating_hours = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

# Menu Items Table
class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    price = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    image = Column(Text, nullable=True)
    is_available = Column(Boolean, default=True)
    is_vegetarian = Column(Boolean, default=False)
    is_vegan = Column(Boolean, default=False)
    is_gluten_free = Column(Boolean, default=False)
    restaurant_id = Column(String, ForeignKey("restaurants.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
