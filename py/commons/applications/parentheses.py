# coding=utf-8
from commons.structs.stacks import ArrayStack


def is_matched(expr: str):
    lefty = '([{'
    righty = ')]}'

    stack = ArrayStack()
    for c in expr:
        if c in lefty:
            stack.push(c)
        elif c in righty:
            if stack.is_empty():
                return False
            if righty.index(c) != lefty.index(stack.pop()):
                return False
    return stack.is_empty()


if __name__ == '__main__':
    assert is_matched('')
    assert is_matched('()(()){([()])}')
    assert is_matched('((()(()){([()])}))')
    assert is_matched('[(5+x)–(y+z)]')
    assert not is_matched(')(()){([()])}')
    assert not is_matched('({[])}')
    assert not is_matched(')')
