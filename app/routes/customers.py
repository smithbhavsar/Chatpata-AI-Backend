from fastapi import APIRouter, HTTPException
from app.supabase_client import supabase

router = APIRouter()

# ✅ Create a new customer
@router.post("/")
def add_customer(customer: dict):
    response = supabase.table("customers").insert(customer).execute()

    if response.data is None:
        raise HTTPException(status_code=400, detail="Error inserting customer into Supabase")

    return {"message": "Customer added successfully", "data": response.data}

# ✅ Get all customers
@router.get("/")
def get_customers():
    response = supabase.table("customers").select("*").execute()

    if response.data is None:
        raise HTTPException(status_code=400, detail="Error fetching customers from Supabase")

    return response.data

# ✅ Get a specific customer by ID
@router.get("/{customer_id}")
def get_customer(customer_id: str):
    response = supabase.table("customers").select("*").eq("id", customer_id).execute()

    if not response.data:
        raise HTTPException(status_code=404, detail="Customer not found")

    return response.data[0]

# ✅ Update a customer
@router.put("/{customer_id}")
def update_customer(customer_id: str, updated_data: dict):
    response = supabase.table("customers").update(updated_data).eq("id", customer_id).execute()

    if response.data is None:
        raise HTTPException(status_code=400, detail="Error updating customer in Supabase")

    return {"message": "Customer updated successfully", "data": response.data}

# ✅ Delete a customer
@router.delete("/{customer_id}")
def delete_customer(customer_id: str):
    response = supabase.table("customers").delete().eq("id", customer_id).execute()

    if response.data is None:
        raise HTTPException(status_code=400, detail="Error deleting customer from Supabase")

    return {"message": "Customer deleted successfully"}
