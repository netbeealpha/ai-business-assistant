from sqlalchemy.orm import Session

from app.models.conversation import Conversation
from app.models.message import Message



def create_conversation(
    db: Session,
    organization_id: int,
    user_id: int,
    title: str | None = None
):

    conversation = Conversation(
        organization_id=organization_id,
        user_id=user_id,
        title=title
    )


    db.add(conversation)

    db.commit()

    db.refresh(conversation)


    return conversation



def add_message(
    db: Session,
    conversation_id: int,
    role: str,
    content: str
):

    message = Message(
        conversation_id=conversation_id,
        role=role,
        content=content
    )


    db.add(message)

    db.commit()

    db.refresh(message)


    return message



def get_conversation_history(
    db: Session,
    conversation_id: int
):

    conversation = (
        db.query(Conversation)
        .filter(
            Conversation.id == conversation_id
        )
        .first()
    )


    if not conversation:
        return None


    return conversation.messages