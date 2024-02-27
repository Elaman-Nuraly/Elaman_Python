from docx import Document

def create_word_file(text):
    document = Document()
    document.add_paragraph(text)
    document.save('output.docx')

if __name__ == "__main__":
    text = input("Для того чтобы сохранить в Word-файле, введите текст: ")
    create_word_file(text)
    print("Сохранен в Word-файл!")
