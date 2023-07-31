import random
import datetime
import pytz
import json
import os
import tkinter as tk
from tkinter import messagebox, filedialog, Text, Scrollbar

class PairGenerator:
    def __init__(self, num_inputs, num_pairs):
        """Initialize generator with a fixed seed for reproducibility."""
        self.num_inputs = num_inputs
        self.num_pairs = num_pairs
        self.gen = random.Random(42)

    def generate_pairs(self):
        """Generate pairs of input arrays and the XOR of their rounded values."""
        return [(input_values := self._generate_input_values(), self._generate_timestamp(), self._calculate_xor(input_values))
                for _ in range(self.num_pairs)]

    def _generate_input_values(self):
        """Generate a list of random floating point numbers between -1 and 1."""
        return [self.gen.uniform(-1, 1) for _ in range(self.num_inputs)]

    def _generate_timestamp(self):
        """Generate a timestamp string for the current pair."""
        return (datetime.datetime.now(pytz.utc) - datetime.timedelta(hours=self.gen.uniform(1, 24))).isoformat()

    def _calculate_xor(self, input_values):
        """Calculate the XOR of the rounded values of an input array."""
        xor_value = round(input_values[0])
        for val in input_values[1:]:
            xor_value ^= round(val)
        return xor_value

    def save_to_file(self, filename):
        """Save generated pairs to a file."""
        pairs = self.generate_pairs()
        with open(filename, 'w') as f:
            for pair in pairs:
                json.dump(pair, f)
                f.write("\n")

    def load_from_file(self, filename):
        """Load pairs from a file."""
        if not os.path.isfile(filename):
            raise FileNotFoundError(f"No such file: '{filename}'")

        with open(filename, 'r') as f:
            pairs = [self._parse_line(line) for line in f]
            return zip(*pairs)  # Unzips into three separate lists

    def _parse_line(self, line):
        """Parse a line from a file into a pair."""
        input_values, timestamp, expected_output = json.loads(line.strip())
        return input_values, datetime.datetime.fromisoformat(timestamp), expected_output

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
