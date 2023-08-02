import tkinter as tk
from tkinter import messagebox, filedialog, Text, Scrollbar
from libpairgenerator import PairGenerator  # Assuming the library is named libpairgenerator

def save_pairs():
    gen = PairGenerator(15, 20000)
    filename = filedialog.asksaveasfilename(defaultextension=".txt")
    if filename:  # If a filename is given (i.e., the dialog is not cancelled)
        gen.save_to_file(filename)
        messagebox.showinfo("Success", "Pairs generated and saved to file.")

def load_pairs():
    gen = PairGenerator(15, 20000)
    filename = filedialog.askopenfilename()
    if filename:  # If a filename is given
        try:
            inputs, timestamps, expected_outputs = gen.load_from_file(filename)
        except FileNotFoundError as e:
            messagebox.showerror("Error", str(e))
            return

        result = "\n".join(
            f"Pair {i + 1}:\n  Input: {input}\n  Expected output: {expected_output}"
            for i, (input, expected_output) in enumerate(zip(inputs, expected_outputs))
        )

        # Create a new window to display the loaded pairs
        top = tk.Toplevel(root)
        text = Text(top)
        text.insert('1.0', result)
        text.pack()
        scrollbar = Scrollbar(top, command=text.yview)
        scrollbar.pack(side='right', fill='y')
        text['yscrollcommand'] = scrollbar.set

if __name__ == "__main__":
    root = tk.Tk()
    tk.Button(root, text="Generate pairs", command=save_pairs).pack()
    tk.Button(root, text="Load pairs", command=load_pairs).pack()
    root.mainloop()
