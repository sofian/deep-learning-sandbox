# coding=utf-8
import argparse

parser = argparse.ArgumentParser(description="Preprocesses text files to make them easier to train")
parser.add_argument("text_file", type=str, help="The file containing the original text")
parser.add_argument("output_file", type=str, help="The output file")

args = parser.parse_args()

import re

# Load file.
raw_text = open(args.text_file).read()

# Replace * * * * * style separators.
raw_text = raw_text.replace("*", "")

# Replace line breaks with spaces and 2+line breaks with newlines.
raw_text = re.sub(r'\r\n', '\n', raw_text)
raw_text = re.sub(r' *\n', '\n', raw_text)
raw_text = re.sub(r'\n\n+', '\r', raw_text)
raw_text = raw_text.replace("\n", " ")
raw_text = raw_text.replace("\r", "\n")

# Fix multiple white spaces problems.
raw_text = re.sub(r'\n +', '\n', raw_text)
raw_text = re.sub(r' +', ' ', raw_text)

# Replace special characters.
raw_text = raw_text.replace("--", "—")
raw_text = raw_text.replace("_", "")
raw_text = raw_text.replace("*", "")

# Write to output.
output_file = open(args.output_file, "w+")
output_file.write(raw_text)

# load ascii text and covert to lowercase
raw_text = raw_text.lower()

# create mapping of unique chars to integers
chars = sorted(list(set(raw_text)))
print chars
