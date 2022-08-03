from bs4 import BeautifulSoup
import requests
import re
from instagrapi import Client
from PIL import Image
import os


def scrape(username, password):
    # Grabs top 200 Instagram influencers from this website
    url = "https://viralpitch.co/topinfluencers/instagram/top-200-instagram-influencers/"

    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")

    # Grabs usernames
    names = doc.find_all("a", href=re.compile("viralpitch.co/instagram"))

    # Instagram login
    cl = Client()
    cl.login(username, password)

    with open('data.txt', 'w') as f:
        index = 0
        f.write("[\n")
        for i in names:
            if i.string != "Free Report" and i.string != "Instagram Influencer Marketing":
                print(f"Processing index: {index}/199")

                # Website has username typo
                if i.string == "simoneses":
                    user = cl.user_info_by_username("simonemendes")
                else:
                    user = cl.user_info_by_username(i.string)

                followers = user.follower_count

                # Grabs and saves profile pictures
                imageUrl = user.profile_pic_url_hd
                img = Image.open(requests.get(imageUrl, stream=True).raw)
                destination = os.path.join(os.path.dirname(__file__), f"img/{i.string}.jpg")
                img.save(destination)

                # For JS syntax
                f.write("{")
                f.write(f"'name': \"{i.string}\",\n'followers': {followers}")
                if index != 199:
                    f.write("},\n")
                elif index == 199:
                    f.write("}\n")
                index += 1
        f.write("]")
        f.close()

    print("Done")

