import requests
from colorama import Fore, Style
import json
import time

with open("urls.txt", "r") as f:
    urls = f.read().splitlines()

endpoint = "https://discord.com/api/v6/invite/"

invalid = []

for url in urls:
    res = requests.get(endpoint + url)
    if res.status_code == 200:
        data = json.loads(res.text)
        if data["guild"]["name"]:
            print(f"{Fore.GREEN}{url}{Style.RESET_ALL} - Valid URL")
        else:
            print(f"{Fore.YELLOW}{url}{Style.RESET_ALL} - Taken URL")
    elif res.status_code == 429:
        js = res.json()
        time.sleep(js['retry_after'])
        print("Rate Limited... Retrying after " + str(js['retry_after']) + " seconds")
    else:
        print(f"{Fore.RED}{url}{Style.RESET_ALL} - Invalid URL")
        invalid.append(url)


with open("invalid.txt", "w") as f:
    for url in invalid:
        f.write(url + "\n")
