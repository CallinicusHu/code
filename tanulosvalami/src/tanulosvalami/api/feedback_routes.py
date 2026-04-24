"""
Feedback Routes
Handles all HTTP requests for Feedbacks
All routes are nested under /events/{event_id}/feedbacks
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from tanulosvalami.database import get_db
from tanulosvalami.services.feedback_service import FeedbackService
from tanulosvalami.schemas.feedback import FeedbackCreate, FeedbackResponse

router = APIRouter(
    prefix="/events/{event_id}/feedbacks",
    tags=["Feedbacks"]
)


def get_feedback_service(db: Session = Depends(get_db)) -> FeedbackService:
    """
    Dependency that creates a FeedbackService instance
    with the database session
    """
    return FeedbackService(db)


@router.get("/", response_model=list[FeedbackResponse])
def get_all_feedbacks(
    event_id: int,
    service: FeedbackService = Depends(get_feedback_service)
):
    """
    GET /events/{event_id}/feedbacks/
    Returns all feedbacks for a specific event
    Raises 404 if event not found
    """
    return service.get_all_feedbacks_by_event(event_id)


@router.get("/{feedback_id}", response_model=FeedbackResponse)
def get_feedback(
    event_id: int,
    feedback_id: int,
    service: FeedbackService = Depends(get_feedback_service)
):
    """
    GET /events/{event_id}/feedbacks/{feedback_id}
    Returns a single feedback by ID
    Raises 404 if event or feedback not found
    """
    return service.get_feedback_by_id(event_id, feedback_id)


@router.post("/", response_model=FeedbackResponse, status_code=201)
def create_feedback(
    event_id: int,
    feedback_data: FeedbackCreate,
    service: FeedbackService = Depends(get_feedback_service)
):
    """
    POST /events/{event_id}/feedbacks/
    Creates a new feedback for an event
    Raises 404 if event not found
    Raises 400 if rating invalid
    """
    return service.create_feedback(event_id, feedback_data)


@router.delete("/{feedback_id}")
def delete_feedback(
    event_id: int,
    feedback_id: int,
    service: FeedbackService = Depends(get_feedback_service)
):
    """
    DELETE /events/{event_id}/feedbacks/{feedback_id}
    Deletes a feedback by ID
    Raises 404 if event or feedback not found
    """
    return service.delete_feedback(event_id, feedback_id)