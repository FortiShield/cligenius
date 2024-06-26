import cligenius
from typing_extensions import Annotated


def main(
    id: Annotated[int, cligenius.Argument(min=0, max=1000)],
    rank: Annotated[int, cligenius.Option(max=10, clamp=True)] = 0,
    score: Annotated[float, cligenius.Option(min=0, max=100, clamp=True)] = 0,
):
    print(f"ID is {id}")
    print(f"--rank is {rank}")
    print(f"--score is {score}")


if __name__ == "__main__":
    cligenius.run(main)
