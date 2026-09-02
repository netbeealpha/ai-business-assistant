def build_answer_context(
    result: dict
) -> str:


    parts = []


    # Product information
    if result.get("product_results"):

        parts.append(
            "Product Information:\n"
            + str(
                result["product_results"]
            )
        )


    # Knowledge information with citations
    if result.get("knowledge_results"):

        for item in result["knowledge_results"]:

            text = item.get(
                "text",
                ""
            )


            citation = item.get(
                "citation",
                {}
            )


            source_information = ""


            if citation:

                source_information = (
                    "\n\nSource Information:\n"
                    f"Document: {citation.get('document', 'Unknown')}\n"
                    f"Title: {citation.get('title', 'Unknown')}\n"
                    f"Page: {citation.get('page_number', 'Unknown')}"
                )


            parts.append(
                "Information:\n"
                + text
                + source_information
            )


    return "\n\n-----------------\n\n".join(parts)