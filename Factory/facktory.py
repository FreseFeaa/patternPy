from __future__ import annotations
from abc import ABC, abstractmethod


#Создаем абстрактный класс (Наследуем от Abstract Base Classes, для возможности использования всяких абстракций)
class CreatorDucks(ABC):
    @abstractmethod #Декоратор, который обязывает реализовать этот метод в подклассах абстрактного класса.
    def newDuck(self):
        # Тут можно прописать как будет работать этот метод по умолчанию 
        pass

    
    def duckProcess(self) -> str:

        # Вызываем фабричный метод, чтобы получить объект-продукт.
        duck = self.newDuck()

        # Далее, работаем с этим продуктом.
        result = f"Утка: {duck.quack()}"

        return result



#Первый креатор, наследованный от нашего абстрактного
class CreatorSigmaDucks(CreatorDucks):
    
    #Переопределяем фабричный метод, создания продукта 
    def newDuck(self) -> Duck:
        return SigmaDuck()

#Второй креатор, также наследованный от нашего абстрактного
class CreatorPlushDuck(CreatorDucks):
    #Для этого креатора тоже переопределяем фабричный метод, создания продукта 
    def newDuck(self) -> Duck:
        return PlushDuck()





#Общий/Абстрактный класс => который по сути является интерфейсом
class Duck(ABC):
    #Также метод, который должны реализовать подклассы
    @abstractmethod
    def quack(self) -> str:
        pass



#Первый продукт
class SigmaDuck(Duck):
    #Переопределяем  метод 
    def quack(self) -> str:
        return "Кря кря !!!"

#Второй продукт
class PlushDuck(Duck):
    #Переопределяем  метод 
    def quack(self) -> str:
        return "Я плюшевая утка и не умею крякать ((("




def komaruDialog(creatorDucks: CreatorDucks) -> None:
    print(f"Комару: Привет, Утка!!! Можешь покрякать? \n"
          f"{creatorDucks.duckProcess()}", end="")


if __name__ == "__main__":
    print("Разговор кошки Комару с Сигма Уткой")
    komaruDialog(CreatorSigmaDucks())
    print("\n")

    print("Разговор кошки Комару с Плюшевой уткой")
    komaruDialog(CreatorPlushDuck())