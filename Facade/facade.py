from __future__ import annotations

#Создаю класс фасад
class FacadeGame:
    #Конструктор для класса
    def __init__(self, sigmaSnake: SnakeSigma, snakeCat: SnakeCat) -> None:
        self._sigmaSnake = sigmaSnake or SnakeSigma()
        self._snakeCat = snakeCat or SnakeCat()

    def gamelog(self) -> str:
        #Всякие операции
        gameLog = []
        gameLog.append("Система: Игра началась!")
        gameLog.append(self._sigmaSnake.coordSnake())
        gameLog.append(self._snakeCat.coordSnake())
        gameLog.append("Система: Первый ход!")
        gameLog.append(self._sigmaSnake.move())
        gameLog.append(self._snakeCat.move())
        gameLog.append("Система: Игрок Кошко-змея вышел за пределы поля")
        gameLog.append("Система: Победитель: Сигма-змея. Поздравляем!")
        return "\n".join(gameLog)

#Первый классс с разными методами, которые мы будем использовать в фасаде
class SnakeSigma:

    def coordSnake(self) -> str:
        return "Сигма-Змея: Координаты головы = x:2 y:3"


    def move(self) -> str:
        return "Сигма-Змея: Вверх"

#Второйц класс, который мы также будем использовать
class SnakeCat:

    def coordSnake(self) -> str:
        return "Кошко-Змея: Координаты головы = x:6 y:0"


    def move(self) -> str:
        return "Кошко-Змея: Вниз"

#Пример использования фасада в коде
def game(facadeGame: FacadeGame) -> None:
    print(facadeGame.gamelog(), end="")


if __name__ == "__main__":
    #Создаем 1 обьект
    sigmaSnake = SnakeSigma()
    #2 обьект
    snakeCat = SnakeCat()
    #Перекидываем их в наш фасад, для дальнейшей работы уже с обьектом Класса Фасад
    facadeGame = FacadeGame(sigmaSnake, snakeCat)
    #Работаем с обьектом класса фасад
    game(facadeGame)