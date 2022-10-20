'''
1) RE patterns compiles into a series of bytecodes which are then executed by matching engine written in C
2) patterns and strings to be searched can be Unicode strings (str) as well as 8-bit strings (bytes) you cannot match a Unicode string with a byte pattern or vice-versa
3) Here is complete list of metacharacters: don't match themselves but changing meaning of RE . ^ $ * + ? { } [ ] \ | ( )
    a) '[' and ']'  are used for specifying character class: set of characters you wish to match. e.g: [abc] or [a-c] will match any of the characters a, b, or c metacharacets (except '\') are not active inside classes. eg: [akm$] will match any of the characets a, k, m, $
    b) '^' as the first character of class are used for complementing the class. e.g: [^5] will match any character except 5 but [5^] will match any of the characters 5, ^
    c) '\' most important: use as first character
        i) remove special meaning of metacharacters. eg: \[ will match [ character in string
        ii) Some of special sequences beginning with \ represent predefined sets of characters
            A) \d   matches any decimal digit               [0-9]
            B) \D   matches any non-digit character         [^0-9]
            C) \s   mathces any whitespace character        [\t\n\r\f\v]
            D) \S   matches any non-whitespace character    [^\t\n\r\f\v]
            E) \w   matches any alphanumeric character      [a-zA-Z0-9_]
            F) \W   matches any non alphanumeric character  [^a-zA-Z0-9_]
    d) . matches anything except a newline character. Alternate mode re.DOTALL where it will match any character
4) Repeating things: specify that portions of RE must be repeated a certain number of times
    a) * (greedy). eg: ca*t will match ct (0 match), cat (1 match), caat (2 match) and so on
    b) + as same as * but + requires at least one occurence. eg: ca+t will match cat (1 match), caat (2 match) and so on
    c) ? will match either one or zero times. eg: ca?t will match ct (0 match) or cat (1 match).
    d) {m, n} m and n are int. there must be at least m and at most n repitions eg: a/{1, 3}b will match a/b, a//b and a///b. It won't match ab (no slashes) or a////b (4 slashes). Omitting m is interpreted as a lower limit of 0, while omitting n results in an upper bound of infinity. {0,} is the same as *, {1,} is equivalent to +, and {0,1} is the same as ?. It’s better to use *, +, or ?
5) Regular expressions are compiled into pattern objects using re.compile(RE). it also accepts optional flag argument like re.compile(RE, re.IGNORECASE)
6) To match exact '\section' you have to write \\section in RE
7) RE will often written raw string notation. It helps to match a literal backslash and other metacharacters without difficulty
8) Once you have a pattern object. you can call several methods on it like:
    a) match()      Determine if the RE matches at the beginning of the string.
    b) search()     Scan through a string, looking for any location where this RE matches.
    c) findall()    Find all substrings where the RE matches, and returns them as a list.
    d) finditer()   Find all substrings where the RE matches, and returns them as an iterator.
9) match() & search() function return match object for info about the match string. match obj consist following functions:
    a) group()  Return String matched by RE
    b) start()  Return starting position of the match
    c) end()    Return the ending position of the match
    d) span()   Return a tuple containing the (start, end) positions of the match
'''


import re

p = re.compile("[a-z]+") # pattern object
m = p.match("tempo") # match object
print(m.group())
print(m.start())
print(m.end())
print(m.span())
print(p.match('::: message')) # return None because match() only matches at the beginnnig of string
m = p.search('::: message')
print(m.group())
print(m.span())
p = re.compile(r'\d+')
print(p.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping'))
iterator = p.finditer('12 drummers drumming, 11 pipers piping, 10 lords a-leaping')
print(iterator)
for match in iterator:
    print(match.group(), match.span())
