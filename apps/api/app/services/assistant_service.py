from sqlalchemy.orm import Session

from app.services.context_resolver import (
    resolve_context_query
)

from app.services.agent_orchestrator import (
    run_agent
)

from app.services.agent_response import (
    normalize_agent_response
)

from app.services.answer_context import (
    build_answer_context
)

from app.services.answer_generator import (
    generate_answer
)



def ask_assistant(
    db: Session,
    query: str,
    organization_id: int,
    context: list[dict] | None = None
) -> str:


    # Resolve conversation context
    resolved_query = resolve_context_query(
        query=query,
        context=context
    )


    print(
        "ASSISTANT ORIGINAL:",
        query
    )

    print(
        "ASSISTANT CONTEXT:",
        context
    )

    print(
        "ASSISTANT RESOLVED:",
        resolved_query
    )


    # Run AI Agent
    agent_result = run_agent(
        query=resolved_query,
        db=db,
        organization_id=organization_id
    )


    print(
        "AGENT RESULT:",
        agent_result
    )


    # Normalize tool output
    result = normalize_agent_response(
        agent_result
    )


    print(
        "NORMALIZED RESULT:",
        result
    )


    # Build LLM context
    context_text = build_answer_context(
        result
    )


    print(
        "ANSWER CONTEXT:",
        context_text
    )


    # Generate final business answer
    response = generate_answer(
        question=query,
        context=context_text
    )


    return response