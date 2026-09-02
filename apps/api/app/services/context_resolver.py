from typing import List, Dict
import re



def resolve_context_query(
    query: str,
    context: List[Dict] | None = None
) -> str:


    if not context:
        return query


    query_lower = query.lower()


    follow_up_patterns = [
        "it",
        "this",
        "that",
        "available",
        "stock",
        "quantity",
        "how much",
        "is it"
    ]


    is_follow_up = any(
        pattern in query_lower
        for pattern in follow_up_patterns
    )


    if not is_follow_up:
        return query


    # Look at previous assistant answer first
    for message in reversed(context):

        if message["role"] == "assistant":

            assistant_text = message["content"]


            match = re.search(
                r"Product:\s*(.+)",
                assistant_text
            )


            if match:

                return match.group(1).split("\n")[0].strip()


    # fallback: previous user message

    for message in reversed(context):

        if message["role"] == "user":

            return message["content"]


    return query