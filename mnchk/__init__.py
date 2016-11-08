# coding: utf-8
import os
import sys
from struct import unpack, error
from shutil import copy


class MnException(Exception):
    pass


def print_progress(iteration, total, prefix="", suffix="", decimals=1, bar_length=100):
    """ Console progress bar.
    Original code from https://stackoverflow.com/a/34325723

    :param iteration: current iteration
    :type iteration: int
    :param total: total iterations
    :type total: int
    :param prefix: prefix string
    :type prefix: str
    :param suffix: suffix string
    :type suffix: str
    :param decimals: positive number of decimals in percent complete
    :type decimals: int
    :param bar_length: character length of bar
    :type bar_length: int
    """
    format_str = "{0:." + str(decimals) + "f}"
    percents = format_str.format(100 * (iteration / float(total)))
    filled_length = int(round(bar_length * iteration / float(total)))
    bar = "█" * filled_length + "-" * (bar_length - filled_length)
    sys.stdout.write("\r%s |%s| %s%s %s" % (prefix, bar, percents, "%", suffix)),
    if iteration == total:
        sys.stdout.write("\n")
    sys.stdout.flush()


def is_valid(filename, magic_number):
    """ Check if the file `filename` is valid based on its `magic_number`.

    :param filename: path to the file to be tested
    :param magic_number: magic_number to test against
    :return: True if valid, False otherwise
    """
    try:
        with open(os.path.abspath(filename), "rb") as fh:
            try:
                data = unpack("I", fh.read(4))[0]
                return data == magic_number

            except error:
                pass

    except IOError as msg:
        raise MnException("Could not open {}. {}".format(filename, msg))


def mn_check(directory, magic_number, output_dir):
    """ Check all files in `directory` if they are valid. If so, copy them to another directory.

    :param directory:
    :param magic_number:
    :param output_dir:
    """
    count = 0
    valid_count = 0
    files = os.listdir(directory)
    total = len(files)

    print_progress(count, total, prefix="[*] Progress:", suffix="Complete. ({} are valid)".format(valid_count), bar_length=50)
    for filename in files:
        filename = os.path.join(directory, filename)
        if is_valid(filename, magic_number):
            valid_count += 1
            copy(filename, output_dir)
        count += 1
        print_progress(count, total, prefix="[*] Progress:", suffix="Complete. ({} are valid)".format(valid_count), bar_length=50)
