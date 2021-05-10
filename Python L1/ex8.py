str1 = """Python is a widely used high-level programming language for general-purpose programming, created by Guido van Rossum and first released in 1991. An interpreted language, Python has a design philosophy which emphasizes code readability (notably using whitespace indentation to delimit code blocks rather than curly braces or keywords), and a syntax which allows programmers to express concepts in fewer lines of code than possible in languages such as C++ or Java. The language provides constructs intended to enable writing clear programs on both a small and large scale .Python features a dynamic type system and automatic memory management and supports multiple programming paradigms, including object-oriented, imperative, functional programming, and procedural styles. It has a large and comprehensive standard library. Python interpreters are available for many operating systems, allowing Python code to run on a wide variety of systems. CPython, the reference implementation of Python, is open source software and has a community-based development model, as do nearly all of its variant implementations. CPython is managed by the non-profit Python Software Foundation."""


def word_dictionary(x):
    dictionary = {}
    wordList = x.split()
    length = len(wordList)
    for index, word in enumerate(wordList):
        if word in dictionary:
            continue
        tmpList = []
        for i in range(index, length):
            if index == length - 1:
                break
            if word == wordList[i]:
                nextWord = wordList[i + 1]
                tmpList.append(nextWord)

        dictionary[word] = tmpList
    return dictionary


# print(word_dictionary(str1)) a. Dictionary of all the words with thier values what will be followed by


# predict for a word whatwill be followed by


def predict(x, word):
    wordDictionary = word_dictionary(x)
    print(
        f"{word} is followed by the list of words",
        wordDictionary[word],
    )


predict(str1, "Python")
