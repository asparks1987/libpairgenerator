import random
import datetime
import pytz
import csv
import os

class PairGenerator:
    def __init__(self, num_inputs, num_pairs, int_values=False):
        self.num_inputs = num_inputs
        self.num_pairs = num_pairs
        self.int_values = int_values
        self.gen = random.Random(42)

    def generate_pairs(self):
        if self.num_inputs < 1:
            raise ValueError("Number of inputs should be greater than 0.")
        return [(input_values := self._generate_input_values(), self._generate_timestamp(), self._calculate_xor(input_values))
                for _ in range(self.num_pairs)]

    def _generate_input_values(self):
        if self.int_values:
            return [self.gen.randint(-1, 1) for _ in range(self.num_inputs)]
        else:
            return [self.gen.uniform(-1, 1) for _ in range(self.num_inputs)]

    def _generate_timestamp(self):
        return (datetime.datetime.now(pytz.utc) - datetime.timedelta(hours=self.gen.uniform(1, 24))).isoformat()

    def _calculate_xor(self, input_values):
        xor_value = round(input_values[0])
        for val in input_values[1:]:
            xor_value ^= round(val)
        return xor_value

    def save_to_file(self, filename, append=False):
        pairs = self.generate_pairs()
        mode = 'a' if append else 'w'
        with open(filename, mode, newline='') as f:
            writer = csv.writer(f)
            if not append:
                writer.writerow(['input', 'timestamp', 'target'])
            for input_values, timestamp, expected_output in pairs:
                input_values_str = ', '.join(map(str, input_values))
                writer.writerow([input_values_str, timestamp, expected_output])
