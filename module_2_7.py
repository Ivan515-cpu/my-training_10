import random
def generate_password(n):
    result = [] # Список для хранения паролей
    numbers = list(range(1, n + 1)) # Генерируем числа для пар (от 1 до n)
    for i in range(len(numbers)): # Проходим по всем парам чисел
        for j in range(i + 1, len(numbers)):
            a, b = numbers[i], numbers[j] # Берем текущую пару чисел
            if n % (a + b) == 0: # Проверяем кратность суммы чисел числу n
                result.append(f"{a}{b}") # Добавляем пару в результат
    return ''.join(result) # Возвращаем строку результата
n = random.randint(3, 20) # Согласно условиям границы случайных чисел
password = generate_password(n)
print(f"Число: {n}")
print(f"Пароль: {password}")