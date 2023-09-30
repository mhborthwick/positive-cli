from enum import Enum
from typing_extensions import Annotated
import typer
from data import get_message


class YesOrNo(str, Enum):
    yes = "yes"
    no = "no"


def main(
        send_message: Annotated[YesOrNo, typer.Option(
            prompt="Do you want to receive a wholesome message?")]
):
    if (send_message == "yes"):
        message = get_message(1)
        print(message)


if __name__ == "__main__":
    typer.run(main)
