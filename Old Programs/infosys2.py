def bracket_pattern(input_str):
    q = 0
    w = 0
    if (input_str[0] == ")"):
        return(False)
    else:
        for i in range(len(input_str)):
            if (input_str[i] == "("):
                q = q + 1
            elif (input_str[i] == ")"):
                w = w + 1
        if (q == w):
            return(True)
        else:
            return(False)
input_str = ")()()"
print(bracket_pattern(input_str))