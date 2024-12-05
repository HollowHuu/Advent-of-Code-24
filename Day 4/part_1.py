input = [line.upper() for line in open("./Day 4/input.txt", "r").read().split("\n")]

xmas_count = 0

for row_idx, line in enumerate(input):
    for col_idx, char in enumerate(line):
        if char == "X":
            # Check horizontally to the right
            if col_idx + 3 < len(line) and line[col_idx + 1] == "M" and line[col_idx + 2] == "A" and line[col_idx + 3] == "S":
                xmas_count += 1
            
            # Check vertically downwards
            if row_idx + 3 < len(input) and len(input[row_idx + 1]) > col_idx and len(input[row_idx + 2]) > col_idx and len(input[row_idx + 3]) > col_idx:
                if input[row_idx + 1][col_idx] == "M" and input[row_idx + 2][col_idx] == "A" and input[row_idx + 3][col_idx] == "S":
                    xmas_count += 1
            
            # Check diagonally down-right
            if row_idx + 3 < len(input) and col_idx + 3 < len(line):
                if (
                    len(input[row_idx + 1]) > col_idx + 1
                    and len(input[row_idx + 2]) > col_idx + 2
                    and len(input[row_idx + 3]) > col_idx + 3
                ):
                    if input[row_idx + 1][col_idx + 1] == "M" and input[row_idx + 2][col_idx + 2] == "A" and input[row_idx + 3][col_idx + 3] == "S":
                        xmas_count += 1
            
            # Check horizontally to the left
            if col_idx >= 3 and line[col_idx - 1] == "M" and line[col_idx - 2] == "A" and line[col_idx - 3] == "S":
                xmas_count += 1
            
            # Check diagonally down-left
            if row_idx + 3 < len(input) and col_idx >= 3:
                if (
                    len(input[row_idx + 1]) > col_idx - 1
                    and len(input[row_idx + 2]) > col_idx - 2
                    and len(input[row_idx + 3]) > col_idx - 3
                ):
                    if input[row_idx + 1][col_idx - 1] == "M" and input[row_idx + 2][col_idx - 2] == "A" and input[row_idx + 3][col_idx - 3] == "S":
                        xmas_count += 1
            
            # Check vertically upwards
            if row_idx >= 3 and len(input[row_idx - 1]) > col_idx and len(input[row_idx - 2]) > col_idx and len(input[row_idx - 3]) > col_idx:
                if input[row_idx - 1][col_idx] == "M" and input[row_idx - 2][col_idx] == "A" and input[row_idx - 3][col_idx] == "S":
                    xmas_count += 1
            
            # Check diagonally up-left
            if row_idx >= 3 and col_idx >= 3:
                if (
                    len(input[row_idx - 1]) > col_idx - 1
                    and len(input[row_idx - 2]) > col_idx - 2
                    and len(input[row_idx - 3]) > col_idx - 3
                ):
                    if input[row_idx - 1][col_idx - 1] == "M" and input[row_idx - 2][col_idx - 2] == "A" and input[row_idx - 3][col_idx - 3] == "S":
                        xmas_count += 1
            
            # Check diagonally up-right
            if row_idx >= 3 and col_idx + 3 < len(line):
                if (
                    len(input[row_idx - 1]) > col_idx + 1
                    and len(input[row_idx - 2]) > col_idx + 2
                    and len(input[row_idx - 3]) > col_idx + 3
                ):
                    if input[row_idx - 1][col_idx + 1] == "M" and input[row_idx - 2][col_idx + 2] == "A" and input[row_idx - 3][col_idx + 3] == "S":
                        xmas_count += 1

print(xmas_count)
