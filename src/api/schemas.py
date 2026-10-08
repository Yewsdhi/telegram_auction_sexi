from datetime import datetime, timedelta
from typing import Optional

from pydantic import BaseModel, Field


class AuctionItemBase(BaseModel):
    title: str
    description: Optional[str] = None
    price: float
    is_start_price: bool
    photo: str
    owner_id: int
    start_date: datetime = Field(default_factory=datetime.now)
    end_date: datetime = Field(default_factory=lambda: datetime.now() + timedelta(days=365))


class AuctionItemCreate(AuctionItemBase):
    is_start_price: bool = True


class AuctionItemRead(AuctionItemBase):
    id: int
    is_sold: bool

    class Config:
        orm_mode = True


class AuctionItemUpdateReq(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    is_start_price: Optional[bool] = None
    owner_id: Optional[int] = None
    is_sold: Optional[bool] = None
    end_date: Optional[datetime] = None


class AuctionUserCreate(BaseModel):
    username: str


class AuctionUserRead(BaseModel):
    id: int
    username: str
    items: list[AuctionItemRead] = []

    class Config:
        orm_mode = True
