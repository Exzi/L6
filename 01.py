text = input("Введи текст на русском языке: ")
vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
vowel_lt = [char for char in text if char in vowels]
print("Список гласных букв: ", vowel_lt)
print("Длина списка: ", len(vowel_lt))
