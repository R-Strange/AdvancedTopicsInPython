
def yell(text):
    return text.upper() + "!"


bark = yell

bark("hello")


functions = [bark, str.lower, str.capitalize]

for f in functions:
    print(f, f("hey there"))