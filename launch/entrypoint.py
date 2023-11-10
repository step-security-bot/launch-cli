import click


@click.group(name="cli")
def cli():
    pass


from .cli.github import github_group

cli.add_command(github_group)
