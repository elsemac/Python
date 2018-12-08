# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[10])


# Вывести количество букв а в слове
word = 'Архангельск'
print(len(word))


# Вывести количество гласных букв в слове
word = 'Архангельск'
count_word = 0
if 'А' or 'a' in word:
    count_word = count_word + 1
if 'О' or 'о' in word:
    count_word = count_word + 1
if 'Э' or 'э' in word:
    count_word = count_word + 1
if 'И' or 'и' in word:
    count_word = count_word + 1
if 'У' or 'у' in word:
    count_word = count_word + 1
if 'Ы' or 'ы' in word:
    count_word = count_word + 1
if 'Е' or 'е' in word:
    count_word = count_word + 1
if 'Ё' or 'ё' in word:
    count_word = count_word + 1
if 'Ю' or 'ю' in word:
    count_word = count_word + 1
if 'Я' or 'я' in word:
    count_word = count_word + 1   
print(count_word) 


word = 'Архангельск'
word = word.lower()
vowel_list = set(['а','о','э','и','у','ы','е','ё','ю','я'])
vowels = 0
for set in vowel_list:
    if set in word:
        vowels += word.count(set)
print(vowels)




# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
split = (sentence.split())
for letter in split:
    print(letter[0])



# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'

letters_in_sentence = len(sentence.replace(' ', ''))
words_in_sentence = len(sentence.split())
answer = letters_in_sentence / words_in_sentence
print(answer)



# ???