'''--- Part Two ---'''

reports = open("./Day 2/input.txt", "r").read().split("\n")


def validate_report(levels: list[int], removed_level: bool = False) -> bool:
    '''Validate the report to see if the levels are safe'''
    if len(levels) < 2:
        return False

    print(levels)

    for i in range(len(levels)):
        if i == 0:
            continue
        
        # Print current level and previous level for debugging
        print(levels[i])

        if levels[i] == levels[i-1]:
            if handle_unsafe(levels, removed_level, i):
                continue
            return False

        if abs(levels[i] - levels[i-1]) > 3:
            if handle_unsafe(levels, removed_level, i):
                continue
            return False

    return True

def handle_unsafe(levels: list[int], removed_level: bool, index: int) -> bool:
    '''Handle the unsafe levels'''
    if removed_level:
        return False
    levels.pop(index)
    removed_level = True

    if not validate_report(levels, removed_level):
        return False

    return True

def fix_report(report):
    '''Fix the report to be a list of integers'''
    levels = []
    for i in report:
        levels.append(int(i))

    return levels

def count_valid_reports(reports: list[str]) -> int:
    '''Count the number of valid reports'''
    count = 0
    for report in reports:
        levels = fix_report(report.split())

        if validate_report(levels):
            count += 1
            # print(levels)
    return count

# print(count_valid_reports(reports))

def test_statement():
    levels = [87, 90, 92, 95, 96, 93]
    assert validate_report(levels)
    levels = [87, 90, 92, 95, 96, 93, 97]
    assert validate_report(levels)
    levels = [100, 100, 97, 95, 94, 93]
    assert validate_report(levels)
    levels = [78, 80, 83, 84, 86, 93, 90]
    assert not validate_report(levels)

test_statement()