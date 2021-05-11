import click

from . import __version__

@click.command()
@click.version_option(version=__version__)
def main():
    """The Hypermodern Python project"""
    click.echo("Hello, world!")