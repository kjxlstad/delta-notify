import requests
from bs4 import BeautifulSoup


class Archive:
    def __init__(self) -> None:
        self.tickets = set()

    @staticmethod
    def fetch(url: str, selector: str) -> int:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        return hash(soup.select(selector)[0])

    def add(self, url: str, selector: str, author: int) -> None:
        content = self.fetch(url, selector)
        self.tickets |= {(url, selector, author, content)}

    def update(self) -> set[tuple[str, str, str, int]]:
        changed = {
            (url, locator, author, content)
            for url, locator, author, content in self.tickets
            if content != self.fetch(url, locator)
        }

        self.tickets -= changed

        return changed
