import tkinter as tk
from tkinter import scrolledtext

def create_ui(root, process_input):
    input_text_prompts = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
    input_text_results = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
    output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20)

    input_text_prompts.pack(pady=10)
    input_text_results.pack(pady=10)
    output_text.pack(pady=10)

    process_button = tk.Button(root, text="Process", command=process_input)
    process_button.pack(pady=5)

    return input_text_prompts, input_text_results, output_text, process_button
