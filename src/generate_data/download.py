import os
import requests
import zipfile

def get_data():
    url = "http://files.grouplens.org/datasets/movielens/ml-100k.zip"

    raw_dir = "data/raw"
    os.makedirs(raw_dir, exist_ok=True)

    zip_path = os.path.join(raw_dir, "ml-100k.zip")

    with requests.get(url, stream=True) as r:
        r.raise_for_status()              # raises if HTTP error
        with open(zip_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(raw_dir)

    print(f"Downloaded and extracted to {raw_dir}")

# if __name__ == "__main__":
#     get_data()

