import fire
from parser.vidparser import parsemethods
import os

home_dir = os.path.expanduser("~/")
current_dir = os.getcwd()


def brightest(file, write_path=current_dir):
    parser = parsemethods(file, write_path)
    parser.brightest_frame()


def loudest(file, write_path=current_dir):
    parser = parsemethods(file, write_path)
    parser.loudest_frame()


def ten_seconds(file, write_path=current_dir):
    parser = parsemethods(file, write_path)
    parser.first_ten_seconds()


def before_half(file, write_path=current_dir):
    parser = parsemethods(file, write_path)
    parser.before_half()


def after_half(file, write_path=current_dir):
    parser = parsemethods(file, write_path)
    parser.after_half()


def order(list, file, write_path=current_dir):
    """
    Order function

    Usage: main.py order [1,2,3,4,5] video_file.webm

    Pulls images based off of content in list.

    1 = brightest, 2 = loudest, 3 = ten seconds, 4 = before half, 5 = after half
    """
    parser = parsemethods(file, write_path)

    for i in list:
        if 1 in list:
            parser.brightest_frame()
        if 2 in list:
            parser.loudest_frame()
        if 3 in list:
            parser.first_ten_seconds()
        if 4 in list:
            parser.before_half()
        if 5 in list:
            parser.after_half()


if __name__ == "__main__":
    fire.Fire()
