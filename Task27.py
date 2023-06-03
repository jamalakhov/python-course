# 27. Пользователь вводит текст(строка).
# Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов.
# Определите, сколько различных слов содержится в этом тексте.

# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells

# Output: 15

def count_unique_words(text):
    words = text.split()
    unique_words = set(words)
    return len(unique_words)

input_text = input("Введите текст: ")
unique_word_count = count_unique_words(input_text)

print(unique_word_count)