from github import Github
from github.AuthenticatedUser import AuthenticatedUser
from github.Repository import Repository


def get_github_repos(
    g: Github, user: AuthenticatedUser | None = None
) -> list[Repository]:
    if user:
        return user.get_repos()
    return [repo for repo in g.get_user().get_repos()]
