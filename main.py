from datetime import date
from typing import Optional

import uvicorn
from fastapi import FastAPI, Query, Depends
from pydantic import BaseModel
from bookings.router import router as router_bookings

app = FastAPI()

app.include_router(router_bookings)


class SHotelGet(BaseModel):
    address: str
    name: str
    stars: float


class BookingCustomGet:
    def __init__(self, location: str, date_from: date, date_to: date, has_spa: Optional[bool] = None,
                 starts: Optional[int] = Query(None, ge=1, le=5)):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.has_spa = has_spa
        self.starts = starts


@app.get("/")
async def root(search_args: BookingCustomGet = Depends()):
    hotel = [
        {
            "location": "123 Main St",
            "date_from": "2023-22-11",
            "date_to": "2024-22-11",
            "has_spa": False,
            "stars": 5.0
        }
    ]
    return hotel


class SBookingPost(BaseModel):
    room_id: int
    date_from: date
    date_to: date


@app.post("/boking")
async def add_book(booking: SBookingPost):
    pass


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8001)
