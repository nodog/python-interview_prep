def remove_invalid_parens(s: str) -> str:
    # for now it will always be open-close, everything else goes,
    # and there will be no dangling open parens
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

    return removed_s


def test_paren_remove(s: str) -> str:
    print("----")
    print(f"input: {s}")
    print(f"output: {remove_invalid_parens(s)}")


if __name__ == '__main__':
    print("---parens---")
    test_paren_remove("()()")
    test_paren_remove(")()")
    test_paren_remove("(())")
    test_paren_remove("(((((((() (((((()")
