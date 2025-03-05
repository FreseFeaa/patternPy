from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List

#Создаем абстрактный класс Субьекта
class TelegramChannel(ABC):
    @abstractmethod
    def addSubscriber(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def banSubscriber(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notification(self) -> None:
        pass

#Конкретный класс субьекта
class KomaruTelegramChannel(TelegramChannel):


    _сoolness: int = None


    _observers: List[Observer] = []


    def addSubscriber(self, observer: Observer) -> None:
        print("KomaruTelegramChannel: Новый юзер подписался на канал!")
        self._observers.append(observer)

    def banSubscriber(self, observer: Observer) -> None:
        print(f"KomaruTelegramChannel: Юзер был забанен")
        self._observers.remove(observer)


    def notification(self) -> None:
        print("KomaruTelegramChannel: Отправление уведомлений...")
        for observer in self._observers:
            observer.update(self)

    def newKomaruPhoto(self) -> None:

        print("\nTelegramChannel: Новая фотка кошки Комару!!!")
        self._сoolness = randrange(6, 11)

        print(f"TelegramChannel: Крутость Кошки комару на фото: {self._сoolness}")
        self.notification()

#Создаем абстрактный класс наблюдателя
class Observer(ABC):
    
    @abstractmethod
    def update(self, subject: TelegramChannel) -> None:
        pass

#Первый наблюдатель
class ConcreteObserverA(Observer):
    def update(self, subject: TelegramChannel) -> None:
        if subject._сoolness > 6:
            print("Юзер(Komugi):  Классная фотка!")

#Второй наблюдатель
class ConcreteObserverB(Observer):
    def update(self, subject: TelegramChannel) -> None:
        if subject._сoolness >= 9:
            print("Юзер(Kokao): Эта фотка просто имба!")
        else:
            print("Юзер(Kokao): В целом неплохо :)")


if __name__ == "__main__":
    
    #Создаем тг канал Кошки Комару  (https://t.me/komaru)
    subject = KomaruTelegramChannel()

    #Создаем нового юзера и подписываем его на канал
    observer_a = ConcreteObserverA()
    subject.addSubscriber(observer_a)

    #Создаем еще одного юзера и подписываем его на канал
    observer_b = ConcreteObserverB()
    subject.addSubscriber(observer_b)

    #Новые фотки Кошки
    subject.newKomaruPhoto()
    subject.newKomaruPhoto()
    
    #Баним юзера, ткк слишком однотипно отвечает (Мб это вообще бот)
    subject.banSubscriber(observer_a)

    #И еще одна новая фотка Комару
    subject.newKomaruPhoto()







