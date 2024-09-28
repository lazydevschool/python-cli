import click
from pycli import main


@click.group()
def cli():
    pass


@cli.command()
@click.option("--name", "-n", required=True, help="Name to greet")
def greeting(name):
    """A greeting for you, but your name is required."""
    main.greeting(name)
