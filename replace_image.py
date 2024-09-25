from re import sub
from requests import get

DOG_API_URL = "https://dog.ceo/api/breeds/image/random"

def main():
    # Get the image url:
    response = get(DOG_API_URL)
    dog_url = dict(response.json()).get("message")
    with open("README.md", "r+") as file:
        content = file.read()
        new = sub(
            r"(?P<before>!\[Dog image\]\()[\w:/\._-]*(?P<after>\))",
            r"\g<before>" + dog_url + r"\g<after>",
            content
        )

        file.seek(0)
        file.write(new)
        file.truncate()

if __name__ == "__main__":
    main()