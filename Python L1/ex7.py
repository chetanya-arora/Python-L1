import re

str1 = """Python is a widely used high-level programming language for general-purpose programming, created by Guido van Rossum and first released in 1991. An interpreted language, Python has a design philosophy which emphasizes code readability (notably using whitespace indentation to delimit code blocks rather than curly braces or keywords), and a syntax which allows programmers to express concepts in fewer lines of code than possible in languages such as C++ or Java. The language provides constructs intended to enable writing clear programs on both a small and large scale .Python features a dynamic type system and automatic memory management and supports multiple programming paradigms, including object-oriented, imperative, functional programming, and procedural styles. It has a large and comprehensive standard library. Python interpreters are available for many operating systems, allowing Python code to run on a wide variety of systems. CPython, the reference implementation of Python, is open source software and has a community-based development model, as do nearly all of its variant implementations. CPython is managed by the non-profit Python Software Foundation."""

str1 = re.sub(
    r"[^\w\s]", "", str1
)  # replacing all the punctaution with empty string keeping only words
array_string = str1.split(" ")


def values(item):
    return item[1]


def dictionary_builder(x):
    dictionary = {}
    for word in x:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    return dict(sorted(dictionary.items(), key=values))


frequency_dictionary = dictionary_builder(array_string)

print(frequency_dictionary)  # a. the Dictionary of frequency of the words

# b. Print top five word frequencies
top_five_frequencies = list(dictionary_builder(array_string).keys())[-6:-1][::-1]
for item in top_five_frequencies:
    print(f"{item}:{frequency_dictionary[item]}")