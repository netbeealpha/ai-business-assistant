def split_text_into_chunks(
    text: str,
    chunk_size: int = 1000,
    overlap: int = 200
) -> list[str]:

    chunks = []

    start = 0

    text_length = len(text)


    while start < text_length:

        end = start + chunk_size

        chunk = text[start:end]


        if chunk.strip():

            chunks.append(chunk)


        if end >= text_length:
            break


        start = end - overlap


    return chunks