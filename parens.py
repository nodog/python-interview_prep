def remove_invalid_parens_iter(s: str) -> str:
    # for now it will always be open-close, everything else goes,
    # and there can be dangling open parens which should be removed
    removed_s = ''
    parens_closed = True
    for c in s:
        add_c = True
        if c == '(':
            if parens_closed == True:
                parens_closed = False
            else:
                add_c = False
        elif c == ')':
            if parens_closed == False:
                parens_closed = True
            else:
                add_c = False
        if add_c:
            removed_s += c

    # remove last unclosed open paren
    last_open = removed_s.rfind('(')
    last_close = removed_s.rfind(')')

    if last_open != -1:
        if last_close < last_open:
            # remove last open
            removed_s = removed_s[:last_open] + removed_s[last_open+1:]

    return removed_s


def test_paren_remove(s: str) -> str:
    print("----")
    print(f"input: {s}")
    print(f"output: {remove_invalid_parens_iter(s)}")


if __name__ == '__main__':
    print("---parens---")
    test_paren_remove("()()")
    test_paren_remove(")()")
    test_paren_remove(")()(")
    test_paren_remove("(())")
    test_paren_remove("(((((((() (((((()")
    test_paren_remove("()))))) ())))) (((((")
