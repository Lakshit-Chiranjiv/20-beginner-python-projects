import pywhatkit as pwk

# Text to Handwriting
def text_to_handwriting(text):
    pwk.text_to_handwriting(text, "blueFile.png", rgb=(0, 0, 255))

# Text to Handwriting in green color
def text_to_handwriting_green(text):
    pwk.text_to_handwriting(text, "greenFile.png", rgb=(0, 255, 0))

text = """
    Hello, I am a Python Developer.
    I am learning Python.
    I am learning Pywhatkit.
    I am learning Text to Handwriting.
    My Name is Lakshit.
    I am 21 years old.
"""

text_to_handwriting(text)
text_to_handwriting_green(text)

print("Done")