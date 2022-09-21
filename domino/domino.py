import argparse
import math

__version__ = "1.0.0"


def get_row(row):
    allowed = r'\|/'
    letters = set(row)
    if any(letter not in allowed for letter in letters):
        raise ValueError(f"Wrong character(s) detected in {row}. Allowed characters are: {allowed}")
    return row


def move(row, moves):
    moves_dict = {
        '|/': '|',
        '/|': '/',
        '/\\': '|',
        '\/': '|',
        '//': '/',
        '\\\\': '\\',
        '||': '|',
        '|\\': '\\',
        '\\|': '|'
    }

    for move in range(moves):
        new_row = ""
        for i, letter in enumerate(row, 0):
            if letter == '|':
                if i == 0 and i+1 == len(row):
                    new_row += moves_dict['||']
                elif i == 0 and i+1 < len(row):
                    new_row += moves_dict[f'|{row[i+1]}']
                elif i+1 == len(row):
                    new_row += moves_dict[f'{row[i-1]}|']
                else:
                    new_row += moves_dict[f'{row[i-1]}{row[i+1]}']
            else:
                new_row += letter
        row = new_row
    return row

def play_domino(args):
    row = move(args.row, args.moves)
    print(f"Final domino row: {row}")


def verify_row(row):
    allowed = r'\|/'
    letters = set(row)
    if any(letter not in allowed for letter in letters):
        raise ValueError(f"Wrong character(s) detected in {row}. Allowed characters are: {allowed}")
    return row


def verify_moves(moves):
    moves = int(moves)
    if moves < 0:
        raise ValueError("The value must be positive integer or 0")
    return moves


def args_init():
    parser = argparse.ArgumentParser(
    description='')
    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s {}'.format(__version__))
    parser.add_argument('--row', '-r', required=True, type=verify_row, action='store',
        help=r'Set the playing board. Please remember, that allowed characters are: \, /, |')
    parser.add_argument('--moves', '-m', default=1, type=verify_moves,
                        help='Set the number of moves. The type must be positive integer or 0')
    return parser.parse_args()


if __name__ == "__main__":
    args = args_init()
    play_domino(args)
