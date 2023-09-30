from enum import Enum
from typing_extensions import Annotated
import typer
from data import get_random_message


class YesOrNo(str, Enum):
    yes = "y"  # update to "yes"
    no = "n"  # update to "no"


def main(
        send_message: Annotated[YesOrNo, typer.Option(
            prompt="Do you want to receive a wholesome message?")]
):
    if (send_message == "n"):
        print("Ok, no wholesome message for you. Bye!")
        raise typer.Exit()
    else:
        message = get_random_message()
        print(message)


if __name__ == "__main__":
    typer.run(main)
