# coding=utf-8
import os


def factorial(n: int):
    return 1 if n == 0 else n * factorial(n-1)


def draw_line(tick_length, tick_label=''):
    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)


def draw_interval(central_length: int):
    if central_length == 1:
        draw_line(1)
        return

    draw_interval(central_length - 1)
    draw_line(central_length)
    draw_interval(central_length - 1)


def draw_ruler(n_inches: int, major_length: int):
    if n_inches <= 0:
        return

    # 0 inch
    draw_line(major_length, '0')
    for i in range(1, n_inches + 1):
        draw_interval(major_length - 1)
        draw_line(major_length, str(i))


def disk_usage(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for file in os.listdir(path):
            child_path = os.path.join(path, file)
            total += disk_usage(child_path)
        print('{0:<7}'.format(total), path)
    return total

