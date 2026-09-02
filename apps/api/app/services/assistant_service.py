from sqlalchemy.orm import Session

from app.services.query_executor import execute_query

from app.services.response_composer import compose_response



def ask_assistant(
    db: Session,
    query: str,
    organization_id: int
) -> str:


    result = execute_query(
        db=db,
        query=query,
        organization_id=organization_id
    )


    response = compose_response(
        result
    )


    return response