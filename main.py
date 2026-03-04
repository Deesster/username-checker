import requests
PLATFORMS={
   "GitHub": "https://github.com/{}",
    "Instagram": "https://www.instagram.com/{}/",
    "Reddit": "https://www.reddit.com/user/{}",
    "Twitter": "https://twitter.com/{}"
}
def check_username(username):
  print(f"\n Checking username: {username}\n")
  for platform, url in PLATFORMS.items():
    full_url=url.format(username)
    try:
      response=requests.get(full_url)
      if response.status_code==200:
        print(f"{platform}: Found")
      else:
        print(f"{platform}: Not Found")
    except requests.exceptions.RequestException:
            print(f"{platform}: Error")

if __name__ == "__main__":
    username = input("Enter username: ")
    check_username(username)
      
      
      
