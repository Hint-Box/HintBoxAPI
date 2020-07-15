import requests

response = requests.get('https://api.github.com/orgs/Hint-Box/repos')

projects = [pro for pro in response.json()]

hint_projects = [{
    "id": projects[0]["id"],
    "name": projects[0]["name"],
    "url": projects[0]["url"],
    "githubURL": projects[0]["html_url"],
    "created_at": projects[0]["created_at"],
    "description": projects[0]["description"],
    "tags": requests.get('https://api.github.com/repos/Hint-Box/HintBoxAPI/tags').json(),
    "contributors": requests.get('https://api.github.com/repos/Hint-Box/HintBoxAPI/contributors').json()
}]
