tree_count_in_row = 1
row_count = 1

robot_count = 1

while True:
    tree_count_in_row += 2
    row_count += 1

    robot_count += tree_count_in_row

    if robot_count > 251:
        break

print(f"{robot_count} robots in a tree of {row_count} rows with the last row {tree_count_in_row} robots")
