import types


def main(name: str = types.Argument()):
    print(f"Hello {name}")


if __name__ == "__main__":
    types.run(main)