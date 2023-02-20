with open("books/frankenstein.txt") as f:
    file_contents = f.read()

#print(file_contents)

def count_words(content):
    words = content.split()
    return len(words)

#print(count_words(file_contents))
total_words = count_words(file_contents)

def count_letters(content):
    contentLower = content.lower()
    contentDict = {}
    characters = list(contentLower)
    for c in characters:
        if c not in contentDict:
            contentDict[c] = 1
        else:
            contentDict[c] += 1
    return contentDict

#print(count_letters(file_contents))
dictionary_chars = count_letters(file_contents)


print("-- Start report of Frankenstein")
print(f"{total_words} words found in the document\n")
for c in sorted(dictionary_chars, key= dictionary_chars.get, reverse=True):
    if c.isalpha():
        print(f"The '{c}' character was found {dictionary_chars[c]} times")

print("-- End Report --") 