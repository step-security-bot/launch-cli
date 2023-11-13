import click


@click.group(name="cli")
def cli():
    """Launch CLI tooling to help automate common tasks performed by Launch engineers and their clients."""
    pass


from .aws import aws_group
from .github import github_group

cli.add_command(github_group)
cli.add_command(aws_group)
