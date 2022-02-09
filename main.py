from server import Client
from os import environ


def config() -> str:
    return environ.get("TOKEN")


def run(token: str) -> None:
    client = Client()
    client.run(token)


if __name__ == "__main__":
    run(config())
