#!/usr/bin/python3

import pickle
import argparse
import random
import time
import os


def parse_arguments():
    """To parse the arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-time",
        type=int,
        help="New word frequency in seconds",
        default=150)
    args = parser.parse_args()
    return args


def show_words():
    t = parse_arguments().time
    d = pickle.load(open("gre.p", "rb"))
    words = list(d.keys())
    while True:
        w = random.choice(words)
        m = d[w]
        os.system('notify-send "' + w + '" "' + m + '"')
        time.sleep(t)


if __name__ == "__main__":
    show_words()
