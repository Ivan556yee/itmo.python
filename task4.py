RED = '\u001b[41m'
BLUE = '\u001b[44m'
END = '\u001b[0m'
s1 = s2 = 0
with open('sequence.txt', 'r') as file:
    f = [float(i) for i in file]
s1 = sum(abs(x) for x in f[:125])
s2 = sum(abs(x) for x in f[125:250])
s = s1 + s2
percent1 = s1*100/s
percent2 = s2*100/s

print(f"Первые 125 чисел: {percent1:.1f}%")
print(f"Вторые 125 чисел: {percent2:.1f}%")

bar_length = 40
first_bar = int(percent1 * bar_length / 100)
second_bar = int(percent2 * bar_length / 100)

print("Диаграмма:")
print(f"{RED}{' ' * first_bar}{END}{BLUE}{' ' * second_bar}{END}")