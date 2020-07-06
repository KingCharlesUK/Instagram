from colorama import Fore, Style, init
from instagram_private_api import Client, ClientError, ClientLoginError
import json
import os
from datetime import datetime
from time import sleep
import ctypes
import keyboard
import requests

init()

usrname = json.loads(open("config.json").read())['username']
password = json.loads(open("config.json").read())['password']

ctypes.windll.kernel32.SetConsoleTitleW("Instagram AIO V1.0 | by Papi - Loading...")


def logo():
    print(f"{Fore.LIGHTMAGENTA_EX}       .o.       ooooo   .oooooo.   ")
    print(f"{Fore.LIGHTMAGENTA_EX}      .888.      `888'  d8P'  `Y8b  ")
    print(f"{Fore.LIGHTMAGENTA_EX}     .8\"888.      888  888      888 ")
    print(f"{Fore.LIGHTMAGENTA_EX}    .8' `888.     888  888      888 ")
    print(f"{Fore.LIGHTMAGENTA_EX}   .88ooo8888.    888  888      888 ")
    print(f"{Fore.LIGHTMAGENTA_EX}  .8'     `888.   888  `88b    d88' ")
    print(f"{Fore.LIGHTMAGENTA_EX} o88o     o8888o o888o  `Y8bood8P'  \n")


def clear():
    os.system("cls")

def get_user_id(u):
    url = f"https://www.instagram.com/{u}/?__a=1"
    response = requests.get(url=url, headers={
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"})
    id = json.loads(response.text)['graphql']['user']['id']
    return id


def get_media_id(m):
    url = f"https://api.instagram.com/oembed/?url={m}"
    response = requests.get(url=url, headers={
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"})
    id = json.loads(response.text)['media_id']
    return id


def get_username(u):
    url = f"https://i.instagram.com/api/v1/users/{u}/info/"
    headers = {
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 105.0.0.11.118 (iPhone11,8; iOS 12_3_1; en_US; en-US; scale=2.00; 828x1792; 165586599)'
    }
    response = requests.get(url=url, headers=headers)
    user = json.loads(response.text)['user']['username']
    return user

if usrname == "username-here":
    print(f"{Fore.LIGHTRED_EX}[{Style.RESET_ALL}ERROR{Fore.LIGHTRED_EX}] Please change your username in config.json")
    print(
        f"{Style.RESET_ALL}> {Fore.LIGHTMAGENTA_EX}Press {Fore.LIGHTMAGENTA_EX}[{Style.RESET_ALL}ESC{Fore.LIGHTMAGENTA_EX}] to close this window{Style.RESET_ALL}...")
    while True:
        try:
            if keyboard.is_pressed('esc'):
                raise SystemExit
        except:
            raise SystemExit
elif password == "password-here":
    print(f"{Fore.LIGHTRED_EX}[{Style.RESET_ALL}ERROR{Fore.LIGHTRED_EX}] Please change your password in config.json")
    print(
        f"{Style.RESET_ALL}> {Fore.LIGHTMAGENTA_EX}Press {Fore.LIGHTMAGENTA_EX}[{Style.RESET_ALL}ESC{Fore.LIGHTMAGENTA_EX}] to close this window{Style.RESET_ALL}...")
    while True:
        try:
            if keyboard.is_pressed('esc'):
                raise SystemExit
        except:
            raise SystemExit
else:
    try:
        ctypes.windll.kernel32.SetConsoleTitleW("Instagram AIO V1.0 | by Papi - Loading...")
        clear()
        print(f"{Style.RESET_ALL}> {Fore.LIGHTMAGENTA_EX}Logging into {usrname}{Style.RESET_ALL}...")
        api = Client(usrname, password)
        print(f"{Style.RESET_ALL}> {Fore.LIGHTMAGENTA_EX}Successfully logged into {usrname}{Style.RESET_ALL}.")
        sleep(1)
        print(f"{Style.RESET_ALL}> {Fore.LIGHTMAGENTA_EX}Loading the main menu{Style.RESET_ALL}...")
        sleep(3)
    except ClientLoginError:
        print(f"\n{Fore.LIGHTRED_EX}[{Style.RESET_ALL}ERROR{Fore.LIGHTRED_EX}] Incorrect login information")
        print(
            f"{Style.RESET_ALL}> {Fore.LIGHTMAGENTA_EX}Press {Fore.LIGHTMAGENTA_EX}[{Style.RESET_ALL}ESC{Fore.LIGHTMAGENTA_EX}] to close this window{Style.RESET_ALL}...")
        while True:
            try:
                if keyboard.is_pressed('esc'):
                    raise SystemExit
            except:
                raise SystemExit


def mchoose():
    try:
        option = int(input(f"\n{Style.RESET_ALL}> {Fore.LIGHTMAGENTA_EX}Select an option{Style.RESET_ALL}: "))
        if option == 1:
            scrape()
        elif option == 2:
            followbot()
        elif option == 3:
            unfollowbot()
        elif option == 4:
            commentbot()
        else:
            print(f"\n{Fore.LIGHTRED_EX}[{Style.RESET_ALL}ERROR{Fore.LIGHTRED_EX}] Please choose a valid integer")
    except ValueError:
        print(f"\n{Fore.LIGHTRED_EX}[{Style.RESET_ALL}ERROR{Fore.LIGHTRED_EX}] Please enter an integer")
        mchoose()


def main():
    ctypes.windll.kernel32.SetConsoleTitleW("Instagram AIO V1.0 | by Papi - Type: None")
    clear()
    print(f"{Fore.LIGHTMAGENTA_EX} Logged in as{Style.RESET_ALL}: @{usrname}")
    logo()
    print(f"{Fore.LIGHTMAGENTA_EX} [{Style.RESET_ALL}1{Fore.LIGHTMAGENTA_EX}] Username Scraper")
    print(f"{Fore.LIGHTMAGENTA_EX} [{Style.RESET_ALL}2{Fore.LIGHTMAGENTA_EX}] Follow Bot")
    print(f"{Fore.LIGHTMAGENTA_EX} [{Style.RESET_ALL}3{Fore.LIGHTMAGENTA_EX}] Unfollow Bot")
    print(f"{Fore.LIGHTMAGENTA_EX} [{Style.RESET_ALL}4{Fore.LIGHTMAGENTA_EX}] Comment Bot")
    mchoose()


def scrape():
    ctypes.windll.kernel32.SetConsoleTitleW(
        "Instagram AIO V1.0 | by Papi - Type: Username Scraper")
    clear()
    print(f"{Fore.LIGHTMAGENTA_EX} Logged in as: {Style.RESET_ALL}@{usrname}")
    logo()
    hashtag = input(f"\n{Style.RESET_ALL}> {Fore.LIGHTMAGENTA_EX}Enter a hashtag to scrape{Style.RESET_ALL}: #")
    amount = int(input(f"{Style.RESET_ALL}> {Fore.LIGHTMAGENTA_EX}Amount of users to scrape{Style.RESET_ALL}: "))
    url = f"https://www.instagram.com/explore/tags/{hashtag}/?__a=1"
    response = requests.get(url, headers={
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"})
    j = json.loads(response.text)
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    print(
        f"\n{Fore.LIGHTGREEN_EX}[{Style.RESET_ALL}{time}{Fore.LIGHTGREEN_EX}] Starting to scrape users from {Style.RESET_ALL}#{hashtag}...\n")
    i = 0
    pos = 1
    for u in range(amount):
        id = j['graphql']['hashtag']['edge_hashtag_to_media']['edges'][i]['node']['owner']['id']
        uname = get_username(id)
        with open("scraped.txt", "a+") as f:
            f.write(f"{uname}\n")

        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        print(f"{Fore.LIGHTGREEN_EX}[{Style.RESET_ALL}{time}{Fore.LIGHTGREEN_EX}] Scraped User{Style.RESET_ALL}: {uname} {Fore.LIGHTGREEN_EX}({Style.RESET_ALL}#{pos}{Fore.LIGHTGREEN_EX})")
        sleep(2)

        pos += 1
        i += 1

    print(f"\n{Style.RESET_ALL}> {Fore.LIGHTGREEN_EX}Finished, and put scraped users into scraped.txt{Style.RESET_ALL}.")
    print(
        f"{Style.RESET_ALL}> {Fore.LIGHTMAGENTA_EX}Press {Fore.LIGHTMAGENTA_EX}[{Style.RESET_ALL}ESC{Fore.LIGHTMAGENTA_EX}] to return to the main menu{Style.RESET_ALL}...")
    while True:
        try:
            if keyboard.is_pressed('esc'):
                clear()
                main()
                break
        except:
            break


def follow():
    lines = 0
    with open("users.txt", "r+") as f:
        for line in f:
            lines += 1
    with open("users.txt", "r+") as fp:
        user = fp.readline()
        count = 0
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        print(
            f"\n{Fore.LIGHTGREEN_EX}[{Style.RESET_ALL}{time}{Fore.LIGHTGREEN_EX}] Starting to follow {Style.RESET_ALL}{lines} {Fore.LIGHTGREEN_EX}users from file{Style.RESET_ALL}...\n")
        while user:
            try:
                api.friendships_create(user_id=get_user_id(user.strip()))
                now = datetime.now()
                time = now.strftime("%H:%M:%S")
                count += 1
                print(
                    f"{Fore.LIGHTGREEN_EX}[{Style.RESET_ALL}{time}{Fore.LIGHTGREEN_EX}] Followed{Style.RESET_ALL}: @{user.strip()} {Fore.LIGHTGREEN_EX}({Style.RESET_ALL}#{count}{Fore.LIGHTGREEN_EX})")
                user = fp.readline()
                sleep(30)
            except ClientError:
                print(
                    f"{Fore.LIGHTRED_EX}[{Style.RESET_ALL}ERROR{Fore.LIGHTRED_EX}] Your account is currently rate limited{Style.RESET_ALL}. {Fore.LIGHTRED_EX}Try again later{Style.RESET_ALL}.")
                break

    print(f"\n{Style.RESET_ALL}> {Fore.LIGHTGREEN_EX}Finished{Style.RESET_ALL}.")
    print(
        f"{Style.RESET_ALL}> {Fore.LIGHTMAGENTA_EX}Press {Fore.LIGHTMAGENTA_EX}[{Style.RESET_ALL}ESC{Fore.LIGHTMAGENTA_EX}] to return to the main menu{Style.RESET_ALL}...")
    while True:
        try:
            if keyboard.is_pressed('esc'):
                clear()
                main()
                break
        except:
            break


def fbchoose():
    try:
        option = int(input(f"\n{Style.RESET_ALL}> {Fore.LIGHTMAGENTA_EX}Select an option{Style.RESET_ALL}: "))
        if option == 1:
            follow()
        else:
            print(f"\n{Fore.LIGHTRED_EX}[{Style.RESET_ALL}ERROR{Fore.LIGHTRED_EX}] Please choose a valid integer")
    except ValueError:
        print(f"\n{Fore.LIGHTRED_EX}[{Style.RESET_ALL}ERROR{Fore.LIGHTRED_EX}] Please enter an integer")
        fbchoose()


def followbot():
    ctypes.windll.kernel32.SetConsoleTitleW("Instagram AIO V1.0 | by Papi - Type: Follow Bot")
    clear()
    print(f"{Fore.LIGHTMAGENTA_EX} Logged in as: {Style.RESET_ALL}@{usrname}")
    logo()
    print(f"{Fore.LIGHTMAGENTA_EX} [{Style.RESET_ALL}1{Fore.LIGHTMAGENTA_EX}] From File")
    fbchoose()


def unfollow():
    lines = 0
    with open("users.txt", "r+") as f:
        for line in f:
            lines += 1
    if lines == 0:
        print(f"\n{Fore.LIGHTRED_EX}[{Style.RESET_ALL}ERROR{Fore.LIGHTRED_EX}] Please input usernames in users.txt")
        print(
        f"{Style.RESET_ALL}> {Fore.LIGHTMAGENTA_EX}Press {Fore.LIGHTMAGENTA_EX}[{Style.RESET_ALL}ESC{Fore.LIGHTMAGENTA_EX}] to return to the main menu{Style.RESET_ALL}...")
        while True:
            try:
                if keyboard.is_pressed('esc'):
                    clear()
                    main()
                    break
            except:
                break
    with open("users.txt", "r+") as fp:
        user = fp.readline()
        count = 0
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        print(
            f"\n{Fore.LIGHTGREEN_EX}[{Style.RESET_ALL}{time}{Fore.LIGHTGREEN_EX}] Starting to Unfollow {Style.RESET_ALL}{lines} {Fore.LIGHTGREEN_EX}users from file{Style.RESET_ALL}...\n")
        while user:
            try:
                api.friendships_destroy(user_id=get_user_id(user.strip()))
                now = datetime.now()
                time = now.strftime("%H:%M:%S")
                count += 1
                print(
                    f"{Fore.LIGHTGREEN_EX}[{Style.RESET_ALL}{time}{Fore.LIGHTGREEN_EX}] Unfollowed{Style.RESET_ALL}: @{user.strip()} {Fore.LIGHTGREEN_EX}({Style.RESET_ALL}#{count}{Fore.LIGHTGREEN_EX})")
                user = fp.readline()
                sleep(30)
            except ClientError:
                print(
                    f"{Fore.LIGHTRED_EX}[{Style.RESET_ALL}ERROR{Fore.LIGHTRED_EX}] Your account is currently rate limited{Style.RESET_ALL}. {Fore.LIGHTRED_EX}Try again later{Style.RESET_ALL}.")
                break

    print(f"\n{Style.RESET_ALL}> {Fore.LIGHTGREEN_EX}Finished{Style.RESET_ALL}.")
    print(
        f"{Style.RESET_ALL}> {Fore.LIGHTMAGENTA_EX}Press {Fore.LIGHTMAGENTA_EX}[{Style.RESET_ALL}ESC{Fore.LIGHTMAGENTA_EX}] to return to the main menu{Style.RESET_ALL}...")
    while True:
        try:
            if keyboard.is_pressed('esc'):
                clear()
                main()
                break
        except:
            break


def unfbchoose():
    try:
        option = int(input(f"\n{Style.RESET_ALL}> {Fore.LIGHTMAGENTA_EX}Select an option{Style.RESET_ALL}: "))
        if option == 1:
            unfollow()
        else:
            print(f"\n{Fore.LIGHTRED_EX}[{Style.RESET_ALL}ERROR{Fore.LIGHTRED_EX}] Please choose a valid integer")
    except ValueError:
        print(f"\n{Fore.LIGHTRED_EX}[{Style.RESET_ALL}ERROR{Fore.LIGHTRED_EX}] Please enter an integer")
        unfbchoose()


def unfollowbot():
    ctypes.windll.kernel32.SetConsoleTitleW("Instagram AIO V1.0 | by Papi - Type: Unfollow Bot")
    clear()
    print(f"{Fore.LIGHTMAGENTA_EX} Logged in as: {Style.RESET_ALL}@{usrname}")
    logo()
    print(f"{Fore.LIGHTMAGENTA_EX} [{Style.RESET_ALL}1{Fore.LIGHTMAGENTA_EX}] From File")
    unfbchoose()


def comment():
    comment = input(f"\n{Style.RESET_ALL}> {Fore.LIGHTMAGENTA_EX}Comment{Style.RESET_ALL}: ")
    lines = 0
    with open("posts.txt", "r+") as f:
        for line in f:
            lines += 1
    with open("posts.txt", "r+") as fp:
        post = fp.readline()
        count = 0
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        print(
            f"\n{Fore.LIGHTGREEN_EX}[{Style.RESET_ALL}{time}{Fore.LIGHTGREEN_EX}] Starting to comment on {Style.RESET_ALL}{lines} {Fore.LIGHTGREEN_EX}posts from file{Style.RESET_ALL}...\n")
        while post:
            try:
                api.post_comment(media_id=get_media_id(post.strip()), comment_text=comment)
                now = datetime.now()
                time = now.strftime("%H:%M:%S")
                count += 1
                print(
                    f"{Fore.LIGHTGREEN_EX}[{Style.RESET_ALL}{time}{Fore.LIGHTGREEN_EX}] Comment Sent ({post.strip()}){Style.RESET_ALL}: {comment} {Fore.LIGHTGREEN_EX}({Style.RESET_ALL}#{count}{Fore.LIGHTGREEN_EX})")
                post = fp.readline()
                sleep(30)
            except ClientError:
                print(
                    f"{Fore.LIGHTRED_EX}[{Style.RESET_ALL}ERROR{Fore.LIGHTRED_EX}] Your account is currently rate limited{Style.RESET_ALL}. {Fore.LIGHTRED_EX}Try again later{Style.RESET_ALL}.")
                break

    print(f"\n{Style.RESET_ALL}> {Fore.LIGHTGREEN_EX}Finished{Style.RESET_ALL}.")
    print(
        f"{Style.RESET_ALL}> {Fore.LIGHTMAGENTA_EX}Press {Fore.LIGHTMAGENTA_EX}[{Style.RESET_ALL}ESC{Fore.LIGHTMAGENTA_EX}] to return to the main menu{Style.RESET_ALL}...")
    while True:
        try:
            if keyboard.is_pressed('esc'):
                clear()
                main()
                break
        except:
            break


def comchoose():
    try:
        option = int(input(f"\n{Style.RESET_ALL}> {Fore.LIGHTMAGENTA_EX}Select an option{Style.RESET_ALL}: "))
        if option == 1:
            comment()
        else:
            print(f"\n{Fore.LIGHTRED_EX}[{Style.RESET_ALL}ERROR{Fore.LIGHTRED_EX}] Please choose a valid integer")
    except ValueError:
        print(f"\n{Fore.LIGHTRED_EX}[{Style.RESET_ALL}ERROR{Fore.LIGHTRED_EX}] Please enter an integer")
        comchoose()


def commentbot():
    ctypes.windll.kernel32.SetConsoleTitleW("Instagram AIO V1.0 | by Papi - Type: Comment Bot")
    clear()
    print(f"{Fore.LIGHTMAGENTA_EX} Logged in as: {Style.RESET_ALL}@{usrname}")
    logo()
    print(f"{Fore.LIGHTMAGENTA_EX} [{Style.RESET_ALL}1{Fore.LIGHTMAGENTA_EX}] From File")
    comchoose()


if __name__ == "__main__":
    main()
