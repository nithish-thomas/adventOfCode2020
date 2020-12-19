def process_op(res, op, b):
    res = int(res)
    b = int(b)
    # print(res, op , b)
    if op == '+':
        return res + b
    if op == '-':
        return res - b
    if op == '*':
        return res * b
    if op == '/':
        return res / b


def process_expression(tokens, start_inp, len):
    start = start_inp
    res = tokens[start]
    if res == '(':
        res, start = process_expression(tokens, start + 1, len)
    start += 1
    while start < len:
        op = tokens[start]
        if op == ')':
            return res, start
        b = tokens[start + 1]
        if b == '(':
            b, start = process_expression(tokens, start + 2, len)
            res = process_op(res, op, b)
            start += 1
            continue

        res = process_op(res, op, b)
        start += 2
    return res, start


def tokenize(expression: str):
    res = expression.replace(' ', '')
    return list(res)


def main():
    f = open("input.txt", "r")
    expression = f.read().split('\n')

    res = 0
    for expr in expression:
        tokens = tokenize(expr)
        i, index = process_expression(tokens, 0, len(tokens))
        print(i, index)
        res += i

    print(res)


if __name__ == "__main__":
    main()
