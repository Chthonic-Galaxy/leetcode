def zigzag_formatter(s: str, numRows: int) -> str:
    if numRows == 1 or len(s) == numRows:
        return s
    
    o = ""
    signal = ""
    for i in range(0, numRows):
        if i == 0:
            while True:
                if i <= len(s)-1:
                    o += s[i]
                    i += 2 * (numRows-1)
                else:
                    break
        elif i != 0 and i != numRows-1:
            o_i = i
            signal = ""
            while True:
                for su in [(numRows-1-o_i)*2, (2 * (numRows-1)) - (numRows-1-o_i)*2]:
                    if i <= len(s)-1:
                        o += s[i]
                        i += su
                    else:
                        signal = "exit"
                        break
                if signal == "exit":
                    break
        else:
            while True:
                if i <= len(s)-1:
                    o += s[i]
                    i += 2 * (numRows-1)
                else:
                    break
    return o

print(zigzag_formatter("HOUSEISTHEWORKBENCH", 6))

print("\n---\n")
print(zigzag_formatter("AVA", 2))