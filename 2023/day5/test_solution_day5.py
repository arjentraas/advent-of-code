from day5.solution_day5 import Almanac

example = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4""".splitlines()

almanac = Almanac(example)


class TestAlmanac:
    def test_maps(self):
        assert {79: 81} in almanac.__getattribute__("seed-to-soil").all_map_items
        assert {55: 57} in almanac.__getattribute__("seed-to-soil").all_map_items

    def test_get_destination_value(self):
        assert almanac.__getattribute__("seed-to-soil")._get_destination_value(14) == 14
        assert almanac.__getattribute__("seed-to-soil")._get_destination_value(79) == 81
        assert almanac.__getattribute__("seed-to-soil")._get_destination_value(55) == 57
        assert almanac.__getattribute__("seed-to-soil")._get_destination_value(13) == 13

    def test_get_location(self):
        assert almanac._get_location_number(almanac.seeds[0]) == 82
        assert almanac._get_location_number(almanac.seeds[1]) == 43
        assert almanac._get_location_number(almanac.seeds[2]) == 86
        assert almanac._get_location_number(almanac.seeds[3]) == 35

    def test_get_lowest_location(self):
        assert almanac._get_lowest_location() == 35
