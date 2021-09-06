import typer

app = typer.Typer()

@app.command()
def download():
    print("Xpandretail")

@app.command()
def upload():
    print("Safr")

@app.command()
def display():
    print("Xpandretail")

if __name__ == "__main__":
    app()