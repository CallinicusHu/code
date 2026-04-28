"""
Main Application Entry Point
Initializes FastAPI and registers all routes
"""
from fastapi import FastAPI
from tanulosvalami.database import Base, engine
from tanulosvalami.api.event_routes import router as event_router
from tanulosvalami.api.feedback_routes import router as feedback_router


# Create all database tables on startup
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="Feedback API",
    description="API for managing Events and their Feedbacks",
    version="1.0.0"
)

# Register routers
app.include_router(event_router)
app.include_router(feedback_router)


@app.get("/", tags=["Health"])
def health_check():
    """
    GET /
    Simple health check endpoint
    Returns a message confirming the API is running
    """
    return {"status": "ok", "message": "Feedback API is running!"}