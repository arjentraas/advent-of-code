from helper import read_input


def main():
    input = read_input("_2024/day11/input.txt").strip()
    stones = [int(char) for char in input.split(" ")]

    for i in range(75):
        new_stones = []

        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                halfway = int(len(str(stone)) / 2)
                new_stones.append(int(str(stone)[:halfway]))
                new_stones.append(int(str(stone)[halfway:]))
            else:
                new_stones.append(stone * 2024)
        stones = new_stones

    print(len(stones))


main()
