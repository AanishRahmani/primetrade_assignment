from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    username: str = Field(
        ...,
        min_length=3,
        max_length=50,
        pattern="^[a-zA-Z0-9_-]+$",
        description="Username for the account",
        examples=["john_doe"]
    )
    email: EmailStr = Field(
        ...,
        description="Valid email address",
        examples=["user@example.com"]
    )
    password: str = Field(
        ...,
        min_length=8,
        max_length=72,
        description="Password (8-72 characters)",
        examples=["SecurePass123!"]
    )


class UserLogin(BaseModel):
    email: EmailStr = Field(
        ...,
        description="Registered email address",
        examples=["user@example.com"]
    )
    password: str = Field(
        ...,
        description="Account password",
        examples=["SecurePass123!"]
    )


class UserOut(BaseModel):
    id: int = Field(
        ...,
        description="Unique user identifier"
    )
    username: str = Field(
        ...,
        description="Username of the user"
    )
    email: EmailStr = Field(
        ...,
        description="Email address of the user"
    )
    role: str = Field(
        ...,
        description="User role (e.g., 'user', 'admin')",
        examples=["user"]
    )

    class Config:
        from_attributes = True
