from utils import read_input


def parse_input():
    lines = read_input("2024/day5/input_day5.txt")
    split = lines.split("\n\n")
    rules = []
    for rule in split[0].split("\n"):
        rule_split = rule.split("|")
        rules.append((int(rule_split[0]), int(rule_split[1])))

    updates = []
    for update in split[-1].split("\n"):
        update_split = update.split(",")
        updates.append([int(u) for u in update_split])

    return rules, updates


def is_update_correct(update, rules) -> bool:
    update_correct = True
    for before, after in rules:
        if before not in update or after not in update:
            continue

        before_index = update.index(before)
        after_index = update.index(after)

        if after_index < before_index:
            update_correct = False
    return update_correct


def get_correct_updates(rules, updates):
    correct_updates = []
    for update in updates:
        if is_update_correct(update, rules) is False:
            continue
        correct_updates.append(update)
    return correct_updates


def get_middle_page(update):
    middle_index = int((len(update) - 1) / 2)
    return update[middle_index]


def part_1():
    rules, updates = parse_input()
    correct_updates = get_correct_updates(rules, updates)

    sum = 0

    for update in correct_updates:
        sum += get_middle_page(update)

    print(sum)


def find_incorrect_rules(update, rules):
    incorrect_rules = []
    for before, after in rules:
        if before not in update or after not in update:
            continue
        before_index = update.index(before)
        after_index = update.index(after)
        if after_index < before_index:
            incorrect_rules.append((before, after))

    return incorrect_rules


def should_before(incorrect, reference, rules):
    for before, after in rules:
        if incorrect == before and reference == after:
            return True
    return False


def order_update(update, rules):
    incorrect_rules = find_incorrect_rules(update, rules)
    incorrect_numbers = set()
    for before, after in incorrect_rules:
        incorrect_numbers.add(before)
        incorrect_numbers.add(after)

    correct_numbers = [num for num in update if num not in incorrect_numbers]

    for incorrect_number in incorrect_numbers:
        incorrect_added = False
        for correct_number in correct_numbers:
            if not should_before(incorrect_number, correct_number, rules):
                continue

            if len(correct_numbers) == 1:
                correct_numbers.insert(0, incorrect_number)
                incorrect_added = True
                break
            else:
                correct_index = correct_numbers.index(correct_number)
                correct_numbers.insert(correct_index, incorrect_number)
                incorrect_added = True
                break

        if incorrect_added is True:
            continue

        correct_numbers.append(incorrect_number)
    return correct_numbers


def part_2():
    rules, updates = parse_input()
    correct_updates = get_correct_updates(rules, updates)
    incorrect_updates = [update for update in updates if update not in correct_updates]
    sum = 0
    for update in incorrect_updates:
        correct_update = order_update(update, rules)
        sum += get_middle_page(correct_update)
    print(sum)


part_1()
part_2()
