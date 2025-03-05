from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

#Интерфейс билдера
class WorkerKFC(ABC):

    @property
    @abstractmethod
    def order(self) -> None:
        pass

    @abstractmethod
    def produce_burger(self) -> None:
        pass

    @abstractmethod
    def produce_french_fries(self) -> None:
        pass

    @abstractmethod
    def produce_drink(self) -> None:
        pass

#Конкретный билдер
class ConcreteWorkerKFC(WorkerKFC):

    def __init__(self) -> None:
        #Делаем пустой объект продукта, который дальше будет использоваться при сборке
        self.reset()

    def reset(self) -> None:
        #Создаем новый продукт
        self._order = Order()

    @property
    def order(self) -> Order:
        #Сохраняем наш продукт
        order = self._order
        #Освобождаем место для след. продукта
        self.reset()
        return order

    def produce_burger(self) -> None:
        self._order.add("Бургер")

    def produce_french_fries(self) -> None:
        self._order.add("Большая картошка фри")

    def produce_drink(self) -> None:
        self._order.add("Добрый Кола")

#Конкртеный продукт
class Order():
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def print_order(self) -> None:
        print(f"Заказ: {', '.join(self.parts)}", end="")


class Director:
    def __init__(self) -> None:
        self._workerkfc = None

    @property
    def workerkfc(self) -> WorkerKFC:
        return self._workerkfc

    @workerkfc.setter
    def workerkfc(self, workerkfc: WorkerKFC) -> None:
        self._workerkfc = workerkfc


    def only_burger_order(self) -> None:
        self.workerkfc.produce_burger()

    def full_Komaru_combo(self) -> None:
        self.workerkfc.produce_burger()
        self.workerkfc.produce_french_fries()
        self.workerkfc.produce_drink()


if __name__ == "__main__":

    #Сделали обьект класса Директор
    director = Director()
    #и обьект класса Билдер
    workerkfc = ConcreteWorkerKFC()
    #Передали директору нашего билдера под управление
    director.workerkfc = workerkfc

    print("Заказ 052 (Только бургер): ")
    director.only_burger_order()
    workerkfc.order.print_order()

    print("\n")

    print("Заказ 012 (Комару комбо): ")
    director.full_Komaru_combo()
    workerkfc.order.print_order()

    print("\n")

    # Помните, что паттерн Строитель можно использовать без класса Директор.
    print("Обед сотрудника (Комару комбо без напитка): ")
    workerkfc.produce_burger()
    workerkfc.produce_french_fries()
    workerkfc.order.print_order()