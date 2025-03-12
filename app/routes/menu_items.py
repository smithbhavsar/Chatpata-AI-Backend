from fastapi import APIRouter, HTTPException
from app.supabase_client import supabase

router = APIRouter()

# ✅ Create a new menu item
@router.post("/{restaurant_id}")
def add_menu_item(menu_item: dict):
    response = supabase.table("menu_items").insert(menu_item).execute()
    if response.data is None:
        raise HTTPException(status_code=400, detail="Error inserting menu item into Supabase")
    return {"message": "Menu item added successfully", "data": response.data}

@router.get("/")
def get_all_menu_items():
    response = supabase.table("menu_items").select("*").execute()

    if response.data is None:
        raise HTTPException(status_code=400, detail="Error fetching menu items from Supabase")

    return response.data

# ✅ Get all menu items for a restaurant
@router.get("/{restaurant_id}")
def get_menu_items(restaurant_id: str):
    response = supabase.table("menu_items").select("*").eq("restaurant_id", restaurant_id).execute()

    if response.data is None:
        raise HTTPException(status_code=400, detail="Error fetching menu items from Supabase")

    return response.data

# ✅ Get a specific menu item
@router.get("/item/{menu_item_id}")
def get_menu_item(menu_item_id: str):
    response = supabase.table("menu_items").select("*").eq("id", menu_item_id).execute()

    if not response.data:
        raise HTTPException(status_code=404, detail="Menu item not found")

    return response.data[0]

# ✅ Update a menu item
@router.put("/{menu_item_id}")
def update_menu_item(menu_item_id: str, updated_data: dict):
    response = supabase.table("menu_items").update(updated_data).eq("id", menu_item_id).execute()

    if response.data is None:
        raise HTTPException(status_code=400, detail="Error updating menu item in Supabase")

    return {"message": "Menu item updated successfully", "data": response.data}

# ✅ Delete a menu item
@router.delete("/{menu_item_id}")
def delete_menu_item(menu_item_id: str):
    response = supabase.table("menu_items").delete().eq("id", menu_item_id).execute()

    if response.data is None:
        raise HTTPException(status_code=400, detail="Error deleting menu item from Supabase")

    return {"message": "Menu item deleted successfully"}
