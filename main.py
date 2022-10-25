from urllib.request import Request, urlopen
"""

fetch a random dad joke.

was created inside the development branch
"""
def fetch_random_dad_joke() -> str:
    req = Request(
        url="https://icanhazdadjoke.com/",
        headers={
            "Accept": "text/plain",
            "User-Agent": "Workshop"
        }
    )
    return urlopen(req).read().decode("utf-8")

print(fetch_random_dad_joke())