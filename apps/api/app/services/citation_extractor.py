from typing import List



def extract_citations(
    result: dict
) -> List[dict]:


    citations = []


    for item in result.get(
        "knowledge_results",
        []
    ):

        citation = item.get(
            "citation"
        )


        if citation:

            citations.append(
                citation
            )


    return citations