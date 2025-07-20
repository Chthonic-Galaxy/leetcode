def plusOne(digits: list[int]) -> list[int]:
    if digits[-1] != 9:
        digits[-1] += 1
    else:
        if len(digits) == 1:
            digits = [1, 0]
        else:
            cur = len(digits) - 1
            sum_ = 1
            while cur >= 0 and sum_:
                if digits[cur] == 9 and sum_:
                    print(f"1: {digits=}, {cur=}, {sum_=}")
                    digits[cur] = 0
                    cur -= 1
                    print(f"1: {digits=}, {cur=}, {sum_=}")
                elif sum_:
                    print(f"2: {digits=}, {cur=}, {sum_=}")
                    digits[cur] += sum_
                    sum_ -= 1
                    print(f"2: {digits=}, {cur=}, {sum_=}")
            if sum_:
                digits = [1, *digits]
    return digits

print(plusOne([1,2,3]))
print(plusOne([4,3,2,1]))
print(plusOne([9]))
print(plusOne([9,9,9]))
print(plusOne([1,9,9,9]))
print(plusOne([2,1,9,9,9]))
print(plusOne([2,1,9,8,9]))