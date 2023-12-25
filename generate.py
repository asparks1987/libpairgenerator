import random
import datetime
import pytz
import csv
import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog

class PairGenerator:
    def __init__(self, num_inputs, num_pairs, num_outputs, int_values=False):
        self.num_inputs = num_inputs
        self.num_outputs = num_outputs
        self.num_pairs = num_pairs
        self.int_values = int_values
        self.gen = random.Random(42)

    def generate_pairs(self):
        if self.num_inputs < 1 or self.num_outputs < 1:
            raise ValueError("Number of inputs and outputs should be greater than 0.")
        
        return [
            (
                input_values := self._generate_input_values(),
                self._generate_timestamp(),
                self._calculate_xor(input_values)
            )
            for _ in range(self.num_pairs)
        ]

    def _generate_input_values(self):
        if self.int_values:
            return [self.gen.randint(-100, 100) / 100.0 for _ in range(self.num_inputs)]
        else:
            return [self.gen.uniform(-1, 1) for _ in range(self.num_inputs)]

    def _generate_timestamp(self):
        return (datetime.datetime.now(pytz.utc) - datetime.timedelta(hours=self.gen.uniform(1, 24))).isoformat()

    def _calculate_xor(self, input_values):
        xor_value = round(input_values[0])
        for val in input_values[1:]:
            xor_value ^= round(val)
        # Ensure that the output is within the range of -1 to 1
        return [max(-1, min(xor_value, 1))] * self.num_outputs

    def save_to_file(self, filename, append=False):
        pairs = self.generate_pairs()
        mode = 'a' if append else 'w'
        with open(filename, mode, newline='') as f:
            writer = csv.writer(f)
            if not append:
                header = ['timestamp'] + [f'input_{i}' for i in range(self.num_inputs)] + [f'output_{i}' for i in range(self.num_outputs)]
                writer.writerow(header)
            for input_values, timestamp, expected_output in pairs:
                row = [timestamp] + input_values + expected_output
                writer.writerow(row)

def get_user_input(root):
    num_inputs = simpledialog.askinteger("Number of Inputs", "Enter number of inputs", parent=root, minvalue=1)
    num_pairs = simpledialog.askinteger("Number of Pairs", "Enter number of pairs", parent=root, minvalue=1)
    num_outputs = simpledialog.askinteger("Number of Outputs", "Enter number of outputs", parent=root, minvalue=1)
    return num_inputs, num_pairs, num_outputs

def generate_floats():
    filename = filedialog.asksaveasfilename(defaultextension=".csv")
    num_inputs, num_pairs, num_outputs = get_user_input(root)
    if filename and num_inputs is not None and num_pairs is not None and num_outputs is not None:
        gen = PairGenerator(num_inputs, num_pairs, num_outputs)
        gen.save_to_file(filename)
        messagebox.showinfo("Success", "Float pairs generated and saved to file.")

def generate_ints():
    filename = filedialog.asksaveasfilename(defaultextension=".csv")
    num_inputs, num_pairs, num_outputs = get_user_input(root)
    if filename and num_inputs is not None and num_pairs is not None and num_outputs is not None:
        gen = PairGenerator(num_inputs, num_pairs, num_outputs, int_values=True)
        gen.save_to_file(filename)
        messagebox.showinfo("Success", "Int pairs generated and saved to file.")

if __name__ == "__main__":
    root = tk.Tk()
    tk.Button(root, text="Generate Floats", command=generate_floats).pack()
    tk.Button(root, text="Generate Ints", command=generate_ints).pack()
    root.mainloop()
