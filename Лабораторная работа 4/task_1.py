# TODO решите задачу
import json

FILE = "input.json"


def task() -> float:
    multiplication_sum = 0
    with open(FILE) as f:
        data = json.load(f)
        for dict in data:
            multiplication_sum += dict["score"] * dict["weight"]
    return round(multiplication_sum, 3)


print(task())