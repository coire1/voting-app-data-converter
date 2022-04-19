import typer
from markdownify import markdownify as md
import json

app = typer.Typer()

@app.command()
def convert(
    input_file: str = typer.Option("", help="JSON file with challenges and HTML fields."),
    output_file: str = typer.Option("", help="Path to export."),
):
    """
    Convert challenges.
    """

    tags_to_strip = ['a', 'b', 'img', 'strong', 'u', 'i', 'embed', 'iframe']

    with open(input_file, encoding="utf-8") as file:
        challenges = json.load(file)

    md_challenges = []
    for challenge in challenges:
        challenge['description'] = md(challenge['description'], strip=tags_to_strip)
        md_challenges.append(challenge)

    with open(output_file, 'w', encoding="utf-8") as file:
        file.write(json.dumps(md_challenges, indent=2))
