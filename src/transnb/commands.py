import click

from transnb import messages


@click.command()
def tweet() -> None:
    """Entry point for sending a tweet."""
    click.echo(messages.get_random_message())


@click.command()
def all_messages() -> list:
    """all available messages"""
    for msg in messages.get_all_messages():
        click.echo(msg)
