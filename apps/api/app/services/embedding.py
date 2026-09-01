from sentence_transformers import SentenceTransformer
from sqlalchemy.orm import Session

from app.models.knowledge_chunk import KnowledgeChunk


_model = None


def get_embedding_model():

    global _model

    if _model is None:

        _model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    return _model



def generate_embedding(
    text: str
) -> list[float]:

    model = get_embedding_model()

    embedding = model.encode(
        text
    )

    return embedding.tolist()



def regenerate_chunk_embeddings(
    db: Session
):

    chunks = (
        db.query(KnowledgeChunk)
        .filter(
            KnowledgeChunk.embedding.is_(None)
        )
        .all()
    )


    updated = 0


    for chunk in chunks:

        chunk.embedding = generate_embedding(
            chunk.text
        )

        updated += 1


    db.commit()

    return updated