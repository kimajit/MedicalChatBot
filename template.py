import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "research/trials.ipynb",
    "app.py",
    "store_index.py",
    "static/style.css",
    "templates/chat.html"

]


for file_path in list_of_files:
    filePath =Path(file_path)
    filedir, filename = os.path.split(filePath)
    if filedir !="":
      os.makedirs(filedir, exist_ok=True)
      logging.info(f"Creating directory; {filedir} for the file {filename}")
    if (not os.path.exists(filePath))or (os.path.getsize(filePath) == 0):
       with open(filePath, 'w') as f:
         pass
         logging.info(f"Creating empty file: {filePath}")

    else:
      logging.info(f"{filename} is already created")
       


