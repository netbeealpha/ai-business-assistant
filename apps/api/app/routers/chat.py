from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session


from app.database.session import get_db
from app.schemas.chat import (
    ChatRequest,
    ChatResponse
)

from app.dependencies.auth import get_current_user

from app.models.user import User


from app.services.conversation import (
    create_conversation,
    add_message
)

from app.services.assistant_service import (
    ask_assistant
)
from app.services.context import (
    get_conversation_context
)

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)



@router.post(
    "",
    response_model=ChatResponse
)
def chat(
    request: ChatRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    # Create new conversation if not provided

    if request.conversation_id is None:

        conversation = create_conversation(
            db=db,
            organization_id=current_user.organization_id,
            user_id=current_user.id,
            title=request.message[:50]
        )

        conversation_id = conversation.id


    else:

        conversation_id = request.conversation_id


    context = get_conversation_context(
        db=db,
        conversation_id=conversation_id
    )
    print("CHAT CONTEXT:", context)
    print("CURRENT MESSAGE:", request.message)
    # Save user message

    add_message(
        db=db,
        conversation_id=conversation_id,
        role="user",
        content=request.message
    )

    

    # Generate assistant answer

    answer = ask_assistant(
        db=db,
        query=request.message,
        organization_id=current_user.organization_id,
        context=context
    )


    # Save assistant message

    add_message(
        db=db,
        conversation_id=conversation_id,
        role="assistant",
        content=answer["answer"]
    )


    return {
        "conversation_id": conversation_id,
        "answer": answer["answer"],
        "sources": answer["sources"]
    }