import requests

response = requests.get("https://api.github.com/orgs/Hint-Box/repos")
projects = []

for project in response.json():
    getting_projects = {
        "id": project["id"],
        "name": project["name"],
        "description": project["description"],
        "url": project["url"],
        "githubURL": project["html_url"],
        "created_at": project["created_at"],
        "tags": requests.get(
            "https://api.github.com/repos/Hint-Box/HintBoxAPI/tags"
        ).json(),
        "contributors": requests.get(
            "https://api.github.com/repos/Hint-Box/HintBoxAPI/contributors"
        ).json(),
    }
    projects.append(getting_projects)
