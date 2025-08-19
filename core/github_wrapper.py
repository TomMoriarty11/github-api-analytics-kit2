import requests
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("GITHUB_TOKEN")

class GitHubAPI:
    def __init__(self, token=TOKEN):
        self.base_url = "https://api.github.com"
        self.headers = {"Authorization": f"Bearer {token}"}

    def get_repo_commits(self, owner, repo, since=None):
        url = f"{self.base_url}/repos/{owner}/{repo}/commits"
        params = {"since": since} if since else {}
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()

    def get_contributors(self, owner, repo):
        url = f"{self.base_url}/repos/{owner}/{repo}/contributors"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
