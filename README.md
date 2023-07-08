PairGenerator Library
The PairGenerator library provides a simple yet powerful tool to generate pairs of random floating-point arrays and the XOR of their rounded values. Additionally, each pair comes with a timestamp. The library also includes capabilities to save and load the generated pairs to and from a JSON file.

Requirements
Python 3.6 or higher
pytz library
Installation
To use the PairGenerator library, you need to have Python installed on your computer. If you don't have Python installed, you can download it from the official website: https://www.python.org/downloads/

The PairGenerator library requires the pytz library for generating timestamps. You can install it using pip:
pip install pytz

Usage
Import the PairGenerator class from the pairgenerator.py file:

from pairgenerator import PairGenerator

Create an instance of the PairGenerator class:

gen = PairGenerator(15, 20000)  # Generates 20000 pairs of 15-element arrays

Generate the pairs:

pairs = gen.generate_pairs()
Save the pairs to a file:

gen.save_to_file("test.txt")
Load the pairs from a file:

try:
    inputs, timestamps, expected_outputs = gen.load_from_file("test.txt")
except FileNotFoundError as e:
    print(e)
Features
Generates pairs of random floating-point arrays and the XOR of their rounded values.
Generates a timestamp for each pair.
Ability to save the generated pairs to a file.
Ability to load the pairs from a file.
Contributing
We welcome any contributions to the PairGenerator library. If you want to contribute, please fork this repository, make your changes, and open a pull request.

License
The PairGenerator library is released under the MIT license.

