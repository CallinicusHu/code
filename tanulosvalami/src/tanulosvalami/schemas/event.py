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
    title: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Title of the event",
        examples=["Team Building 2024"]
    )
    description: str | None = Field(
        default=None,
        max_length=1000,
        description="Optional description of the event",
        examples=["Annual team building event"]
    )
    location: str = Field(
        ...,
        min_length=2,
        max_length=200,
        description="Location of the event",
        examples=["Budapest, Office"]
    )
    event_date: datetime = Field(
        ...,
        description="Date and time of the event",
        examples=["2024-06-15T10:00:00"]
    )


class EventCreate(EventBase):
    """
    Schema for creating a new Event
    Used in: POST /events
    """
    pass


class EventUpdate(BaseModel):
    """
    Schema for updating an Event
    All fields are optional - only send what you want to change
    Used in: PUT /events/{id}
    """
    title: str | None = Field(
        default=None,
        min_length=3,
        max_length=100
    )
    description: str | None = Field(
        default=None,
        max_length=1000
    )
    location: str | None = Field(
        default=None,
        min_length=2,
        max_length=200
    )
    event_date: datetime | None = None


class EventResponse(EventBase):
    """
    Schema for API responses
    Includes all fields + database generated fields
    Used in: All responses
    """
    id: int
    created_at: datetime

    model_config = {"from_attributes": True}