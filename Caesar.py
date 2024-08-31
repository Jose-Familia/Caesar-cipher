import argparse

parser = argparse.ArgumentParser(description="This decodes a file provided as parameter.")

parser.add_argument("filename", help="The file to decode")

args = parser.parse_args()

def decode_Caesar_cipher(s, n):
    alpha = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',.?!"
    s = s.strip()
    text = ''
    for c in s:
        text += alpha[(alpha.index(c) + n) % len(alpha)]
    # decoded text:
    print(text)

filename = args.filename
opened_file = open(filename)
encoded_text = opened_file.read()  # read the file into a string

decode_Caesar_cipher(encoded_text, -13)

opened_file.close()  # always close the files you've opened
