def zigzag_formatter(s: str, numRows: int) -> str:
    s_l = len(s)
    columns = 1
    while True:
        s_l -= numRows
        if s_l <= 0: break
        columns += 1
        for _ in range(numRows-2 if numRows-2 >= 0 else 0):
            s_l -= 1
            if s_l <= 0: break
            columns += 1


    matrix = [[0 for _ in range(columns)] for _ in range(numRows)]
    r, c = -1, 0
    state = "straight"
    for l in s:
        if r == 0: state = "straight"
        if r == numRows-1: state = "zigzag"
        if state == "straight":
            r += 1
            matrix[r][c] = l
        else:
            r -= 1
            c += 1
            matrix[r][c] = l
            
    output = ""
    for r in matrix:
        for c in r:
            if c != 0:
                output += c
    return output

print(zigzag_formatter("HOUSEISTHEWORKBENCH", 6))

print("\n---\n")
print(zigzag_formatter("AVA", 2))