import click

from .pipeline import pipeline_group


@click.group(name="aws")
def aws_group():
    """Command family for AWS-related tasks."""


aws_group.add_command(pipeline_group)
