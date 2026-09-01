from fastapi import FastAPI
from sqlalchemy import text

from app.database.connection import engine

from app.routers.auth import router as auth_router
from app.routers.organizations import router as organization_router
from app.routers.users import router as user_router
from app.routers.products import router as product_router
from app.routers.faqs import router as faq_router
from app.routers.knowledge_sources import router as knowledge_source_router
from app.routers.upload import router as upload_router
from app.routers.knowledge_chunks import router as knowledge_chunk_router

app = FastAPI(
    title="AI Business Assistant API",
    version="0.1.0"
)

# Register API routers
app.include_router(organization_router)
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(product_router)
app.include_router(faq_router)
app.include_router(knowledge_source_router)
app.include_router(upload_router)
app.include_router(knowledge_chunk_router)

@app.get("/health")
def health_check():

    return {
        "status": "healthy",
        "service": "AI Business Assistant API"
    }


@app.get("/database-test")
def database_test():

    with engine.connect() as connection:

        result = connection.execute(
            text("SELECT 1")
        )

        value = result.scalar()

    return {
        "database": "connected",
        "test_value": value
    }