def to_weird_case_word(string):
    return "".join(c.upper() if i%2 == 0 else c for i, c in enumerate(string.lower()))
    
def to_weird_case(string):
    return " ".join(to_weird_case_word(str) for str in string.split())
    
    
or


def to_weird_case(string):
    index = 0
    new_string = ''
    for word in string:
        if word == ' ':
            index = -1
            new_string += word
        elif index % 2 == 0:
            new_string += word.upper()
        else:
            new_string += word.lower()
        index += 1
    return new_string
