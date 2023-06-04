""" implementation of conways game of life
    Rules
    1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    2. Any live cell with two or three live neighbours lives on to the next generation.
    3. Any live cell with more than three live neighbours dies, as if by overpopulation.
    4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
 """
from functools import cache
from dataclasses import dataclass

import sys
import argparse


@dataclass
class Cell:
    x: int
    y: int



def print_errors_and_exit() -> None:
    print('The life file path provided either does not exist or did not conform to the Life 1.06 file format.')
    print('https://conwaylife.com/wiki/Life_1.06')
    sys.exit(-1)


def get_cells_from_file(cell_file: str) -> dict[tuple[int, int], int]:
    file_broken = False
    try:
        with open(cell_file, 'r') as file:
            lines = file.read().splitlines()
        file_broken = validate_life_format(lines)
    except (FileNotFoundError, IndexError):
        file_broken = True
    
    if file_broken:
        print_errors_and_exit()

    # remove #Life 1.06 line
    lines.pop(0)

    cells: dict[tuple[int, int], int] = {}
    for line in lines:
        x, y = line.split(' ')
        coordinates = (int(x), int(y))
        cells[coordinates] = 0
    return cells


class Conway:
    def __init__(self, cells: dict[tuple[int, int], int]) -> None:
        self.cells = cells
        self.neighbor_count: dict[tuple[int, int] int] = {}

    def update_neighbors(self) -> None:
        neighbors = {}
        for cell in self.cells.keys():
            x, y = cell

            neighbors = [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1), (x + 1, y + 1), (x + 1, y - 1), (x - 1, y - 1), (x - 1, y + 1)]
            for neighbor in neighbors:
                neighbors[neighbor] = self.cells.get(neighbor, 0) + 1
        
        self.neighbor_count = neighbors



    def calculate_next_generation(self) -> None:
        self.update_neighbors()

        delete = set()
        new_life = set()
        for cell, neighbors in self.neighbor_count.items():
            if neighbors < 2:
                delete.add(cell)
            if neighbors == 2 or neighbors == 3 and cell in self.cells:
                continue
            if neighbors > 3:
                delete.add(cell)
            if neighbors == 3:
                new_life.add(cell)
        
        if len(self.cells) == 1:
            self.cells = {}

        for cell, neighbors in self.cells.items():
            



def validate_life_format(lines: list[str]) -> bool:
    return lines[0] != '#Life 1.06'


def perform_generation_calculations(conways: Conway, number_of_lifecycles_to_calculate: int) -> None:
    for _ in range(number_of_lifecycles_to_calculate):
        conways.calculate_next_generation()


def output_to_file(conways: Conway, output_file: str) -> None:
    with open(output_file, 'w') as file:
        file.write('#Life 1.06\n')
        for x, y in conways.cells:
            file.write(f'{x} {y}\n')


@cache
def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Perform conways game of life algorithm on a given Life 1.06 file, and output the result.')
    parser.add_argument('--life_file', type=str, help='The Life 1.06 file to perform the algorithm on')
    parser.add_argument('--number_of_lifecycles_to_calculate', type=int, help='The number of lifecycles to perform on the given life file.')
    parser.add_argument('--output_file', type=str, help='Output the result to this file.')
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cells = get_cells_from_file(args.life_file)
    conways = Conway(cells)
    perform_generation_calculations(conways, args.number_of_lifecycles_to_calculate)
    output_to_file(conways, args.output_file)


if __name__ == '__main__':
    main()
