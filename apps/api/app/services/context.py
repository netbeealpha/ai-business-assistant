from sqlalchemy.orm import Session

from app.models.message import Message



def get_conversation_context(
    db: Session,
    conversation_id: int,
    limit: int = 10
):

    messages = (
        db.query(Message)
        .filter(
            Message.conversation_id == conversation_id
        )
        .order_by(
            Message.created_at.desc()
        )
        .limit(limit)
        .all()
    )


    messages.reverse()


    context = []


    for message in messages:

        context.append(
            {
                "role": message.role,
                "content": message.content
            }
        )


    return context