import json
import urllib.request


def get_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:

        req = urllib.request.Request(url, headers=headers)


        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            print(data["value"])

    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    get_chuck_norris_joke()