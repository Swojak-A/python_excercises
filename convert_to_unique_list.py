# assert unique_in_order("AAAABBBCCDAABBB") == ["A", "B", "C", "D", "A", "B"]
# assert unique_in_order("ABBCcAD") == ["A", "B", "C", "c", "A", "D"]
# assert unique_in_order([1, 2, 2, 3, 3]) == [1, 2, 3]


def unique_in_order(arg):
    ret = []
    for e in arg:
        if ret:
            if e != ret[-1]:
                ret.append(e)
        else:
            ret.append(e)
    return ret


assert unique_in_order("AAAABBBCCDAABBB") == ["A", "B", "C", "D", "A", "B"]
assert unique_in_order("ABBCcAD") == ["A", "B", "C", "c", "A", "D"]
assert unique_in_order([1, 2, 2, 3, 3]) == [1, 2, 3]
