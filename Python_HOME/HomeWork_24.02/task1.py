import tkinter as tk
import requests
import os

def fetch_data():

    id = id_entry.get()
    if id.isdigit():
        response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{id}')

        if response.status_code == 200:
            data = response.json()
            output_text.delete(1.0, tk.END)
            output_text.insert(tk.END, data)
            save_data(data)

        else:
            output_text.delete(1.0, tk.END)
            output_text.insert(tk.END, f"Error: {response.status_code}")

    else:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "ID must be a number")

def save_data(data):

    id = data['id']
    filename = (f'post_{id}.json')

    with open(filename, 'w') as f:
        f.write(str(data))
    output_text.insert(tk.END, f"\nData saved to {filename}")

if __name__ == "__main__":

    root = tk.Tk()
    root.title("JSON Placeholder Viewer")

    id_label = tk.Label(root, text="Enter post ID:")
    id_label.grid(row=0, column=0, padx=5, pady=5)
    id_entry = tk.Entry(root)
    id_entry.grid(row=0, column=1, padx=5, pady=5)

    fetch_button = tk.Button(root, text="Fetch Data", command=fetch_data)
    fetch_button.grid(row=0, column=2, padx=5, pady=5)

    output_text = tk.Text(root, width=50, height=10)
    output_text.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

    root.mainloop()
