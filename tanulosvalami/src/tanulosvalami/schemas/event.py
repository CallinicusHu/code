"""
Pydantic schemas for Event
EventBase: shared fields
EventCreate: for POST requests (creating)
EventUpdate: for PUT requests (updating)
EventResponse: for API responses
"""
from datetime import datetime
from pydantic import BaseModel, Field


class EventBase(BaseModel):
    """
    Shared fields between all Event schemas
    """
    name: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Name of the event",
        examples=["Team Building 2026"]
    )
    description: str | None = Field(
        default=None,
        max_length=1000,
        description="Optional description of the event",
        examples=["Annual team building event"]
    )
    location: str | None = Field(
        default=None,
        min_length=2,
        max_length=200,
        description="Location of the event",
        examples=["Vác, Office"]
    )
    date: datetime = Field(
        ...,
        description="Date and time of the event",
        examples=["2026-05-25T18:00:00"]
    )
    gm: str = Field(
        ...,
        min_length=2,
        max_length=200,
        description="Game Master for the event",
        examples=["Admin"]
    )


class EventCreate(EventBase):
    """
    Schema for creating a new Event
    Used in: POST /events
    """
    pass


class EventUpdate(BaseModel):
    class EventUpdate(BaseModel):
        """
        Schema for updating an Event
        All fields are optional - only send what you want to change
        Used in: PUT /events/{id}
        """
        name: str | None = Field(
            default=None,
            min_length=3,
            max_length=100
        )
        date: datetime | None = None
        gm: str | None = Field(
            default=None,
            min_length=2,
            max_length=200
        )
        location: str | None = Field(
            default=None,
            min_length=2,
            max_length=200
        )
        description: str | None = Field(
            default=None,
            max_length=1000
        )


class EventResponse(EventBase):
    """
    Schema for API responses
    Includes all fields + database generated fields
    Used in: All responses
    """
    id: int
    created_at: datetime

    model_config = {"from_attributes": True}