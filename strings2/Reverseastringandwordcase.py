s = "Hello World"
news     = ""

words_list = s.split(" ")

for word in words_list:
    #reversed_word = word[::-1]
    reversed_word = "".join(reversed(word))
    swapped_case = reversed_word.swapcase()
    news += swapped_case + " "

news = news.rstrip()
print(news)