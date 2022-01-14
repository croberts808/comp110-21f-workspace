"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730439833"


class Simpy:
    values: list[float]

    # TODO: Your constructor and methods will go here.
    def __init__(self, values: list[float] = []):
        """Constructor."""
        self.values = values

    def __str__(self) -> str:
        return f"Simpy({self.values})"

    def fill(self, x: float, y: int):
        new: list[float] = []
        i: int = 0
        while i < y:
            new.append(x)
            i += 1
        self.values = new

    def arange(self, start: float, stop: float, step: float = 1.0):
        new: list[float] = []
        assert step != 0.0
        if step > 0.0:
            while start < stop:
                new.append(start)
                start += step
        elif step < 0.0:
            while start > stop:
                new.append(start)
                start += step
        self.values = new

    def sum(self) -> float:
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Add."""
        xs: list[float] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                xs.append(self.values[i] + rhs.values[i])
        else:
            for item in self.values:
                xs.append(item + rhs)
        return Simpy(xs)

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Pow."""
        xs: list[float] = []
        if isinstance(rhs, Simpy):    
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                xs.append(self.values[i] ** rhs.values[i])
        else:
            for item in self.values:
                xs.append(item ** rhs)
        return Simpy(xs)

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        xs: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                xs.append(self.values[i] == rhs.values[i])
        else:
            for item in self.values:
                xs.append(item == rhs)
        return xs

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Gt."""
        xs: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                xs.append(self.values[i] > rhs.values[i])
        else:
            for item in self.values:
                xs.append(item > rhs)
        return xs

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Getitem."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            assert len(self.values) == len(rhs)
            xs: list[float] = []
            for i in range(len(rhs)):
                if rhs[i]:
                    xs.append(self.values[i])
            return Simpy(xs)


