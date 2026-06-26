import tkinter as tk
from tkinter import ttk
from deep_translator import GoogleTranslator

languages = {
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Japanese": "ja",
    "Chinese": "zh-CN",
    "Arabic": "ar",
    "Telugu": "te",
    "Malayalam": "ml",
    "Kannada": "kn"
}

def translate_text():
    text = input_text.get("1.0", tk.END).strip()
    src = languages[src_lang.get()]
    dest = languages[dest_lang.get()]
    translated = GoogleTranslator(source=src, target=dest).translate(text)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, translated)

# Window setup
window = tk.Tk()
window.title("Language Translation Tool")
window.geometry("600x450")
window.configure(bg="#f0f0f0")

lang_names = list(languages.keys())

tk.Label(window, text="Language Translation Tool",
font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)

tk.Label(window, text="Enter Text:", bg="#f0f0f0").pack()
input_text = tk.Text(window, height=5, width=60)
input_text.pack(pady=5)

tk.Label(window, text="Source Language:", bg="#f0f0f0").pack()
src_lang = ttk.Combobox(window, values=lang_names, width=20)
src_lang.set("English")
src_lang.pack()

tk.Label(window, text="Target Language:", bg="#f0f0f0").pack()
dest_lang = ttk.Combobox(window, values=lang_names, width=20)
dest_lang.set("Tamil")
dest_lang.pack()

tk.Button(window, text="Translate", command=translate_text,
bg="#4CAF50", fg="white", width=20).pack(pady=10)

tk.Label(window, text="Translated Text:", bg="#f0f0f0").pack()
output_text = tk.Text(window, height=5, width=60)
output_text.pack(pady=5)

window.mainloop()