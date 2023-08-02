import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog
from libpairgenerator import PairGenerator  # Assuming the library is named libpairgenerator

def get_user_input(root):
    num_inputs = simpledialog.askinteger("Number of Inputs", "Enter number of inputs", parent=root, minvalue=1)
    num_pairs = simpledialog.askinteger("Number of Pairs", "Enter number of pairs", parent=root, minvalue=1)
    return num_inputs, num_pairs

def generate_floats():
    filename = filedialog.asksaveasfilename(defaultextension=".txt")
    num_inputs, num_pairs = get_user_input(root)
    if filename and num_inputs is not None and num_pairs is not None:
        gen = PairGenerator(num_inputs, num_pairs)
        gen.save_to_file(filename)
        messagebox.showinfo("Success", "Float pairs generated and saved to file.")

def generate_ints():
    filename = filedialog.asksaveasfilename(defaultextension=".txt")
    num_inputs, num_pairs = get_user_input(root)
    if filename and num_inputs is not None and num_pairs is not None:
        gen = PairGenerator(num_inputs, num_pairs, int_values=True)
        gen.save_to_file(filename)
        messagebox.showinfo("Success", "Int pairs generated and saved to file.")

if __name__ == "__main__":
    root = tk.Tk()
    tk.Button(root, text="Generate Floats", command=generate_floats).pack()
    tk.Button(root, text="Generate Ints", command=generate_ints).pack()
    root.mainloop()
