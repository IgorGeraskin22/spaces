# -*- coding: utf-8 -*-
# import numeral as numeral

import simple_draw as sd
import snowfall

sd.resolution = (1000, 700)


# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
# снежинки хранить в глобальных переменных модуля snowfall
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

# создать_снежинки(N)
def falling_snowflakes():
    snowfall.creating_snowflakes(snowfall.num)
    while True:
        sd.start_drawing()
        snowfall.drawing_snowflakes(snowfall.colors)
        snowfall.moving_snowflakes()
        snowflakes_remove = snowfall.counting_fallen_snowflakes()
        snowfall.removing_snowflakes(snowflakes_remove)
        snowfall.drawing_snowflakes(snowfall.colour)
        snowfall.creating_snowflakes(len(snowflakes_remove))
        sd.finish_drawing()
        sd.sleep(0.1)
        if sd.user_want_exit():
            break


falling_snowflakes()
sd.pause()

# Зачёт!
