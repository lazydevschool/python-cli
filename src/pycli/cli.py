import click
from pycli import main


@click.group()
def cli():
    pass


@cli.command()
@click.option("--name", "-n", default="World", help="Name to greet")
def greeting(name):
    main.greeting(name)
