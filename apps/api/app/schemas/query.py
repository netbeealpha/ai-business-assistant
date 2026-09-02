from pydantic import BaseModel



class QueryIntent(BaseModel):

    is_product: bool = False

    is_knowledge: bool = False