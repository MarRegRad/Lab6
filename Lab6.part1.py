#Задание состоит из двух частей.
#1 часть – написать программу в соответствии со своим вариантом задания.
#2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов
# и целевую функцию для оптимизации решения.

#Вариант 10. Составьте все различные лексемы из букв слова «абракадабра» по законам русского языка.

# 1 часть
def generate_words(letters):
    if len(letters) == 0:
        return {''}
    else:
        first = letters[0]
        rest = letters[1:]
        words = generate_words(rest)
        result = set()
        for word in words:
            for i in range(len(word)+1):
                new_word = word[:i] + first + word[i:]
                result.add(new_word)
        result.update(words)
        return result

letters = "абракадабра"
words = generate_words(letters)
print(sorted(words))


