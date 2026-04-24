"""
Event Routes
Handles all HTTP requests for Events
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from tanulosvalami.database import get_db
from tanulosvalami.services.event_service import EventService
from tanulosvalami.schemas.event import EventCreate, EventUpdate, EventResponse

router = APIRouter(
    prefix="/events",
    tags=["Events"]
)


def get_event_service(db: Session = Depends(get_db)) -> EventService:
    """
    Dependency that creates an EventService instance
    with the database session
    """
    return EventService(db)


@router.get("/", response_model=list[EventResponse])
def get_all_events(
    service: EventService = Depends(get_event_service)
):
    """
    GET /events/
    Returns all events
    """
    return service.get_all_events()


@router.get("/{event_id}", response_model=EventResponse)
def get_event(
    event_id: int,
    service: EventService = Depends(get_event_service)
):
    """
    GET /events/{event_id}
    Returns a single event by ID
    Raises 404 if not found
    """
    return service.get_event_by_id(event_id)


@router.post("/", response_model=EventResponse, status_code=201)
def create_event(
    event_data: EventCreate,
    service: EventService = Depends(get_event_service)
):
    """
    POST /events/
    Creates a new event
    Raises 400 if end_date before start_date
    """
    return service.create_event(event_data)


@router.patch("/{event_id}", response_model=EventResponse)
def update_event(
    event_id: int,
    event_data: EventUpdate,
    service: EventService = Depends(get_event_service)
):
    """
    PATCH /events/{event_id}
    Updates an existing event
    Raises 404 if not found
    Raises 400 if dates are invalid
    """
    return service.update_event(event_id, event_data)


@router.delete("/{event_id}")
def delete_event(
    event_id: int,
    service: EventService = Depends(get_event_service)
):
    """
    DELETE /events/{event_id}
    Deletes an event by ID
    Raises 404 if not found
    """
    return service.delete_event(event_id)
