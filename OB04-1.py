### Шаг 1: Создание абстрактного класса для оружия

from abc import ABC, abstractmethod

class Weapon(ABC):

    @abstractmethod
    def attack(self):
        pass


### Шаг 2: Реализация конкретных типов оружия

class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

class Bow(Weapon):
    def attack(self):
        return "Боец наносит удар из лука."

### Шаг 3: Модификация класса Fighter

class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None  # Оружие еще не выбрано

    def choose_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {type(weapon).__name__.lower()}.")

    def change_weapon(self, new_weapon: Weapon):
        self.weapon = new_weapon
        print(f"{self.name} меняет оружие на {type(new_weapon).__name__.lower()}.")

    def attack(self):
        if self.weapon:
            return self.weapon.attack()
        else:
            return "У бойца нет оружия!"

### Шаг 4: Реализация класса Monster и механизма боя

class Monster:
    def __init__(self, name):
        self.name = name

    def defeated(self):
        return f"{self.name} побежден!"

# Функция для демонстрации боя
def battle(fighter: Fighter, monster: Monster):
    print(fighter.attack())
    print(monster.defeated())

### Пример использования программы

#Теперь мы можем использовать все эти классы для демонстрации работы программы:

if __name__ == "__main__":
    # Создаем бойца и монстра
    fighter = Fighter("Боец-1")
    monster = Monster("Монстр-1")

    # Боец выбирает меч
    fighter.choose_weapon(Sword())
    battle(fighter, monster)

    # Боец меняет оружие на лук
    fighter.change_weapon(Bow())
    battle(fighter, monster)