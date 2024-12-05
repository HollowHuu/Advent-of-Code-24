input = [line.upper() for line in open("./Day 4/input.txt", "r").read().split("\n")]

xmas_count = 0

def check_diag_up_left(row_idx, col_idx):
    if input[row_idx][col_idx] != "M":
        return False
    if row_idx >= 2 and col_idx >= 2:
        if (
            col_idx - 1 < len(input[row_idx - 1])
            and col_idx - 2 < len(input[row_idx - 2])
        ):
            if input[row_idx - 1][col_idx - 1] == "A" and input[row_idx - 2][col_idx - 2] == "S":
                return True
    return False

def check_diag_up_right(row_idx, col_idx):
    if input[row_idx][col_idx] != "M":
        return False
    if row_idx >= 2 and col_idx + 2 < len(input[row_idx]):
        if (
            col_idx + 1 < len(input[row_idx - 1])
            and col_idx + 2 < len(input[row_idx - 2])
        ):
            if input[row_idx - 1][col_idx + 1] == "A" and input[row_idx - 2][col_idx + 2] == "S":
                return True
    return False

def check_diag_down_left(row_idx, col_idx):
    if input[row_idx][col_idx] != "M":
        return False
    if row_idx + 2 < len(input) and col_idx >= 2:
        if (
            col_idx - 1 < len(input[row_idx + 1])
            and col_idx - 2 < len(input[row_idx + 2])
        ):
            if input[row_idx + 1][col_idx - 1] == "A" and input[row_idx + 2][col_idx - 2] == "S":
                return True
    return False

def check_diag_down_right(row_idx, col_idx):
    if input[row_idx][col_idx] != "M":
        return False
    if row_idx + 2 < len(input) and col_idx + 2 < len(input[row_idx]):
        if (
            col_idx + 1 < len(input[row_idx + 1])
            and col_idx + 2 < len(input[row_idx + 2])
        ):
            if input[row_idx + 1][col_idx + 1] == "A" and input[row_idx + 2][col_idx + 2] == "S":
                return True
    return False

for row_idx, line in enumerate(input):
    for col_idx, char in enumerate(line):
        if char == "M":
            if check_diag_up_left(row_idx, col_idx) and check_diag_up_right(row_idx, col_idx - 2):
                xmas_count += 1
            if check_diag_up_right(row_idx, col_idx) and check_diag_down_right(row_idx - 2, col_idx):
                xmas_count += 1
            if check_diag_down_right(row_idx, col_idx) and check_diag_down_left(row_idx, col_idx + 2):
                xmas_count += 1
            if check_diag_down_left(row_idx, col_idx) and check_diag_up_left(row_idx + 2, col_idx):
                xmas_count += 1

print(xmas_count)
