import random

# Список слов для кроссворда
words = ["КОТ", "СЛОН", "ДОМ", "ЗМЕЯ", "ПАЛКА", "КНИГА", "РЕКА", "ВЕТЕР"]

# Генерация случайного порядка слов
random.shuffle(words)

# Создание сетки кроссворда (10x10)
grid_size = 12
grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]


def place_word(word, x, y, direction):
    if direction == 'h':
        for i in range(len(word)):
            grid[y][x + i] = word[i]
    elif direction == 'v':
        for i in range(len(word)):
            grid[y + i][x] = word[i]


# Размещение слов в сетке
for word in words:
    placed = False
    while not placed:
        x = random.randint(0, grid_size - len(word))
        y = random.randint(0, grid_size - len(word))
        direction = random.choice(['h', 'v'])

        can_place = True
        if direction == 'h':
            for i in range(len(word)):
                if grid[y][x + i] != ' ' and grid[y][x + i] != word[i]:
                    can_place = False
                    break
        else:
            for i in range(len(word)):
                if grid[y + i][x] != ' ' and grid[y + i][x] != word[i]:
                    can_place = False
                    break

        if can_place:
            place_word(word, x, y, direction)
            placed = True

# Вывод кроссворда
for row in grid:
    print(' '.join(row))
