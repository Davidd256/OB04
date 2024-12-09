### Шаг 1: Создание абстрактного класса для оружия

from abc import ABC, abstractmethod

class Weapon(ABC):

    @abstractmethod
    def attack(self):
        pass