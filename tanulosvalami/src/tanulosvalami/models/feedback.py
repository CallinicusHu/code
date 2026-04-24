"""
Feedback SQLAlchemy model
Stores user feedback for events
"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship

from tanulosvalami.database import Base


class Feedback(Base):
    """
    Feedback model - user feedback for events

    Attributes:
        id: Primary key
        event_id: Foreign key to Event
        user_name: Name of the user giving feedback
        rating: Rating (1-5)
        comment: Optional text comment
        created_at: Timestamp when feedback was created

    Relationships:
        event: Related Event object
    """
    __tablename__ = "feedbacks"

    # Primary Key
    id = Column(Integer, primary_key=True, index=True)

    # Foreign Key to Event
    event_id = Column(
        Integer,
        ForeignKey("events.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    # User Information
    user_name = Column(String(100), nullable=False)

    # Rating (1-5)
    rating = Column(Integer, nullable=False)

    # Optional Comment
    comment = Column(Text, nullable=True)

    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    event = relationship("Event", back_populates="feedbacks")

    # Constraints
    __table_args__ = (
        CheckConstraint('rating >= 1 AND rating <= 5', name='check_rating_range'),
    )

    def __repr__(self):
        return f"<Feedback(id={self.id}, event_id={self.event_id}, rating={self.rating}, user='{self.user_name}')>"