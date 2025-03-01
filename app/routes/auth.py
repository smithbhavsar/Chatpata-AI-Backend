# from fastapi import APIRouter, Depends, HTTPException
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from datetime import datetime, timedelta
# from jose import JWTError, jwt
# import os
# from dotenv import load_dotenv

# load_dotenv()

# router = APIRouter()

# # Security settings
# SECRET_KEY = os.getenv("SECRET_KEY")
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 60

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# # Generate JWT Token
# def create_access_token(data: dict, expires_delta: int = ACCESS_TOKEN_EXPIRE_MINUTES):
#     to_encode = data.copy()
#     expire = datetime.utcnow() + timedelta(minutes=expires_delta)
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt

# # Login route (Mock login, replace with database authentication)
# @router.post("/token")
# def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
#     # Replace this with actual database authentication
#     if form_data.username != "admin" or form_data.password != "password":
#         raise HTTPException(status_code=401, detail="Incorrect username or password")

#     access_token = create_access_token(data={"sub": form_data.username})
#     return {"access_token": access_token, "token_type": "bearer"}

# # Verify JWT Token
# def verify_access_token(token: str = Depends(oauth2_scheme)):
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         return payload
#     except JWTError:
#         raise HTTPException(status_code=401, detail="Invalid token")
