import typer


app = typer.Typer(add_completion=False)


@app.callback()
def callback():
    """
    coMMAND LINE llm
    """


@app.command()
def shoot():
    """
    Shoot the portal gun
    """
    typer.echo("Shooting portal gun")


@app.command()
def load():
    """
    Load the portal gun
    """
    typer.echo("Loading portal gun")
