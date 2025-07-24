from typing import Optional, List
from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class User(BaseModel):
    id: int
    username: str
    email: str
    created_at: str
    updated_at: str

    class Config:
        orm_mode = True

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    stock: int

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    stock: int
    created_at: str
    updated_at: str

    class Config:
        orm_mode = True

class ReviewCreate(BaseModel):
    product_id: int
    rating: int
    comment: Optional[str] = None

class Review(BaseModel):
    id: int
    product_id: int
    user_id: int
    rating: int
    comment: Optional[str] = None
    created_at: str

    class Config:
        orm_mode = True

class OrderCreate(BaseModel):
    user_id: int
    product_ids: List[int] = Field(..., description="List of product IDs to include in the order")

class Order(BaseModel):
    id: int
    user_id: int
    total_amount: float
    status: str
    created_at: str
    updated_at: str
    order_items: List[
        {
            "product_id": int,
            "quantity": int
        }
    ]

    class Config:
        orm_mode = True
