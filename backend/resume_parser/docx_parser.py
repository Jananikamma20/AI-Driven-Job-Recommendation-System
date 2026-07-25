from docx import Document

class DOCXParser:

    def __init__(self):
        pass


    def extract_text(self, docx_path):
        

        text = ""

        try:

            document = Document(docx_path)

            for paragraph in document.paragraphs:

                if paragraph.text.strip():

                    text += paragraph.text + "\n"

        except Exception as e:

            print("Error:", e)

        return text