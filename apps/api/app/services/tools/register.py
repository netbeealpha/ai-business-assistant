from app.services.tools.registry import register_tool

from app.services.product_tool import search_products

from app.services.retrieval import retrieve_relevant_chunks



def register_all_tools():

    register_tool(
        "product_search",
        search_products
    )


    register_tool(
        "knowledge_search",
        retrieve_relevant_chunks
    )