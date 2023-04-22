# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, слова разделены одним 
# или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

input_str = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
input_str = input_str.replace('.', "'")
words = set(input_str.split())
print("Количество различных слов:", len(words))

# new_str = 'I\'m sure.'   '\' сохраняет пунктуацию
# print(new_str)