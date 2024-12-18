from collections import defaultdict

from helper import read_input


def main():
    disk_map = read_input("_2024/day9/input.txt").strip()
    file_dict = {}  # store index as key and file_id as value
    empty_spaces = defaultdict(list)  # (length, (start, end))

    file_id = 0
    is_file = True
    current_index = 0
    for char in disk_map:
        if is_file is False:
            is_file = True
            if int(char) > 0:
                empty_spaces[int(char)].append((current_index, current_index + int(char)))
        else:
            file_dict[file_id] = (current_index, current_index + int(char))

            file_id += 1
            is_file = False
        current_index += int(char)

    file_ids = sorted(file_dict.keys(), reverse=True)

    for file_id in file_ids:
        digit_length = file_dict[file_id][1] - file_dict[file_id][0]
        try:
            fitting_empty_length = next(length for length in empty_spaces.keys() if length >= digit_length)
        except StopIteration:
            continue

        empty_space = empty_spaces[fitting_empty_length][0]
        if empty_space[0] >= file_dict[file_id][0]:
            continue
        file_dict[file_id] = (empty_space[0], empty_space[0] + digit_length)

        leftover_empty_space = empty_space[1] - empty_space[0] - digit_length
        new_empty_space = (
            empty_spaces[fitting_empty_length][0][1] - leftover_empty_space,
            empty_spaces[fitting_empty_length][0][1],
        )
        empty_spaces[fitting_empty_length].pop(0)
        if len(empty_spaces[fitting_empty_length]) == 0:
            del empty_spaces[fitting_empty_length]
        empty_spaces[leftover_empty_space].append(new_empty_space)
        empty_spaces[leftover_empty_space] = sorted(empty_spaces[leftover_empty_space])

    checksum = 0
    for file_id, indices in file_dict.items():
        for position in range(indices[0], indices[1]):
            checksum += file_id * position
    print(checksum)


# 8639151560936 - too high
main()
