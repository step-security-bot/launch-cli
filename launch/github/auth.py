import os

from github import Auth, Github
from github.AuthenticatedUser import AuthenticatedUser

try:
    GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
except KeyError:
    print(
        "ERROR: The GITHUB_TOKEN environment variable is not set. You must set this environment variable with the contents of your GitHub Personal Access Token (PAT) to use this script."
    )
    exit(-1)

GITHUB_HEADERS = {"Authorization": f"Bearer {GITHUB_TOKEN}"}


def get_github_instance(token: str | None = None) -> Github:
    if not token:
        token = GITHUB_TOKEN
    auth = Auth.Token(token)
    return Github(auth=auth)
