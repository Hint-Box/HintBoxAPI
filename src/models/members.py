import requests

response = requests.get('https://api.github.com/orgs/Hint-Box/members')
members = []

for member in response.json():
    getting_members = {
        "id": member["id"],
        "login": member["login"],
        "avatar": member["avatar_url"],
        "url": member["html_url"],
        "repos": member["repos_url"]
    }
    members.append(getting_members)
