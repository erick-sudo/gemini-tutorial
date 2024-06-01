import pathlib
import textwrap
import os

import google.generativeai as genai

import PIL.Image

from IPython.display import display, Markdown

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# for m in genai.list_models():
#     print(m.name)

model = genai.GenerativeModel('gemini-1.5-flash')


# --------------- Streaming Content ----------------------
# response = model.generate_content("What is the meaning of life?", stream=True)

# for chunk in response:
#     print(chunk.text)
#     print("_"*80)

# print(to_markdown(response.text))


# --------------------- Images ----------------------------
# img = PIL.Image.open('image.jpg')

# response = model.generate_content(["Write a short, engaging blog post based on this picture. It should include a description of the meal in the photo and talk about my journey meal prepping.",img], stream=True)

# for chunk in response:
#     print(chunk.text)
#     print("_"*80)


# ----------------- Chat Conversations ---------------------
chat = model.start_chat(history=[])
response = chat.send_message("Hello", stream=True)

for chunk in response:
    print(chunk.text)
    print("_"*80)