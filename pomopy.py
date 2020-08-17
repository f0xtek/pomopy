#!/usr/bin/env python
"""
pomopy - A Python CLI Pomodoro timer.

Allows you to focus using the Pomodoro technique.
"""
import time
from datetime import datetime, timedelta
from argparse import ArgumentParser
from pomopy.notify import notify

ROUNDS = 4
TASK_LENGTH_MINUTES = 25
TIME_FORMAT = '%H:%M:%S'


def get_args():
    parser = ArgumentParser()
    parser.add_argument("-t", "--task-length", type=int, default=25,
                        help="The amount of time in minutes spent working on a task.")
    parser.add_argument("-s", "--short-break-length", type=int, default=5,
                        help='The amount of time in minutes for the short break.')
    parser.add_argument("-l", "--long-break-length", type=int, default=20,
                        help='The amount of time in minutes for the log break.')
    return parser.parse_args()


def pomodoro(task_length, short_break, long_break):
    for it in range(ROUNDS-1):
        timestamp = datetime.now()
        td = timedelta(seconds=task_length * 60)
        next_break = (timestamp + td).strftime(TIME_FORMAT)
        notify(f"{timestamp.strftime(TIME_FORMAT)} - Start work. Next break will be at {next_break}.")
        time.sleep(task_length*60)
        notify(f"{datetime.now().strftime(TIME_FORMAT)} - Take a short break for {short_break} minutes!")
        time.sleep(short_break*60)
    timestamp = datetime.now()
    td = timedelta(seconds=task_length * 60)
    next_break = (timestamp + td).strftime(TIME_FORMAT)
    notify(f"{timestamp.strftime(TIME_FORMAT)} - Start work. Next break will be at {next_break}.")
    time.sleep(task_length*60)
    notify(f"{datetime.now().strftime(TIME_FORMAT)} - Time to take a break for {long_break} minutes!")
    print(f"{datetime.now().strftime(TIME_FORMAT)} - Finished!")


def main():
    args = get_args()
    pomodoro(args.task_length, args.short_break_length, args.long_break_length)


if __name__ == '__main__':
    main()
