import torch

from transformers import AutoTokenizer, AutoModel


_model = None
_tokenizer = None


MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"



def get_embedding_model():

    global _model, _tokenizer


    if _model is None:

        _tokenizer = AutoTokenizer.from_pretrained(
            MODEL_NAME
        )

        _model = AutoModel.from_pretrained(
            MODEL_NAME
        )

        _model.eval()


    return _tokenizer, _model



def generate_embedding(
    text: str
) -> list[float]:


    tokenizer, model = get_embedding_model()


    inputs = tokenizer(
        text,
        padding=True,
        truncation=True,
        return_tensors="pt"
    )


    with torch.no_grad():

        outputs = model(
            **inputs
        )


    token_embeddings = outputs.last_hidden_state

    attention_mask = inputs["attention_mask"]


    mask = attention_mask.unsqueeze(
        -1
    ).expand(
        token_embeddings.size()
    ).float()


    summed = torch.sum(
        token_embeddings * mask,
        dim=1
    )


    counts = torch.clamp(
        mask.sum(dim=1),
        min=1e-9
    )


    embedding = summed / counts


    return embedding[0].tolist()