"""
Pydantic schemas for Feedback
FeedbackBase: shared fields
FeedbackCreate: for POST requests (creating)
FeedbackResponse: for API responses
"""
from datetime import datetime
from pydantic import BaseModel, Field


class FeedbackBase(BaseModel):
    """
    Shared fields between all Feedback schemas
    """
    user_name: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="Name of the user giving feedback",
        examples=["John Doe"]
    )
    rating: int = Field(
        ...,
        ge=1,
        le=5,
        description="Rating between 1 and 5",
        examples=[4]
    )
    comment: str | None = Field(
        default=None,
        max_length=1000,
        description="Optional comment",
        examples=["Great event, loved it!"]
    )


class FeedbackCreate(FeedbackBase):
    """
    Schema for creating a new Feedback
    Used in: POST /events/{event_id}/feedbacks
    """
    pass


class FeedbackResponse(FeedbackBase):
    """
    Schema for API responses
    Includes all fields + database generated fields
    Used in: All responses
    """
    id: int
    event_id: int
    created_at: datetime

    model_config = {"from_attributes": True}