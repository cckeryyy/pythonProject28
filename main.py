# Квестовие предметы
item_key_first_location = "Key"  # Ключ для первой локации
item_key_shaman = "Key of the Elder Gate"  # Ключ для последней лакации
item_map = "Map"  # Карта для

# Все основные предметы
item_lighter = "Lighter"  # Зажигалка
item_knife = "Machete"  # Мачете
item_compass = "Compass"  # Компас
item_locket = "Locket"  # Медальон
item_matches = "Matches"  # Спички

# Персонажи
player = "James Everest"  # Main person
shaman = "Berthold the Wise"  # Quest person
leader_of_aborigines = "Mbongi"  # Person


def puzzles():
    import random
    puzzle = [
        "Не отыскать её корней,\nВерхушка выше тополей.\nВсё круче вверх она идёт -\nА не растёт.",
        "Без голоса кричит,\nБез крыльев — а летает,\nИ безо рта свистит,\nИ без зубов кусает.",
        "Две ноги на трёх ногах,\nА четвёртая в зубах.\nВдруг четыре прибежали\nИ с безногой убежали.",
        "А что у меня в кармане?",
        "Пожирает всё кругом:\nЗверя, птицу, лес и дом.\nСталь сгрызёт, железо сгложет,\nКрепкий камень уничтожит,\nВласть его всего сильней,\nДаже власти королей."
    ]
    return random.choice(puzzle)


# Все локации:
# Первая локация
def info_first_location():
    print("Старая дверь - выглядит так, будто она охраняет что-то древнее и непостижимое, что скрыто за ее массивными\n"
          "створками. Ее\n"
          "ручка, облезлая от времени, кажется словно протягивающейся вам рукою секретов, готовых быть раскрытыми.При\n"
          "приближении к двери, вы чувствуете, как в воздухе витает непостижимая аура тайны и мистики. Плотный воздух\n"
          "напоминает вам о могуществе истории, о давно забытых временах и событиях, которые таятся за этими древними\n"
          "планками.")


# Вторая локация
def info_second_location():
    print("Джунгли - Вы находитесь глубоко в дремучих джунглях, где каждый шаг наполнен таинственностью и опасностью\n."
          "Плотная зеленая листва заслоняет небо, пропуская едва заметные лучи солнца сквозь густую зелень.")


# Третья локация
def info_third_location():
    print("Хижина шаманов - Вы стоите перед скрытой в глубинах леса хижиной, известной как Хижина Шаманов. Ее стены\n "
          "скрыты мхом , а крыша покрыта плетеньем из сухих лоз. Структура, казалось бы, сливается с окружающей\n "
          "природой, словно выросшая из самой земли.")


# Четвёртая локация
def info_fourth_location():
    print("Древние пирамиды- Величественные сооружения, свидетели далекого прошлого. Поднимающиеся ввысь, они словно\n"
          "касаются небес, а их монументальные стены излучают таинственное величие, в котором слились сила и загадка.\n"
          "Вокруг пирамид раскинулась пустынная пустота, наполненная древними тайнами и невысказанными\n"
          "историями.Стены пирамид украшены загадочными рельефами, изображающими древних фараонов, богов и сцены из"
          "их жизни и верований.")


# Предистория
def history():
    import sys
    import time

    text = """
    Вы думаете, из-за чего вы здесь оказались? Хм, ну тогда слушайте... 

    Всё началось с одного момента, когда муж по имени Дима исчез по неизвестной причине,
    и его жена по имени Кристина нашла записку в их комнате, в которой было написано следующее:
    "-77.982919, 118.866311". После этого жена поняла, что что-то здесь не так,
    и отправилась на поиски своего мужа. Она села в машину и поехала по этим координатам.
    Прошел час, два, три, и после долгих поисков она наконец доехала к этим координатам.
    Но эти координаты вели в центр леса. После того как она доехала, она вышла из машины,
    взяла с собой телефон, зажигалку и маленький нож, и пошла дальше, смотря в телефон. 
    Она так шла примерно 1-2 часа, но когда она приблизилась к этим координатам,
    она увидела перед собой небольшой бугорок, похожий на бункер. Рванула к этому бункеру,
    но, пройдя лишь 10 шагов, пол под ней обвалился, и она оказалась там, где ты находишься сейчас.

    Удачи

    Кристина: "Ай, как больно. Где я? Что это за место? Ладно, не надо расслабляться. Пора выбираться отсюда."
    """

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)


def second_location_moving():
    move_forward = 0
    move_left = 0
    move_right = 0
    text_for_left = False
    text_for_right = False
    while True:
        try:
            move = input("Куда идти? (a - Лево, w - Прямо, d - Право, c - Открыть инвентарь): ").lower()
            if player:
                if move == "w":
                    if move_forward < 5:
                        print("Вы сделали 1 шаг вперед")
                        move_forward += 1
                    elif move_forward == 5:
                        print("Тут стена")
                    else:
                        print("IDK")
                elif move == "d":
                    if not text_for_right:
                        print("Вы розвернулись на право")
                        text_for_right = True
                    if move_right < 5:
                        print("Вы сделали 1 шаг в право")
                        move_right += 1
                        move_left -= 1
                    else:
                        print("Тут стена")
                elif move == "a":
                    if not text_for_left:
                        print("Вы розвернулись и сделали 1 шаг на лево")
                        text_for_left = True
                    if move_left < 5:
                        print("Вы сделали 1 шаг на лево")
                        move_left += 1
                        move_right -= 1
                    elif move_left == 5:
                        print("Тут стена")
                    else:
                        print("IDK")
        except ValueError:
            print("Введите пожалуйста правильный ответ")


# Движение
def first_location_moving():
    move_forward = 0
    move_backward = 0
    move_left = 0
    move_right = 0
    text_for_backward = False
    text_for_left = False
    text_for_right = False
    while True:
        try:
            move = input("Куда идти? (a - Лево, w - Прямо, d - Право, s - Назад, c - Открыть инвентарь): ").lower()
            if player:
                if move == "w":
                    if move_forward < 5:
                        print("Вы сделали 1 шаг вперед")
                        move_forward += 1
                        move_backward -= 1
                    elif move_forward == 5:
                        print("Тут стена")
                    else:
                        print("IDK")
                elif move == "d":
                    if not text_for_right:
                        print("Вы розвернулись на право")
                        text_for_right = True
                    if move_right < 5:
                        print("Вы сделали 1 шаг в право")
                        move_right += 1
                        move_left -= 1
                    else:
                        print("Тут стена")
                elif move == "a":
                    if not text_for_left:
                        print("Вы розвернулись и сделали 1 шаг на лево")
                        text_for_left = True
                    if move_left < 5:
                        print("Вы сделали 1 шаг на лево")
                        move_left += 1
                        move_right -= 1
                    elif move_left == 5:
                        print("Тут стена")
                    else:
                        print("IDK")
                elif move == "s":
                    if not text_for_backward:
                        print("Вы розвернулись назад и сделали 1 шаг")
                        text_for_backward = True
                    if move_backward < 5:
                        print("Вы сделали 1 шаг назад")
                        move_backward += 1
                        move_forward -= 1
                    elif move_backward == 5:
                        print("Тут стена")
                elif move == "c":
                    return inventory
                continue
            else:
                print("IDK")

        except ValueError:
            print("Введите пожалуйста правильный ответ")


# Функция инвентаря только для квестовых предметов


# Функция инвентаря
def inventory():
    while True:
        try:
            print(f"Вы нашли и подняли этот предмет: {item_key_first_location}")
            do_take = input("Взять этот предмет? (1 - Да | 2 - Нет | 3 - Инвентарь): ")
            if do_take == "1":
                with open("inventory.txt", "a") as file:
                    if item_key_first_location != item_key_first_location:
                        print(f"Вы положили {item_key_first_location} в инвентарь")
                        file.write(item_key_first_location + "\n")
                    elif item_key_first_location == item_key_first_location:
                        print("У вас достаточно таких предметов")
            elif do_take == "2":
                print(f"Вы выбросили {item_key_first_location}")
                break
            elif do_take == "3":
                print("Ваш инвентарь:")
                with open("inventory.txt", "r") as file:
                    inventory_inside = file.read()
                    print(inventory_inside)
        except ValueError:
            print("Введите пожалуйста число в ответ")


while True:
    info_first_location()
    first_location_moving()
    inventory()
