import random


def get_rand_index(len: int) -> int:
    return random.randint(0, len - 1)


def get_random_message() -> str:
    messages = [
        "hello there",
        "whats up",
        "how're you doing",
    ]
    index = get_rand_index(len(messages))
    return messages[index]
