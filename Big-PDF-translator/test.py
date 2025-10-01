import pypdf
import os
import time
import tqdm

import google.generativeai as genai

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

model = genai.GenerativeModel('gemini-1.0-pro')

reader = pypdf.PdfReader("./pdfs/Titan-All.pdf")

pbar = tqdm.tqdm(reader.pages)
pbar.update()