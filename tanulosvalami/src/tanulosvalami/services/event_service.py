"""
Event Service
Handles all business logic for Events
Sits between Routes and Repository
"""
from typing import Type

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from tanulosvalami.repositories.event_repository import EventRepository
from tanulosvalami.schemas.event import EventCreate, EventUpdate
from tanulosvalami.models.event import Event


class EventService:

    def __init__(self, db: Session):
        """
        Creates an EventRepository instance with the database session
        """
        self.repository = EventRepository(db)

    def get_all_events(self) -> list[Type[Event]]:
        """
        Fetch all events
        No business logic needed here, just pass through
        """
        return self.repository.get_all()

    def get_event_by_id(self, event_id: int) -> Event:
        """
        Fetch a single event by ID
        Raises 404 if not found
        """
        event = self.repository.get_by_id(event_id)

        if not event:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Event with id {event_id} not found"
            )

        return event

    def create_event(self, event_data: EventCreate) -> Event:
        """
        Create a new event in the database.
        """
        return self.repository.create(event_data)

    def update_event(self, event_id: int, event_data: EventUpdate) -> Event:
        """
        Update an existing event
        1. Check if event exists (raises 404 if not)
        2. Update the event
        """
        # Check if event exists (this is still good!)
        existing_event = self.get_event_by_id(event_id)

        # Pass the data straight to the repository
        return self.repository.update(event_id, event_data)

    def delete_event(self, event_id: int) -> dict:
        """
        Delete an event by ID
        Raises 404 if not found
        Returns a success message
        """
        # Check if event exists (raises 404 if not)
        self.get_event_by_id(event_id)

        self.repository.delete(event_id)

        return {"message": f"Event with id {event_id} successfully deleted"}