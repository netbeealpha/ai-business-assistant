def compose_product_response(
    products: list[dict],
    intent: str = "general"
) -> str:

    if not products:
        return "No matching product found."


    product = products[0]


    if intent == "availability":

        return (
            f"{product['name']} is "
            f"{product['stock_status']}.\n"
            f"Available quantity: "
            f"{product['stock_quantity']}"
        )


    if intent == "price":

        return (
            f"{product['name']} price is "
            f"{product['sale_price']} "
            f"{product['currency']}."
        )


    if intent == "details":

        return (
            f"Product: {product['name']}\n"
            f"Brand: {product.get('brand')}\n"
            f"Category: {product.get('category')}\n"
            f"Description: {product.get('description')}"
        )


    # default response

    return (
        f"Product: {product['name']}\n"
        f"Brand: {product.get('brand', 'N/A')}\n"
        f"Category: {product.get('category', 'N/A')}\n"
        f"Price: {product.get('sale_price')} "
        f"{product.get('currency', '')}\n"
        f"Stock: {product.get('stock_status', 'unknown')}\n"
        f"Available Quantity: {product.get('stock_quantity', 'N/A')}\n"
        f"SKU: {product.get('sku', 'N/A')}"
    )

def compose_knowledge_response(
    chunks: list[dict]
) -> str:

    if not chunks:

        return "No relevant information found."


    responses = []


    for chunk in chunks:

        responses.append(
            f"""
Information:

{chunk['text']}

Source ID:
{chunk.get('source_id')}

Chunk ID:
{chunk.get('chunk_id')}
"""
        )


    return "\n".join(
        responses
    ).strip()



def compose_response(
    result: dict
) -> str:
    print("COMPOSER INPUT:❤️", result)

    responses = []


    if result.get("product_results"):

        product_response = compose_product_response(
            result["product_results"],
            result.get("followup_intent", "general")
        )

        if product_response:
            responses.append(product_response)


    if result.get("knowledge_results"):

        responses.append(
            compose_knowledge_response(
                result["knowledge_results"]
            )
        )


    if not responses:

        return "No information found."


    return "\n\n".join(
        responses
    )