from gtts import gTTS
from tkinter import *
from tkinter import filedialog, messagebox
import os

# Main window setup
root = Tk()
root.title("Text to Speech")
root.geometry("500x300")

# Function: Convert user input to speech
def text_to_speech():
    """Converts text from the input field to audio."""
    text = entry.get()
    if text.strip() == "":
        messagebox.showwarning("Input Required", "Please type something first.")
        return
    output = gTTS(text=text, lang='en', slow=False)
    output.save("output.mp3")
    os.system("start output.mp3")

# Function: Read text from file and convert to audio
def file_to_speech():
    """Opens a text file, reads content, and converts it to audio."""
    filepath = filedialog.askopenfilename(
        title="Select Text File", 
        filetypes=[("Text Files", "*.txt")]
    )
    if filepath:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            if content.strip() == "":
                messagebox.showwarning("Empty File", "The selected file is empty.")
                return
            output = gTTS(text=content, lang='en', slow=False)
            output.save("output.mp3")
            os.system("start output.mp3")

# Function: Exit the app
def close_app():
    """Closes the application window."""
    root.destroy()

# UI elements
Label(root, text="Enter text below to convert to speech:", font=("Arial", 12)).pack(pady=10)

entry = Entry(root, width=60)
entry.pack(pady=5)

Button(root, text="Convert Typed Text", command=text_to_speech, width=25).pack(pady=10)
Button(root, text="Convert File Text", command=file_to_speech, width=25).pack(pady=5)
Button(root, text="Exit", command=close_app, width=25).pack(pady=10)

# Start the app
root.mainloop()
