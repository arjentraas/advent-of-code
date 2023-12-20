from pathlib import Path

from tqdm import tqdm

with Path("day5/input_day5").open("r") as handle:
    input_data = [line.strip() for line in handle.readlines()]

# input_data = """seeds: 79 14 55 13

# seed-to-soil map:
# 50 98 2
# 52 50 48

# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15

# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4

# water-to-light map:
# 88 18 7
# 18 25 70

# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13

# temperature-to-humidity map:
# 0 69 1
# 1 0 69

# humidity-to-location map:
# 60 56 37
# 56 93 4""".splitlines()


seeds = [int(s) for s in input_data[0].split(" ")[1:]]
seed_pairs = []
for i in range(0, len(seeds), 2):
    seed_pairs.append([seeds[i], seeds[i + 1]])


maps_str_lst = input_data[2:]

maps = {}
for i, line in enumerate(maps_str_lst):
    if "map" in line:
        map_name = line.split(" ")[0]
        start = i
    if not line:
        end = i
        maps[map_name] = maps_str_lst[start + 1 : end]

    if i == len(maps_str_lst) - 1:
        maps[map_name] = maps_str_lst[start + 1 :]

for map_name, map_items in maps.items():
    list_map_items = []
    for map_item in map_items:
        items = map_item.split(" ")
        list_map_items.append(
            {
                "start_source": int(items[1]),
                "end_source": int(items[1]) + int(items[2]) - 1,
                "start_dest": int(items[0]),
                "end_dest": int(items[0]) + int(items[2]) - 1,
            }
            #     int(items[1]),  # start_source,
            #     int(items[1]) + int(items[2]) - 1,  # end_source
            #     int(items[0]),  # start dest
            #     int(items[0]) + int(items[2]) - 1,
            # ]
        )
    maps[map_name] = list_map_items


def get_dst_val(src: int, maps: list):
    dst = src
    for m in maps:
        if src >= m[0] and src <= m[1]:
            dst = m[2] + src - m[0]
    return dst


# locations = []
# for seed in tqdm(seeds):
#     soil = get_dst_val(seed, maps["seed-to-soil"])
#     fertilizer = get_dst_val(soil, maps["soil-to-fertilizer"])
#     water = get_dst_val(fertilizer, maps["fertilizer-to-water"])
#     light = get_dst_val(water, maps["water-to-light"])
#     temperature = get_dst_val(light, maps["light-to-temperature"])
#     humidity = get_dst_val(temperature, maps["temperature-to-humidity"])
#     location = get_dst_val(humidity, maps["humidity-to-location"])
#     locations.append(location)
# print(
#     f"Seed {seed}, soil {soil}, fertilizer {fertilizer}, water {water}, light {light}, temperature {temperature}, humidity {humidity}, location {location}."
# )

# print(min(locations))


# locations = []
# lowest_location = 9999999999999999999999
# num_iters = 0
# for seed_pair in seed_pairs:
#     num_iters += seed_pair[1]
#     for seed in tqdm(range(seed_pair[0], seed_pair[0] + seed_pair[1])):
#         soil = get_dst_val(seed, maps["seed-to-soil"])
#         fertilizer = get_dst_val(soil, maps["soil-to-fertilizer"])
#         water = get_dst_val(fertilizer, maps["fertilizer-to-water"])
#         light = get_dst_val(water, maps["water-to-light"])
#         temperature = get_dst_val(light, maps["light-to-temperature"])
#         humidity = get_dst_val(temperature, maps["temperature-to-humidity"])
#         location = get_dst_val(humidity, maps["humidity-to-location"])
#         if location < lowest_location:
#             lowest_location = location
#         # locations.append(location)

# print(lowest_location)
