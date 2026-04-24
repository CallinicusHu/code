"""
Feedback Repository
Handles all database operations for Feedbacks
"""

from typing import Type

from sqlalchemy.orm import Session
from tanulosvalami.models.feedback import Feedback
from tanulosvalami.schemas.feedback import FeedbackCreate


class FeedbackRepository:

    def init(self, db: Session):
        """
        db: SQLAlchemy Session - injected from FastAPI
        """
        self.db = db

    def get_all_by_event(self, event_id: int) -> list[Type[Feedback]]:
        """
        Fetch all feedbacks for a specific event
        """
        return (
            self.db.query(Feedback)
            .filter(Feedback.event_id == event_id)
            .all()
        )

    def get_by_id(self, feedback_id: int) -> Feedback | None:
        """
        Fetch a single feedback by its ID
        Returns None if not found
        """
        return (
            self.db.query(Feedback)
            .filter(Feedback.id == feedback_id)
            .first()
        )

    def create(self, event_id: int, feedback_data: FeedbackCreate) -> Feedback:
        """
        Create a new feedback for an event

Convert schema to model
Attach event_id
Add to database
Commit transaction
Return created feedback
"""

        db_feedback = Feedback(**feedback_data.model_dump(),
                               event_id=event_id)
        self.db.add(db_feedback)
        self.db.commit()
        self.db.refresh(db_feedback)
        return db_feedback

    def delete(self, feedback_id):
        # document why this method is empty because you made it
        pass


def delete(self, feedback_id: int) -> bool:
    """
    Delete a feedback by ID
    Returns True if deleted, False if not found
    """
    db_feedback = self.get_by_id(feedback_id)

    if not db_feedback:
        return False

    self.db.delete(db_feedback)
    self.db.commit()
    return True
