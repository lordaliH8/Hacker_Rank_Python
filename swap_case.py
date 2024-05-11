def swap_case(s):
    tmp = ""
    for i in range(len(s)):
        if s[i].isupper() == True:
            tmp += s[i].lower()
        else:
            tmp += s[i].upper()
    return tmp
print(swap_case("AlI"))