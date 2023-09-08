import easyocr
import numpy as np
import matplotlib.pyplot as plt
import re
import itertools

IMAGE_PATH = "basic-projects\OCR\sign.png"
det = []
reader = easyocr.Reader(["en"],gpu=True)
result = reader.readtext(IMAGE_PATH)
print(result)
words = re.findall(r'\b[a-zA-Z]+\b', str(result))
print(words)
text = "The words found in the image are: "
for i in words:
    text = str(i) + " "
if len(words)!=0:
    print(text)
else:
    print("No text detected!")    