import re
from collections import Counter

text = """
In computing, a regular expression, sometimes called 
a regex or regexp, is a sequence of characters that define a 
search pattern. Usually such patterns are used by string-searching 
algorithms for "find" or "find and replace" operations on strings, or 
for input validation. It is a technique that developed in theoretical 
computer science and formal language theory.

The concept arose in the 1950s when the American mathematician Stephen 
Kleene formalized the description of a regular language. The concept came 
into common use with Unix text-processing utilities. Different syntaxes 
for writing regular expressions have existed since the 1980s, one being 
the POSIX standard and another, widely used today, being the Perl syntax.

Regular expressions are used in search engines, search and replace dialogs 
of word processors and text editors, in text processing utilities such as 
sed and AWK and in lexical analysis. Many programming languages provide 
support for regular expressions in the language syntax (e.g., Perl, Python, 
Java, and C++), while some programming languages require the use of external 
libraries or modules to allow the use of regular expressions."""

text = re.sub(r'[^\w\s]','',text)  # убираем знаки препинания
text = text.lower()

word_counts = Counter(text.split())

for word, count in word_counts.most_common(10):
    print(word, count)