class Project:
    def __init__(self, id, name, url, githubURL, created_at, description="", tags=""):
        self.id = id
        self.name = name
        self.description = description
        self.tags = tags
        self.url = url
        self.githubURL = githubURL
        self.created_at = created_at

    def __str__(self):
        data = {}
        data["id"] = self.id
        data["name"] = self.name
        data["description"] = self.description
        data["tags"] = self.tags
        data["url"] = self.url
        data["githubURL"] = self.githubURL
        data["created_at"] = self.created_at
        return str(data)
