import typer
from data import get_random_message


def main():
    send_message = typer.confirm("Do you want to receive a wholesome message")
    if send_message == False:
        print("Ok, no wholesome message for you. Bye!")
        raise typer.Exit()
    else:
        while True:
            message = get_random_message()
            print(message)

            another_message = typer.confirm(
                "Do you want to receive another wholesome message?")
            if another_message == False:
                print("Ok, have a great day!")
                raise typer.Exit()


if __name__ == "__main__":
    typer.run(main)
