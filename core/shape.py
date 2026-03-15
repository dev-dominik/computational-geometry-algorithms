from __future__ import annotations

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def get_points(self):
        pass