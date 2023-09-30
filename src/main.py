import typer
from data import get_message


def main():
    message = get_message(0)
    print(message)


if __name__ == "__main__":
    typer.run(main)
