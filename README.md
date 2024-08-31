# Caesar-cipher

El cifrado César es un método de encriptación simple donde cada letra de un texto se desplaza un número fijo de posiciones en el alfabeto. En el código que compartiste, se implementa una función para decodificar un texto cifrado utilizando un desplazamiento de -13. Esto significa que cada carácter en el texto cifrado se "mueve" 13 posiciones hacia atrás en el alfabeto definido, devolviendo el texto original.

## Code 

```Python
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
```

## encrypted message

>[!NOTE]
Qrn!Mfur!y,pxIMvsMF,BH!rM!rnqv'tMAuv IMAur'JJJMVHzMCr!FIMCr!FMqv n..,v'ArqJMQvqMF,BM!rnyyFMAuv'xMVMD,ByqMB rMAurMPrn r!Mpv.ur!MA,Mr'p,qrMzFMrCvyM.yn'KMc,,!MAuv'tLMjur'MqvqMF,BM A,.MB v'tMF,B!Mo!nv'KMOr AMDv ur IMZ,!vn!AF


## decrypted message (Output)

>[!NOTE]
Dear Sherlock, if you're reading this, then... I'm very, very disappointed. Did you really think I would use the Ceaser cipher to encode my evil plan? Poor thing! When did you stop using your brain? Best wishes, Moriarty
---
>[!TIP]
Use Python Caesar.py 13.txt 
to run the script
