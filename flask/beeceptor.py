import random
import requests
"""
    Generate URL using the deployed Beeceptor endpoint
"""


def get_image_url(type_param: int) -> str:
  url = f"https://telegenic.free.beeceptor.com/album/type{type_param}"
  return url


"""
    Get a prospective album cover URL
"""

def get_url_from_beeceptor() -> str:
  try:
    type_param = random.randint(1, 2)
    url = get_image_url(type_param)
    r = requests.get(url)
    return (r.json()["status"])
  except Exception as e:
    print(f"Error while getting album cover link from Beeceptor: {e}")
    return "https://i.imgur.com/oA0yD7d.png"