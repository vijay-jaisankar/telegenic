import random
import requests

"""
    Generate URL using the deployed Beeceptor endpoint
"""
def get_image_url(type_param : int) -> str:
    url = f"https://telegenic.free.beeceptor.com/album/type{type_param}"
    return url

"""
    Get a prospective album cover URL
"""
def get_url_from_beeceptor() -> str:
    type_param = random.randint(1,2)
    url = get_image_url(type_param)
    r = requests.get(url)
    return (r.json()["status"])


if __name__ == "__main__":
    s = get_url_from_beeceptor()
    print(s)