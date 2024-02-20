# Квестовие предметы
item_key_first_location = "Key"  # Ключ для первой локации
item_key_shaman = "Key of the Elder Gate"  # Ключ для последней лакации
item_locket = "Locket"  # Медальон
item_map = "Map"  # Карта для

# Все основные предметы
item_lighter = "Lighter\n"  # Зажигалка
item_knife = "Machete\n"  # Мачете
item_compass = "Compass\n"  # Компас
item_matches = "Matches"  # Спички

# Персонажи
player = "James Everest"  # Main person
shaman = "Berthold the Wise"  # Quest person
leader_of_aborigines = "Mbongi"  # Person


# Все локации:
# Первая локация
def info_first_location():
    print("Старая дверь - выглядит так, будто она охраняет что-то древнее и непостижимое, что скрыто за ее массивными\n"
          "створками. Ее ручка, облезлая от времени, кажется словно протягивающейся вам рукою секретов, готовых быть\n"
          "раскрытыми.При приближении к двери, вы чувствуете, как в воздухе витает непостижимая аура тайны и мистики.\n"
          "Плотный воздух напоминает вам о могуществе истории, о давно забытых временах и событиях, которые таятся за\n"
          "этими древними планками.\n"
          "Доступные действия: Движения: WASD, подбор предметов")


# Вторая локация
def info_third_location():
    print("Хижина шаманов - Вы стоите перед скрытой в глубинах леса хижиной, известной как Хижина Шаманов. Ее стены\n "
          "скрыты мхом , а крыша покрыта плетеньем из сухих лоз. Структура, казалось бы, сливается с окружающей\n "
          "природой, словно выросшая из самой земли.")


# Третья локация
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

    text = """В древние времена существовало загадочное королевство Атлантида, известное своим богатством и 
мудростью. Легенды гласят, что в его сердце хранился медальон с невероятной силой, способной изменить ход событий.
Молодой и отважный искатель приключений, Джеймс, узнал о медальоне и решил отправиться в опасное путешествие через 
древние пирамиды, чтобы найти его. По пути ему предстоит преодолеть различные препятствия и встретить загадочных 
шаманов, готовых помочь ему в его поисках.
Так начинается захватывающее приключение Джеймса, наполненное опасностями и тайнами, где каждый шаг приводит
его ближе к желанному медальону и его удивительной силе.

    Удачи
    
    
        """

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)


def last_location():
    while True:
        print("Джеймс (возбуждённо): Вот мы и пришли, древние пирамиды! Их величие просто потрясающее.\n"
              "Джеймс подходит к основанию пирамиды и вглядывается в древние резные узоры на камнях.\n"
              "Джеймс: Взглянуть на эти узоры - это как взглянуть в прошлое. Какое великое мастерствоОн начинает осматривать пирамиду более внимательно, обходя её вокруг.\n"
              "Джеймс (про себя): Но где же вход? Где то должен быть какой-то признак... Ага! (Он замечает выступ, который выглядит как ключевая деталь, отличающаяся от окружающих камней.) Это должно быть то, что я искал!\n"
              "Джеймс приближается к выступу и осматривает его. Затем он вытаскивает ключ из своего сумки, подходит к выступу и вставляет его в выемку.)\n"
              "Джеймс: Это совершенно точно! Ключ вставлен. Теперь, давайте посмотрим, что там внутри...")


def f_check_item(x, y, medal_position, invent):
    if (x, y) == medal_position:
        print("Вы нашли древний артефакт!")


def move_forward():
    moves = ["w", "w", "a", "w", "w", "d", "d", "w", "a", "w", "w"]
    for move in moves:
        s_move = input("Куда идти? (a - Лево, w - Прямо, d - Право, c - Открыть инвентарь): ").lower()
        if s_move != move:
            print("DEAD")
            return
    print("Молодец, ты прошел нашу ловушку")
    return third_location_moving_for_quest()


def third_location_moving():
    x = 0
    y = 0
    invent = read_inventory()
    medal_position = (6, 13)

    while True:
        try:
            move = input("Куда идти? (a - Лево, w - Прямо, d - Право, s - Назад, c - Открыть инвентарь): ").lower()
            if move == "w":
                move_forward()
                f_check_item(x, y, medal_position, inventory)
                if (x, y) == medal_position:
                    print("Поздравляем! Вы нашли древний медальон!")
                    return invent
            else:
                print("IDK")

        except ValueError:
            print("Введите пожалуйста правильный ответ")


def third_location_moving_for_quest():
    print("Вы успешно завершили квест!")
    steps = 0
    while steps < 3:
        moved = input("Куда идти? (w - Прямо): ").lower()
        if moved == "w":
            steps += 1
            print(f"Шаг {steps}")
        else:
            print("DEAD")
            return
    return the_end()


def the_end():
    import sys
    import time
    text = ("Джеймс вздохнул с облегчением, понимая, что его миссия завершена. Он удерживал в руках Полуночный Медальон\n"
            "— ключ к силе, но и к ответственности за его использование.Вернувшись из джунглей, Джеймс стал хранителем\n"
            "медальона, используя его мудро и справедливо для защиты своего мира от зла. Он помнил свое приключение как\n"
            "испытание, которое сделало его сильнее и мудрее. И, несмотря на то, что его путешествие подошло к концу,\n"
            "новые приключения всегда ждали его впереди, ведь мир полон тайн и загадок, готовых быть раскрытыми тем,\n"
            "кто смело идет вперед.\n"
            ""
            "GG")

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(2)
    sys.exit()


def second_location_moving():
    move_forward = 0
    while True:
        try:
            move = input("Куда идти? (w - Прямо, c - Открыть инвентарь): ").lower()
            if move == "w":
                if move_forward < 3:
                    print("Вы сделали 1 шаг вперед")
                    move_forward += 1
                elif move_forward == 3:
                    return third_location_moving()
            elif move == "c":
                return inventory()
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
    inventor = read_inventory()
    item_position = (3, 3)
    door_position = (5, 3)
    has_key = "Key" in inventor
    while True:
        try:
            move = input("Куда идти? (a - Лево, w - Прямо, d - Право, s - Назад, c - Открыть инвентарь): ").lower()
            if move:
                if move == "w":  # Прямо
                    if move_forward < 5:
                        print("Вы сделали 1 шаг вперед")
                        move_forward += 1
                        move_backward -= 1
                        check_item(move_forward, move_left, item_position, inventor)
                        check_door(move_forward, move_left, door_position, has_key)
                    elif move_forward == 5:
                        print("Тут стена")
                    else:
                        print("IDK")
                elif move == "d":
                    if not text_for_right:
                        print("Вы развернулись на право")
                        text_for_right = True
                    if move_right < 5:
                        print("Вы сделали 1 шаг в право")
                        move_right += 1
                        move_left -= 1
                        check_item(move_forward, move_left, item_position, inventor)
                        check_door(move_forward, move_left, door_position, has_key)
                    else:
                        print("Тут стена")
                elif move == "a":
                    if not text_for_left:
                        print("Вы развернулись и сделали 1 шаг на лево")
                        text_for_left = True
                    if move_left < 5:
                        print("Вы сделали 1 шаг на лево")
                        move_left += 1
                        move_right -= 1
                        check_item(move_forward, move_left, item_position, inventor)
                        check_door(move_forward, move_left, door_position, has_key)
                    elif move_left == 5:
                        print("Тут стена")
                    else:
                        print("IDK")
                elif move == "s":
                    if not text_for_backward:
                        print("Вы развернулись назад и сделали 1 шаг")
                        text_for_backward = True
                    if move_backward < 5:
                        print("Вы сделали 1 шаг назад")
                        move_backward += 1
                        move_forward -= 1
                        check_item(move_forward, move_left, item_position, inventor)
                        check_door(move_forward, move_left, door_position, has_key)
                    elif move_backward == 5:
                        print("Тут стена")
                elif move:
                    if move == "c":
                        return inventory(inventor)
                    else:
                        return first_location_moving()
            else:
                print("IDK")

        except ValueError:
            print("Введите пожалуйста правильный ответ")


def remove_item_from_inventory(item_to_remove):
    try:
        with open("inventory.txt", "r") as file:
            inventory_items = file.readlines()
    except FileNotFoundError:
        print("Файл инвентаря не найден.")
        return

    try:
        inventory_items.remove(item_to_remove + '\n')
        with open("inventory.txt", "w") as file:
            file.writelines(inventory_items)
        print(f"Предмет {item_to_remove} удален из инвентаря.")
    except ValueError:
        print(f"Предмет {item_to_remove} не найден в инвентаре.")


def check_door(x, y, door_position, has_key):
    if (x, y) == door_position:
        if has_key:
            print("Вы нашли дверь!")
            print("Поздравляем, у вас есть ключ, вы можете открыть дверь!")
        else:
            print("Здесь дверь!")
            print("Вам нужен ключ, чтобы открыть эту дверь.")
    elif (x, y) == door_position and not has_key:
        print("Здесь дверь!")
        print("Вам нужен ключ, чтобы открыть эту дверь.")


# Функция для первого предмета
def check_item(x, y, item_position, inventor):
    global item_key_first_location
    if (x, y) == item_position:
        print(f"Вы нашли {item_key_first_location}!")
        if item_key_first_location in inventor:
            print("У вас уже есть этот предмет в инвентаре.")
            return
        take_item = input(f"Хотите взять {item_key_first_location}? (1 - Да, 2 - Нет): ")
        if take_item == "1":
            inventor.append(item_key_first_location)
            write_inventory(inventor)
            print(f"{item_key_first_location} добавлен в инвентарь!")
        elif take_item == "2":
            return first_location_moving()


def write_inventory(items):
    with open("inventory.txt", "w") as file:
        for item in items:
            file.write(item + '\n')


def read_inventory():
    try:
        with open("inventory.txt", "r") as file:
            return [item.strip() for item in file.readlines()]
    except FileNotFoundError:
        items = ["Lighter", "Machete", "Compass", "Matches"]
        with open("inventory.txt", "w") as file:
            for item in items:
                file.write(item + '\n')
        return items


def inventory(inventor):
    print("Ваш инвентарь:")
    for item in inventor:
        print(item)
    input("Введите любую кнопку что бы закрыть инвентарь: ")


# Функция инвентаря только для квестовых предметов:
# Функция для ключа шамана
def inventory_key_shaman():
    try:
        print(f"Вам дали этот предмет: {item_key_shaman}")
        do_take = input("Взять этот предмет? (1 - Да | 2 - Нет | 3 - Инвентарь): ")
        if do_take == "1":
            with open("inventory.txt", "a") as file:
                if item_key_shaman != item_key_shaman:
                    print(f"Вы положили {item_key_shaman} в инвентарь")
                    file.write(item_key_shaman + "\n")
                elif item_key_shaman == item_key_shaman:
                    print("У вас достаточно таких предметов")
        elif do_take == "2":
            print(f"Вы выбросили {item_key_shaman}")
            return inventory_key_shaman()
        elif do_take == "3":
            print("Ваш инвентарь:")
            with open("inventory.txt", "r") as file:
                inventory_inside = file.read()
                print(inventory_inside)
    except ValueError:
        print("Введите пожалуйста число в ответ")


# Функция для первой локации
def inventory_key():
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


# Функция для карты
def inventory_map():
    try:
        print(f"Вам дали этот предмет: {item_key_shaman}")
        do_take = input("Взять этот предмет? (1 - Да | 2 - Нет | 3 - Инвентарь): ")
        if do_take == "1":
            with open("inventory.txt", "a") as file:
                if item_key_shaman != item_key_shaman:
                    print(f"Вы положили {item_key_shaman} в инвентарь")
                    file.write(item_key_shaman + "\n")
                elif item_key_shaman == item_key_shaman:
                    print("У вас достаточно таких предметов")
        elif do_take == "2":
            print(f"Вы выбросили {item_key_shaman}")
            return inventory_map()
        elif do_take == "3":
            print("Ваш инвентарь:")
            with open("inventory.txt", "r") as file:
                inventory_inside = file.read()
                print(inventory_inside)
    except ValueError:
        print("Введите пожалуйста число в ответ")


def start_game_fl():
    history_called = False
    info_first_location_called = False

    while True:
        if not history_called:
            history()
            history_called = True

        if not info_first_location_called:
            info_first_location()
            info_first_location_called = True

        first_location_moving()


# def start_game_sl():
#     info_third_location_called = False
#     second_location_called = False
#
#     while True:
#         if not info_third_location_called:
#             info_third_location()
#             info_third_location_called = True
#
#         second_location_moving()
#
#         if not second_location_called:
#             second_location()
#             second_location_called = True


def start_game_tl():
    info_fourth_location = False
    press_f = False

    while True:
        if not info_fourth_location:
            info_fourth_location = True

        if not press_f:
            third_location_moving()
            press_f = True

        third_location_moving_for_quest()


start_game_tl()

