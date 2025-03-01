from fastapi import APIRouter, HTTPException
from app.supabase_client import supabase

router = APIRouter()

# ✅ Create a new restaurant
@router.post("/")
def add_restaurant(restaurant: dict):
    response = supabase.table("restaurants").insert(restaurant).execute()

    if response.data is None:
        raise HTTPException(status_code=400, detail="Error inserting data into Supabase")

    return {"message": "Restaurant added successfully", "data": response.data}

# ✅ Get all restaurants
@router.get("/")
def get_restaurants():
    response = supabase.table("restaurants").select("*").execute()

    if response.data is None:
        raise HTTPException(status_code=400, detail="Error fetching data from Supabase")

    return response.data

# ✅ Get a specific restaurant by ID
@router.get("/{restaurant_id}")
def get_restaurant(restaurant_id: str):
    response = supabase.table("restaurants").select("*").eq("id", restaurant_id).execute()

    if not response.data:
        raise HTTPException(status_code=404, detail="Restaurant not found")

    return response.data[0]

# ✅ Update a restaurant
@router.put("/{restaurant_id}")
def update_restaurant(restaurant_id: str, updated_data: dict):
    response = supabase.table("restaurants").update(updated_data).eq("id", restaurant_id).execute()

    if response.data is None:
        raise HTTPException(status_code=400, detail="Error updating restaurant in Supabase")

    return {"message": "Restaurant updated successfully", "data": response.data}

# ✅ Delete a restaurant (Cascade delete menu items)
@router.delete("/{restaurant_id}")
def delete_restaurant(restaurant_id: str):
    # Delete all menu items first
    supabase.table("menu_items").delete().eq("restaurant_id", restaurant_id).execute()
    
    # Delete the restaurant
    response = supabase.table("restaurants").delete().eq("id", restaurant_id).execute()

    if response.data is None:
        raise HTTPException(status_code=400, detail="Error deleting restaurant from Supabase")

    return {"message": "Restaurant and its menu items deleted successfully"}
