"""
Feedback Service
Handles all business logic for Feedbacks
Sits between Routes and Repository
"""
from typing import Type

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from tanulosvalami.repositories.feedback_repository import FeedbackRepository
from tanulosvalami.repositories.event_repository import EventRepository
from tanulosvalami.schemas.feedback import FeedbackCreate
from tanulosvalami.models.feedback import Feedback


class FeedbackService:

    def __init__(self, db: Session):
        """
        Creates both repositories since Feedback
        needs to verify that the Event exists
        """
        self.repository = FeedbackRepository(db)
        self.event_repository = EventRepository(db)

    def get_all_feedbacks_by_event(self, event_id: int) -> list[Type[Feedback]]:
        """
        Fetch all feedbacks for a specific event
        1. Check if event exists (raises 404 if not)
        2. Return all feedbacks for that event
        """
        event = self.event_repository.get_by_id(event_id)

        if not event:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Event with id {event_id} not found"
            )

        return self.repository.get_all_by_event(event_id)

    def get_feedback_by_id(self, event_id: int, feedback_id: int) -> Feedback:
        """
        Fetch a single feedback by ID
        1. Check if event exists (raises 404 if not)
        2. Check if feedback exists (raises 404 if not)
        3. Check if feedback belongs to the event (raises 404 if not)
        """
        event = self.event_repository.get_by_id(event_id)

        if not event:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Event with id {event_id} not found"
            )

        feedback = self.repository.get_by_id(feedback_id)

        if not feedback:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Feedback with id {feedback_id} not found"
            )

        if feedback.event_id != event_id:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Feedback with id {feedback_id} not found for event {event_id}"
            )

        return feedback

    def create_feedback(self, event_id: int, feedback_data: FeedbackCreate) -> Feedback:
        """
        Create a new feedback for an event
        1. Check if event exists (raises 404 if not)
        2. Validate rating (raises 400 if invalid)
        3. Create the feedback
        """
        event = self.event_repository.get_by_id(event_id)

        if not event:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Event with id {event_id} not found"
            )

        if not 1 <= feedback_data.rating <= 5:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Rating must be between 1 and 5"
            )

        return self.repository.create(event_id, feedback_data)

    def delete_feedback(self, event_id: int, feedback_id: int) -> dict:
        """
        Delete a feedback by ID
        1. Check if feedback exists and belongs to event (raises 404 if not)
        2. Delete the feedback
        3. Return a success message
        """
        # This already checks event and feedback existence
        self.get_feedback_by_id(event_id, feedback_id)

        self.repository.delete(feedback_id)

        return {"message": f"Feedback with id {feedback_id} successfully deleted"}