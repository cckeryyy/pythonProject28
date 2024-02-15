# Основные предметы
item_key = "Ключ"
item_list = "Записка"
item_book = "Книжка"
item_poster = "Постер"
user = "Kristina"


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
        time.sleep(0.05)  # Задержка между символами, чтобы текст печатался плавно


# Движение
def moving():
    move_forward = 0
    move_backward = 0
    move_left = 0
    move_right = 0
    text_for_backward = False
    text_for_left = False
    text_for_right = False
    while True:
        try:
            move = input("Куда идти? (a - Лево, w - Прямо, d - Право, s - Назад): ").lower()
            if user:
                if move == "w":
                    if move_forward < 5:
                        print("Вы сделали 4 шага вперед")
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
                        print("Вы сделали 4 шага в право")
                        move_right += 1
                        move_left -= 1
                    else:
                        print("Тут стена")
                elif move == "a":
                    if not text_for_left:
                        print("Вы розвернулись и сделали 4 шага на лево")
                        text_for_left = True
                    if move_left < 5:
                        print("Вы сделали 4 шага на лево")
                        move_left += 1
                        move_right -= 1
                    elif move_left == 5:
                        print("Тут стена")
                    else:
                        print("IDK")
                elif move == "s":
                    if not text_for_backward:
                        print("Вы розвернулись назад и сделали 4 шага")
                        text_for_backward = True
                    if move_backward < 5:
                        print("Вы сделали 4 шага назад")
                        move_backward += 1
                        move_forward -= 1
                    elif move_backward == 5:
                        print("Тут стена")
                    else:
                        print("IDK")

        except ValueError:
            print("Введите пожалуйста правильный ответ")


# Функция инвентаря
def inventory():
    while True:
        try:
            inventory_inside = []
            print(f"Вы нашли и подняли этот предмет: {item_key}")
            do_take = int(input("Взять этот предмет? (1 - Да | 2 - Нет): "))
            if do_take == 1:
                print(f"Вы положили {item_key} в инвентарь")
                inventory_inside.append(item_key)
                break
            elif do_take == 2:
                print(f"Вы выбросили {item_key}")
                break
        except ValueError:
            print("Введите пожалуйста число в ответ")


history()
moving()
inventory()