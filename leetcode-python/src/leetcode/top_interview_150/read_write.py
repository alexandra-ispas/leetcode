import json
import random
import uuid


class Person(object):
    name: str
    age: int

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def to_json(self) -> str:
        return json.dumps(self.__dict__)


def write():
    persons = [
        Person(name=str(uuid.uuid1()), age=random.randint(0, 50)) for _ in range(10)
    ]
    # create a file
    file = "persons.txt"
    with open(file, "w") as f:
        for p in persons:
            f.write(p.to_json() + "\n")


def read():
    input_file = "persons.txt"
    with open(input_file, "r") as f:
        for line in f:
            print(line)
            print(Person(**dict(json.loads(line.strip()))))


def read_from_stdin():
    import sys

    while True:
        line = sys.stdin.readline().strip()
        if line == "#":
            break
        print(line)


def main():
    read()


if __name__ == "__main__":
    main()
