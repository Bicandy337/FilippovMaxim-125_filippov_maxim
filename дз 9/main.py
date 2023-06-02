def alternating_case(string):
    result = ""
    is_upper = False
    for char in string:
        if char.isalpha():
            if is_upper:
                result += char.upper()
                is_upper = False
            else:
                result += char.lower()
                is_upper = True
        else:
            result += char
    return result

string = "Hello World! How are you today?"
result = alternating_case(string)
print(result)