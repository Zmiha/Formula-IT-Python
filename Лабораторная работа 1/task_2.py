list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

"""
Другой способ разделения игроков
firstCommand = list_players[::2] 
secondCommand = list_players[1::2]
"""

firstCommand = list_players[:3]
secondCommand = list_players[3:]

print(firstCommand)
print(secondCommand)
