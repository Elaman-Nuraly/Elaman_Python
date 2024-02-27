import sys
import os
import requests
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QWidget

class JsonPlaceholderApp(QMainWindow):

    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("JSON Placeholder Viewer")
        self.setGeometry(100, 100, 500, 400)
        self.id_label = QLabel("Enter post ID:")
        self.id_entry = QLineEdit()
        self.fetch_button = QPushButton("Fetch Data")
        self.output_text = QTextEdit()

        layout = QVBoxLayout()
        layout.addWidget(self.id_label)
        layout.addWidget(self.id_entry)
        layout.addWidget(self.fetch_button)
        layout.addWidget(self.output_text)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
        self.fetch_button.clicked.connect(self.fetch_data)

    def fetch_data(self):

        id = self.id_entry.text()
        if id.isdigit():
            response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{id}')

            if response.status_code == 200:
                data = response.json()
                self.output_text.clear()
                self.output_text.append(str(data))
                self.save_data(data)

            else:
                self.output_text.clear()
                self.output_text.append(f"Error: {response.status_code}")

        else:
            self.output_text.clear()
            self.output_text.append("ID must be a number")

    def save_data(self, data):

        id = data['id']
        filename = (f'post_{id}.json')

        with open(filename, 'w') as f:
            f.write(str(data))
        self.output_text.append(f"Data saved to {filename}")

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = JsonPlaceholderApp()
    window.show()
    sys.exit(app.exec())
