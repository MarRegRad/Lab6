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
#words = generate_words(letters)
#print(sorted(words))


# 2 часть
#ограничение - две согласные не могут быть рядом
#целевая функция - лексемы с наибольшим числом согласных на нечетных местах


max_count_sogl = 0
res = []
sogl = "бркд"
gl = "а"
words = generate_words(letters)
for i in words:
    rule = True
    count_sogl = 0
    for j in range(len(i)):
        if (j%2 == 1):
            if i[j] in sogl:
                # кол-во согласных в слове
                count_sogl += 1
    for j in range(0, len(i) - 1):
        if ((i[j] in sogl) and (i[j+1] in sogl)):
            rule = False
    if rule:
        if count_sogl == max_count_sogl:
            res.append(i)
        if count_sogl > max_count_sogl:
            res = []
            max_count_sogl = count_sogl
            res.append(i)
print(f"""
Максимальное число согласных в слове: {max_count_sogl}
Кол-во ликсем, удовлетворяющих условию: {len(res)}
Лексемы, удовлетворяющие условию:""")
for i in res:
    print(i)
        
            
