from pathlib import Path
import pymupdf
from docx import Document



def extract_text_from_txt(
    file_path: str
) -> str:

    path = Path(file_path)

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        text = file.read()

    return text


def extract_text_from_pdf(
    file_path: str
) -> list[dict]:

    document = pymupdf.open(file_path)

    pages = []

    for page_number, page in enumerate(document, start=1):

        text = page.get_text()

        pages.append(
            {
                "page_number": page_number,
                "text": text
            }
        )

    document.close()

    return pages


def extract_text_from_docx(
    file_path: str
) -> str:

    document = Document(file_path)

    paragraphs = []

    for paragraph in document.paragraphs:

        if paragraph.text.strip():

            paragraphs.append(
                paragraph.text
            )


    return "\n".join(paragraphs)