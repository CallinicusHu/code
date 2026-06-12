from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker

#
from tanulosvalami.main import app
from tanulosvalami.models.event import Base
from tanulosvalami.api.event_routes import get_event_service
from tanulosvalami.services.event_service import EventService

#
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_threat": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#
Base.metadata.create_all(bind=engine)


#
def override_get_event_service():
    db = TestingSessionLocal()
    try:
        #
        yield EventService(db)
    finally:
        db.close()


#
app.dependency_overrides[get_event_service] = override_get_event_service

#
client = TestClient(app)


def test_update_event_success():
    """

    :return:
    """

    #
    create_payload = {
        "name": "Original Event",
        "date": "2026-06-15T10:00:00",
        "gm": "OriginalGM",
        "location": "Old Location",
        "description": "Just for testing"
    }
    create_response = client.post("/events/", json=create_payload)
    event_id = create_response.json()["id"]

    #
    update_payload = {
        "location": "Budapest",
        "gm": "SuperAdmin"
    }
    patch_response = client.patch(f"/events/{event_id}", json=update_payload)

    #
    assert patch_response.status_code == 200
    data = patch_response.json()

    #
    assert data["location"] == "Budapest"
    assert data["gm"] == "SuperAdmin"

    #
    assert data["name"] == "Original Event"
