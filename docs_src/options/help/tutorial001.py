import cligenius


def main(
    name: str,
    lastname: str = cligenius.Option("", help="Last name of person to greet."),
    formal: bool = cligenius.Option(False, help="Say hi formally."),
):
    """
    Say hi to NAME, optionally with a --lastname.

    If --formal is used, say hi very formally.
    """
    if formal:
        print(f"Good day Ms. {name} {lastname}.")
    else:
        print(f"Hello {name} {lastname}")


if __name__ == "__main__":
    cligenius.run(main)
