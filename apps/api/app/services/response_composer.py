def compose_product_response(
    products: list[dict]
) -> str:

    if not products:

        return "No matching product found."


    responses = []


    for product in products:

        responses.append(
            f"""
Product: {product['name']}
Brand: {product.get('brand', 'N/A')}
Category: {product.get('category', 'N/A')}
Price: {product.get('sale_price', product.get('regular_price'))} {product.get('currency', '')}
Stock: {product.get('stock_status', 'unknown')}
Available Quantity: {product.get('stock_quantity', 'N/A')}
SKU: {product.get('sku', 'N/A')}
"""
        )


    return "\n".join(
        responses
    ).strip()


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


    responses = []


    if result.get("product_results"):

        responses.append(
            compose_product_response(
                result["product_results"]
            )
        )


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