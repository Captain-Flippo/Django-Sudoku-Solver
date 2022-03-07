import numpy as np

class SudokuSolver:
    def __init__(self, sudoku_data):
        self.solutions = []
        self.formatted = []
        self.failsafe = False
        if sudoku_data:
            self.data = self.dict_format(sudoku_data)
            self.data = np.asarray(self.data)
            if len(self.data[self.data == 0]) <= 56:
                self.solve()
                self.div_format()
            else:
                self.failsafe = True
        else:
            pass

    def show(self):
        countrow = 1
        for row in self.data:
            countentry = 1
            rowstring = ""
            for entry in row:
                if entry == 0:
                    entry = "-"
                if countentry % 3 == 0:
                    rowstring += str(entry) + " | "
                else:
                    rowstring += str(entry) + " "
                countentry += 1
            print(rowstring)
            if countrow % 3 == 0:
                print("-"*28)
            countrow += 1

    def rules(self, x, y, n):
        if n in self.data[:, y]:
            return False
        if n in self.data[x, :]:
            return False
        x0 = (x//3)*3
        y0 = (y//3)*3
        if n in self.data[x0:x0+3, y0:y0+3]:
            return False
        return True

    def solve(self):
        for y in range(9):
            for x in range(9):
                if self.data[x, y] == 0:
                    for n in range(1, 10):
                        if self.rules(x, y, n):
                            self.data[x, y] = n
                            self.solve()
                            self.data[x, y] = 0
                    return
        self.solutions.append(np.copy(self.data.tolist()))
    
    def div_format(self):
        segments = [(0,3), (3,6), (6,9)]
        for su in self.solutions:
            sdarray = np.asarray(su)
            sudoku = []
            for x in segments:
                row = []
                for y in segments:
                    row.append(sdarray[x[0]:x[1], y[0]:y[1]].tolist())
                sudoku.append(row)
            self.formatted.append(sudoku)
    
    
    def dict_format(self, form_dict):
        sudoku_list = []
        row = [0 for i in range(9)]
        for i in range(9):
            sudoku_list.append(row)
        sudoku_list = np.asarray(sudoku_list)
        for keyword in form_dict:
            if "bl-" in keyword:
                if form_dict[keyword] == "":
                    number = 0
                else:
                    number = int(form_dict[keyword])
                block_id, field_id = keyword.split(":")
                block_parts = block_id.split("-")[1:]
                field_parts = field_id.split("-")[1:]
                y = int(block_parts[0])*3 + int(field_parts[0])
                x = int(block_parts[1])*3 + int(field_parts[1])
                sudoku_list[y,x] = number
        return sudoku_list
                


def test():
    test = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]]

    S = SudokuSolver(test)
    S.solve()
    print(S.solutions)


if __name__ == "__main__":
    test()
