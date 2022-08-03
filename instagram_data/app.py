from scraper import scrape
from instagrapi.exceptions import BadPassword, UnknownError, SentryBlock, ChallengeRequired


def app():
    finished = False
    while not finished:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        try:
            scrape(username, password)
            finished = True
        except UnknownError:
            print("Error unknown. Make sure your username is valid.")
        except BadPassword:
            print("Password does not match with that username. Try again.")
        except ChallengeRequired:
            print("Challenge required. Try logging into Instagram and adding a phone number, then try again.")
        except SentryBlock:
            print("Your IP associated with this account is most likely banned from Instagram. Try a different IP or account.")

