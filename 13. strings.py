word = " spontaneous, emission "
another_word = " from reactor "

# individual char
print(word[4])

# slicing
print(word[2:6])
print(word[:6])
print(word[6:])

# modifying
print(word.upper())
print(word.lower())

# removing white space from front
print(word.strip())

# replacing
print(word.replace("emission", "blast"))

# splitting
print(word.split(","))

# concatenation
print(word + another_word)

# formatting
count = 19
fruit = "apples"
statement = "i have {1} basket of {0}"

# line 34 statement will print count then fruit, when no index is given
# but when index is provided in {} then it will take accordingly
print(statement.format(fruit, count))

# escaping ""
quote = "\"this is, how it works\""
print(quote)
