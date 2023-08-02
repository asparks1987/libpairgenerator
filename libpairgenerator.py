import random
import datetime
import pytz
import json
import os
import csv

class PairGenerator:
    def __init__(self, num_inputs, num_pairs):
        self.num_inputs = num_inputs
        self.num_pairs = num_pairs
        self.gen = random.Random(42)

    def generate_pairs(self):
        if self.num_inputs < 1:
            raise ValueError("Number of inputs should be greater than 0.")
        return [(input_values := self._generate_input_values(), self._generate_timestamp(), self._calculate_xor(input_values))
                for _ in range(self.num_pairs)]

    def _generate_input_values(self):
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
                # write the header
                writer.writerow(['input', 'timestamp', 'target'])
            for input_values, timestamp, expected_output in pairs:
                # convert list to a string
                input_values_str = ', '.join(map(str, input_values))
                writer.writerow([input_values_str, timestamp, expected_output])

    def load_from_file(self, filename):
        if not os.path.isfile(filename):
            raise FileNotFoundError(f"No such file: '{filename}'")
        with open(filename, 'r') as f:
            pairs = [self._parse_line(line) for line in f]
            return zip(*pairs) 

    def _parse_line(self, line):
        input_values, timestamp, expected_output = json.loads(line.strip())
        return input_values, datetime.datetime.fromisoformat(timestamp), expected_output
