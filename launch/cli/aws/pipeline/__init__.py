from time import sleep

import click
from click_spinner import spinner

# from .pipeline import pipeline_group


@click.group(name="pipeline")
def pipeline_group():
    """Command family for pipeline-related tasks."""


# aws_group.add_command(pipeline_group)


@pipeline_group.command()
def run_stage():
    """An example command that might be utilized by a pipeline."""

    click.echo("Performing some long-running task... ", nl=False)
    with spinner():
        sleep(5)
    click.secho("Pipeline command complete!", fg="green")
