from utils import read_input


def main():
    disk_map = read_input("_2024/day9/input.txt").strip()
    ordered_dict = {}  # store index as key and file_id as value
    empty_spaces = []  # store indices of empty_spaces

    file_id = 0
    is_file = True
    current_index = 0
    for char in disk_map:
        if is_file is False:
            is_file = True

            for _ in range(int(char)):
                empty_spaces.append(current_index)
                current_index += 1

            continue

        for i in range(int(char)):
            ordered_dict[current_index] = file_id
            current_index += 1

        file_id += 1
        is_file = False

    file_id_indices = sorted([k for k in ordered_dict.keys() if k], reverse=True)

    for i in file_id_indices:
        if i <= empty_spaces[0]:
            break
        ordered_dict[empty_spaces[0]] = ordered_dict[i]
        del ordered_dict[i]
        empty_spaces.pop(0)

    checksum = sum(k * v for k, v in ordered_dict.items())
    print(checksum)


main()
