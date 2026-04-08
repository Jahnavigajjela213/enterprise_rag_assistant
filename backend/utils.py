import os
import re


def clean_text(text):
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def check_data_folder(path="backend/data"):
    if not os.path.exists(path):
        raise Exception("Data folder missing")

    files = os.listdir(path)
    if not files:
        raise Exception("No PDF files found in data folder")
