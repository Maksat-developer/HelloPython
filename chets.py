# 1 Запрос пользователя через getpass 


# from getpass import getpass


# username = input("Введите логин: ")
# password = getpass("Введите пароль: ")


# # 2 Разница между == и is 

# first = [1, 2, 3]
# second = [1, 2, 3]

# print(first == second) # True потомучто значения одинаковы 
# print(first is second) # False потомучто is указывают на разные обьекиы в памяти 

# 3 Разница sort() и sorted()

games = ['Wither', 'Counter-Strike', 'Minecraft']

games_sorted = sorted(games)
print("sorted() возвращает копию массива в отсортированном виде:")
print("\u2514\u2500\u2500", games_sorted, '\n')

print("Исходный список:")
print("\u2514\u2500\u2500", games, '\n')


games.sort()
print("sort() возврощает отсортриованный исходный список:")
print("\u2514\u2500\u2500", games, '\n')





