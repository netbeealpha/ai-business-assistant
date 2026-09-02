from app.services.agent_orchestrator import run_agent

from app.services.agent_response import normalize_agent_response

from app.services.response_composer import compose_response

from app.services.context_resolver import resolve_context_query

def ask_assistant(
    db: Session,
    query: str,
    organization_id: int,
    context: list[dict] | None = None
) -> str:


    resolved_query = resolve_context_query(
        query=query,
        context=context
    )


    print("ASSISTANT ORIGINAL:", query)
    print("ASSISTANT CONTEXT:", context)
    print("ASSISTANT RESOLVED:", resolved_query)


    agent_result = run_agent(
        query=resolved_query,
        db=db,
        organization_id=organization_id
    )


    result = normalize_agent_response(
        agent_result
    )


    response = compose_response(
        result
    )


    return response