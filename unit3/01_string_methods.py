s = input("Enter a sentence: ")

print("Length:", len(s))
print("Uppercase:", s.upper())
print("Lowercase:", s.lower())
print("After removing spaces:", s.strip())

old = input("Enter word to replace: ")
new = input("Enter new word: ")
print("After replacement:", s.replace(old, new))

ch = input("Enter character to count: ")
print("Character count:", s.count(ch))

sub = input("Enter substring: ")
print("Starts with:", s.startswith(sub))
print("Ends with:", s.endswith(sub))

s1 = input("Enter another string: ")
print("Concatenation:", s + " " + s1)
print("Repetition:", s * 2)
print("Membership:", sub in s)
