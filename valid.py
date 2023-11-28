def isValid(s: str):
    for i in range(len(s)):
        if i + 1 < len(s) and s[i] == "(" and s[i + 1] == ")":
            return 'true'
            break
        elif s[i] == "[" and s[i + 1] == "]":
            return 'true'
            break
        elif s[i] == "{" and s[i + 1] == "}":
            return 'true'
            break
        else:
            return 'false'
            break


a = str(input())
print(isValid(a))
