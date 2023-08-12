phrase = input("Введите строку для проверки рифмы:")
phrase = phrase.split(" ")

def rhythm(phrase):
    count = 0
    list = []
    for word in phrase:
        for letter in word:
            if letter in "аеёиоуыэюя":
                count += 1
        list.append(count)
        count = 0
    return "Парам пам-пам" if len(set(list)) == 1 else "Пам парам"

print(rhythm(phrase))
