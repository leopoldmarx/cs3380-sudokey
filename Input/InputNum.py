from abc import ABC, abstractmethod


class InputNum(ABC):

    @abstractmethod
    def click(self):
        pass