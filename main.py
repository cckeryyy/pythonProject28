def second_location():
    import random
    f_puzzle = "Не отыскать её корней,\nВерхушка выше тополей.\nВсё круче вверх она идёт -\nА не растёт."
    s_puzzle = "Без голоса кричит,\nБез крыльев — а летает,\nИ безо рта свистит,\nИ без зубов кусает."
    t_puzzle = "Две ноги на трёх ногах,\nА четвёртая в зубах.\nВдруг четыре прибежали\nИ с безногой убежали."
    fourth_puzzle = "А что у меня в кармане?"
    fifth_puzzle = "Пожирает всё кругом:\nЗверя, птицу, лес и дом.\nСталь сгрызёт, железо сгложет,\nКрепкий камень уничтожит,\nВласть его всего сильней,\nДаже власти королей."
    puzzles = [s_puzzle, t_puzzle, f_puzzle, fourth_puzzle, fifth_puzzle]
    f_answer = 'Гора'
    s_answer = 'Ветер'
    t_answer = 'Человек сидит на табуретке и ест рыбу'
    fourth_answer = 'Ключ Старших Врат'
    fifth_answer = 'Время'
    popitok = 3
    while True:
        print("Джеймс: Приветствую, мудрый Бертольд! Я ищу ключ от древних пирамид. Может быть, ты можешь помочь мне?")
        print(
            "Бертольд: Добро пожаловать, молодой искатель приключений. Чтобы получить ключ, тебе нужно пройти "
            "испытание моей мудрости. Готов ли ты к вызову загадки?")
        print("Джеймс: Конечно, я готов! Я всегда готов к новым вызовам.")
        puzzle = random.choice(puzzles)
        print(f"Бертольд: Великолепно! Вот моя загадка: {puzzle}\n")
        if puzzle == f_puzzle:
            print(f"Ответ (1 - 'Цветок', 2 - '{f_answer}', 3 - 'Камень'): ")
            answer = input("Выбери правильный ответ: ")
            if answer == "2":
                print(
                    "Бертольд: Отлично, Джеймс! Ты прав. Мудро мыслишь. Вот ключ от древних пирамид, он поможет тебе "
                    "продолжить твое путешествие.\nДжеймс: Спасибо тебе, Бертольд! Я ценю твою помощь и мудрость. "
                    "Теперь я отправлюсь дальше, к новым приключениям!")
                break
            else:
                popitok -= 1
                if popitok > 0:
                    print(f"Не правильно!! У тебя осталось {popitok} попыт{'ка' if popitok == 1 else 'ки'}")
                else:
                    print("Вас ЗАКОЛОЛИ (дозой)")
                    break
        elif puzzle == s_puzzle:
            print(f"Ответ (1 - 'Самум', 2 - 'Буря', 3 - '{s_answer}'): ")
            answer = input("Выбери правильный ответ: ")
            if answer == "3":
                print(
                    "Бертольд: Отлично, Джеймс! Ты прав. Мудро мыслишь. Вот ключ от древних пирамид, он поможет "
                    "тебе продолжить твое путешествие.\nДжеймс: Спасибо тебе, Бертольд! Я ценю твою помощь и "
                    "мудрость. Теперь я отправлюсь дальше, к новым приключениям!")
                break
            else:
                popitok -= 1
                if popitok > 0:
                    print(f"Не правильно!! У тебя осталось {popitok} попыт{'ка' if popitok == 1 else 'ки'}")
                else:
                    print("Вас ЗАКОЛОЛИ (дозой)")
                    break
        elif puzzle == t_puzzle:
            print(
                f"Ответ (1 - 'Человек инвалид', 2 - '{t_answer}', 3 - 'Человек инвалид НО в каляске'): ")
            answer = input("Выбери правильный ответ: ")
            if answer == "2":
                print(
                    "Бертольд: Отлично, Джеймс! Ты прав. Мудро мыслишь. Вот ключ от древних пирамид, он поможет тебе "
                    "продолжить твое путешествие.\nДжеймс: Спасибо тебе, Бертольд! Я ценю твою помощь и мудрость. "
                    "Теперь я отправлюсь дальше, к новым приключениям!")
                break
            else:
                popitok -= 1
                if popitok > 0:
                    print(f"Не правильно!! У тебя осталось {popitok} попыт{'ка' if popitok == 1 else 'ки'}")
                else:
                    print("Вас ЗАКОЛОЛИ (дозой)")
                    break
        elif puzzle == fourth_puzzle:
            print(
                f"Ответ (1 - '{fourth_answer}', 2 - 'Кошелек', 3 - 'Камень'): ")
            answer = input("Выбери правильный ответ: ")
            if answer == "1":
                print(
                    "Бертольд: Отлично, Джеймс! Ты прав. Мудро мыслишь. Вот ключ от древних пирамид, он поможет тебе "
                    "продолжить твое путешествие.\nДжеймс: Спасибо тебе, Бертольд! Я ценю твою помощь и мудрость. "
                    "Теперь я отправлюсь дальше, к новым приключениям!")
                break
            else:
                popitok -= 1
                if popitok > 0:
                    print(f"Не правильно! У тебя осталось {popitok} попыт{'ка' if popitok == 1 else 'ки'}")
                else:
                    print("Вас ЗАКОЛОЛИ (дозой)")
                    break
        elif puzzle == fifth_puzzle:
            print(
                f"Ответ (1 - '{fifth_answer}', 2 - 'Огонь', 3 - 'Охотник'): ")
            answer = input("Выбери правильный ответ: ")
            if answer == "1":
                print(
                    "Бертольд: Отлично, Джеймс! Ты прав. Мудро мыслишь. Вот ключ от древних пирамид, он поможет тебе "
                    "продолжить твое путешествие.\nДжеймс: Спасибо тебе, Бертольд! Я ценю твою помощь и мудрость. "
                    "Теперь я отправлюсь дальше, к новым приключениям!")
                break
            else:
                popitok -= 1
                if popitok > 0:
                    print(f"Не правильно!! У тебя осталось {popitok} попыт{'ка' if popitok == 1 else 'ки'}")
                else:
                    print("Вас ЗАКОЛОЛИ (дозой)")
                    break
        else:
            print("Потрачено")
