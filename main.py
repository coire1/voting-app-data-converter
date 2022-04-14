"""Main script for the Catalyst Dashboard."""
import typer

from commands import challenges
from commands import proposals

app = typer.Typer()

app.add_typer(
    challenges.app,
    name="challenges",
    help="Convert challenge specific data."
)

app.add_typer(
    proposals.app,
    name="proposals",
    help="Convert proposals specific data."
)

if __name__ == "__main__":
    app()
