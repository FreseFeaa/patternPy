#Первый интерфейс, который имеет нужный нам метод
class Me:
    def phrase(self) -> str:
        return "Я: Комару, ты очень красиво выглядишь!"

#Второй Адаптируемый класс, который содержит нужное нам поведение, но его интерфейс несовместим с существующим общим кодом
class Komaru:

    def komaru_phrase(self) -> str:
        return "Ми мяу!"

#Крутой класс адаптер, который наследуеться сразу от обоих классов
class Translator(Me, Komaru):
    #Переназначаем метод первого класса (Который мы наследовали), при этом делаем это используя метод второго класса
    def phrase(self) -> str:
        if self.komaru_phrase() == "Ми мяу!":
            return "Переводчик: Ты тоже!"
        else:
            return "Переводчик: Ошибка, текст не распознан"
        

#Наш общий код
def say(me: "Me") -> None:

    print(me.phrase(), end="")


if __name__ == "__main__":
    print("Вы встретили Комару, и хотите с ней поговорить")
    me = Me()
    say(me)
    print("\n")

    komaru = Komaru()
    print(f"Комару: {komaru.komaru_phrase()}", end="\n\n")

    print("Я: Я не понимаю, что ты хочешь мне сказать( \n После того, как я включу переводчик с Кошачьего, повтори пожалуйста)")
    print("--Переводчик был включён--\n")
    translator = Translator()
    print(f"Комару: {komaru.komaru_phrase()}", end="\n\n")
    say(translator)