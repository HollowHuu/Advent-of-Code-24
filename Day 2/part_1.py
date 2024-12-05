reports = open("./Day 2/input.txt", "r").read().split("\n")

def validate_report(levels):
    direction = 0
    if len(levels) < 2:
        return False

    if levels[0] > levels[1]: # If the first level is greater than the second level, the direction is descending
        direction = 0
    elif levels[0] < levels[1]: # If the first level is less than the second level, the direction is ascending
        direction = 1
    else:
        return False # If the two levels are the same, its unsafe

    match direction:
        case 1:
            # Orders must be in ascending order
            for i in range(1, len(levels)):
                if (levels[i-1] < levels[i]) and (levels[i] - levels[i-1]) <= 3:
                    continue
                else:
                    return False
        case 0:
            # Orders must be in descending order
            for i in range(1, len(levels)):
                if (levels[i-1] > levels[i]) and (levels[i-1] - levels[i]) <= 3:
                    continue
                else:
                    return False

    return True

def fix_report(report):
    levels = []
    for i in report:
        levels.append(int(i))

    return levels

def count_valid_reports(reports):
    count = 0
    for report in reports:
        levels = fix_report(report.split())

        if validate_report(levels):
            count += 1
            print(levels)
    return count

print(count_valid_reports(reports))