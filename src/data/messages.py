import json
import os
import random

from dataclasses import dataclass
from typing import List


@dataclass
class MessageItem:
    message: str
    source: str


@dataclass
class MessageResponse:
    results: List[MessageItem]


def get_rand_index(len: int) -> int:
    return random.randint(0, len - 1)


def read_messages(file_path: str) -> MessageResponse:
    with open(file_path, "r") as file:
        messages = json.load(file)
    return messages


def get_random_message() -> str:
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "messages.json")
    messages = read_messages(file_path)
    index = get_rand_index(len(messages["results"]))
    return messages["results"][index]
