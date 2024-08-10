def solution(code):
    mode = False
    s = ""
    for i in range(0, len(code)):
        if code[i] == "1":
            mode = not mode 
            continue
        
        if mode and i % 2 != 0:
            s += code[i]
        elif not mode and i % 2 == 0:
            s += code[i]            
    if not s:
        return "EMPTY"
    return s