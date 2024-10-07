def balanced_bracket(string):
    count = 0
    for bracket in string:
        if bracket == "[":
            count += 1
        elif bracket == "]":
            count -= 1
        
        if count < 0:
            break

    return count == 0

print(balanced_bracket("[]"))

print(balanced_bracket("[]]"))

