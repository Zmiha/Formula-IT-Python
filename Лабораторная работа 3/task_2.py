# TODO Напишите функцию find_common_participants
def find_common_participants(first, second, parser=","):
    first = set(first.split(parser))
    second = set(second.split(parser))
    command_intersection = list(first.intersection(second))
    command_intersection.sort()
    return command_intersection


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, "|"))

# TODO Провеьте работу функции с разделителем отличным от запятой
