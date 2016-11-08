# coding: utf-8
import argparse

from mnchk import *


class MnChk(object):

    @staticmethod
    def parse_args():
        """ CLI args parser
        """
        parser = argparse.ArgumentParser(
            prog="mnchk",
            description="Magic number checker. Filter out the file that does not use the right magic number.",
            epilog="Returns 0 if successful, -1 otherwise"
        )

        mand = parser.add_argument_group("mandatory")
        mand.add_argument("-i", "--input", dest="input", required=True, type=str,
                          help="input file or directory containing files to check")
        mand.add_argument("-m", "--magic-number", dest="magic_number", required=True, type=str,
                          help="magic number to check input against")
        mand.add_argument("-o", "--output", dest="output_dir", required=True, type=str,
                          help="output directory where to copy the valid files")

        return parser.parse_args()

    @classmethod
    def main(cls):
        """ Main routine
        :return: 0 if successful, -1 otherwise.
        """
        args = cls.parse_args()

        input_dir = ""
        input_file = ""

        if not os.path.exists(args.input):
            print("{} does not exist, exiting...")
            return -1

        magic = int(args.magic_number, 16)

        output_dir = os.path.abspath(args.output_dir)
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)

        if not os.path.isdir(args.input):
            input_file = os.path.abspath(args.input)
            if is_valid(input_file, magic):
                copy(input_file, output_dir)

        else:
            input_dir = os.path.abspath(args.input)
            mn_check(input_dir, magic, output_dir)

        return 0


def main():
    """ Console script entry point """
    sys.exit(MnChk.main())


if __name__ == '__main__':
    sys.exit(MnChk.main())
