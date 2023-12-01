import click

from .access import access_group
from .hooks import hooks_group
from .version import version_group


@click.group(name="github")
def github_group():
    """Command family for GitHub-related tasks."""


github_group.add_command(access_group)
github_group.add_command(hooks_group)
github_group.add_command(version_group)
