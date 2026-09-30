from abc import ABC, abstractmethod
from item import JunkItem

class JunkRepository(ABC):
    @abstractmethod
    def save(self, items: list[JunkItem]) -> None:
        pass
    @abstractmethod
    def load(self) -> list[JunkItem] | None:
        pass
