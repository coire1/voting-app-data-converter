import typer
from markdownify import markdownify as md
import json

app = typer.Typer()

@app.command()
def convert(
    input_file: str = typer.Option("", help="JSON file with proposals and HTML fields."),
    output_file: str = typer.Option("", help="Path to export.")
):
    """
    Convert proposals.
    """

    tags_to_strip = ['a', 'b', 'img', 'strong', 'u', 'i', 'embed', 'iframe']

    with open(input_file, encoding="utf-8") as file:
        proposals = json.load(file)

    md_proposals = []

    for proposal in proposals:
        proposal['proposal_solution'] = md(proposal['proposal_solution'], strip=tags_to_strip)
        proposal['proposal_summary'] = md(proposal['proposal_summary'], strip=tags_to_strip)
        proposal['proposer_relevant_experience'] = md(proposal['proposer_relevant_experience'], strip=tags_to_strip)
        md_proposals.append(proposal)

    with open(output_file, 'w', encoding="utf-8") as file:
        file.write(json.dumps(md_proposals, indent=2))
