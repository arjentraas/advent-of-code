from collections import defaultdict

from helper import read_input


def main():
    disk_map = read_input("_2024/day9/example_input.txt").strip()
    file_dict = {}  # store index as key and file_id as value
    empty_spaces = defaultdict(list)  # (length, (start, end))

    file_id = 0
    is_file = True
    current_index = 0
    for char in disk_map:
        if is_file is False:
            is_file = True

            empty_spaces[int(char)].append((current_index, current_index + int(char)))
            current_index += int(char)

        else:
            file_dict[file_id] = (current_index, current_index + int(char))
            file_id += 1
            is_file = False

    # file_id_indices = sorted([k for k in file_dict.keys() if k], reverse=True)

    # for f in file_id_indices:
    #     if i <= empty_spaces[0]:
    #         break
    #     file_dict[empty_spaces[0]] = file_dict[i]
    #     del file_dict[i]
    #     empty_spaces.pop(0)

    # checksum = sum(k * v for k, v in file_dict.items())
    # print(checksum)


main()
