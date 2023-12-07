import random
from typing import List, Tuple


def roll_dice(num: int, faces: int) -> Tuple[int, ...]:
    return random.choices(range(1, faces + 1), k=num)


class Board:
    def __init__(self):
        self.board: List[str] = [
            "GO", "A1", "CC1", "A2", "T1", "R1", "B1", "CH1", "B2", "B3", "JAIL", "C1", "U1", "C2", "C3", "R2", "D1",
            "CC2", "D2", "D3", "FP", "E1", "CH2", "E2", "E3", "R3", "F1", "F2", "U2", "F3", "G2J", "G1", "G2", "CC3",
            "G3", "R4", "CH3", "H1", "T2", "H2"
        ]
        self.name_to_id = {name: i for (i, name) in enumerate(self.board)}
        self.current = 0
        self.chances = ["GO", "JAIL", "C1", "E3", "H2", "R1", "R", "R", "U", "-3"] + 6 * ["-"]
        random.shuffle(self.chances)
        self.chances_id = 0
        self.comm_chest = ["GO", "JAIL"] + 14 * ["-"]
        random.shuffle(self.comm_chest)
        self.cchest_id = 0
        self.counter = {i: 0 for i in range(len(self.board))}
        self.utilities = [i for (i, tile) in enumerate(self.board) if tile.startswith("U")]
        self.railways = [i for (i, tile) in enumerate(self.board) if tile.startswith("R")]
        self.doubles = 0
    
    def move(self) -> None:
        d1, d2 = roll_dice(num=2, faces=4)
        if d1 == d2:
            self.doubles += 1
            if self.doubles == 3:
                self.current = self.name_to_id["JAIL"]
                self.doubles = 0
                self.counter[self.current] += 1
                return
        else:
            self.doubles = 0
        steps = d1 + d2
        self.current = (self.current + steps) % len(self.board)
        if self.board[self.current] == "G2J":
            self.current = self.name_to_id["JAIL"]
        elif self.board[self.current].startswith("CC"):
            cchest = self.comm_chest[self.cchest_id]
            self.cchest_id = (self.cchest_id + 1) % 16
            if cchest == "-":
                pass
            else:
                self.current = self.name_to_id[cchest]
        elif self.board[self.current].startswith("CH"):
            chance = self.chances[self.chances_id]
            self.chances_id = (self.chances_id + 1) % 16
            if chance == "-3":
                self.current = (self.current - 3) % len(self.board)
            elif chance == "U":
                for u in self.utilities:
                    if self.current < u:
                        self.current = u
                        break
                if self.current > self.utilities[-1]:
                    self.current = self.utilities[0]
            elif chance == "R":
                for r in self.railways:
                    if self.current < r:
                        self.current = r
                        break
                if self.current > self.railways[-1]:
                    self.current = self.railways[0]
            elif chance == "-":
                pass
            else:
                self.current = self.name_to_id[chance]
        self.counter[self.current] += 1

    def chart(self) -> List[Tuple[str, str, float]]:
        tiles = []
        total = sum(self.counter.values())
        for tile_id, count in sorted(self.counter.items(), key=lambda item: item[1], reverse=True):
            tiles.append((str(tile_id).zfill(2), self.board[tile_id], count / total))
        return tiles
    

def main():
    board = Board()
    for _ in range(10000000):
        board.move()
    for t in board.chart()[:6]:
        print(f"{t[0]}, {t[1]}, {t[2]*100:.3f}%")


if __name__ == '__main__':
    main()
