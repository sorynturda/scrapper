# main.py

from fastapi import FastAPI
from dtos import PathDTO
from scrap.scraper import get_info
from scrap.encryption import encrypt_data, decrypt_data

app = FastAPI()


@app.post("/read/")
def read_root(pathDTO: PathDTO):
    path = pathDTO.path.replace(' ','_')
    text = ''
    try:
        text = decrypt_data(path)
    except FileNotFoundError as e:
        try:
            with open("wiki/" + path + ".txt", "r") as f:
                text = f.read()
        except Exception as e:
            return {"text": str(e)}
    return {"text": text}


@app.post("/link/")
def post_link(pathDTO: PathDTO):
    try:
        path = pathDTO.path.replace(' ','_')
        html_text, date = get_info(path)
        if date % 2 == 0:
            encrypt_data(html_text, path)
        else:
            with open("wiki/" + pathDTO.path + ".txt", "w") as f:
                f.write(html_text)
        return {"res": True}
    except Exception as e:
        return {"res": str(e)}
