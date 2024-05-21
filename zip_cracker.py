import logging
import zipfile
from tqdm import tqdm

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="[%H:%M:%S]",
)


wordlist = "rockyou.txt"
zip_file = ""

zip_file = zipfile.ZipFile(zip_file)
n_words = len(list(open(wordlist, "rb")))
logging.info(f"Total passwords to test: {n_words}")

with open(wordlist, "rb") as wordlist:
    for word in tqdm(wordlist, total=n_words, unit="word"):
        try:
            zip_file.extractall(pwd=word.strip())
        except:
            continue
        else:
            logging.info(f"Password found: {word.decode().strip()}")
            exit(0)
print("[!] Password not found, try other wordlist.")
