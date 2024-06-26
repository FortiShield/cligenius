import cligenius

app = cligenius.Cligenius()


@app.command()
def create():
    print("Creating user: Hiro Hamada")


@app.callback()
def callback():
    """
    Creates a single user Hiro Hamada.

    In the next version it will create 5 users more.
    """


if __name__ == "__main__":
    app()
