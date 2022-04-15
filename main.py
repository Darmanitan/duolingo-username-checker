import requests
import threading
import random

usernameList = []
s = open("names.txt", "r").read().splitlines()
for i in s:
    if i =="":
        continue
    usernameList.append(i)
available = open('available.txt', 'w')

# change it to your own duolingo cookie. method can be found in README.md
headers = {
    "Cookie": "this is my duoliungo cookie , nos teal pls"
}
def check():
    x = str(random.choice(usernameList))
    r = requests.get(f"https://www.duolingo.com/users/{x}", headers=headers)

    if r.status_code == 200:
        print(f"[{r.status_code}] {x} is taken")
    else:
        print(f"[{r.status_code}] {x} is avaiable");available.write(f"{x}\n")

threads = []
while True: 
    for i in range(200):
        t = threading.Thread(target=check)
        t.start()
        threads.append(t)


    for i in threads:
        i.join()
