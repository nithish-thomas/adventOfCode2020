priority = {
    '+': 1,
    '-': 1,
    '*': 0,
    '/': 0,
}

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


def process_expression(tokens, start_inp, arr_len):
    res_stack = []
    op_stack = []
    start = start_inp
    res = tokens[start]
    start += 1
    if res == '(':
        res, start = process_expression(tokens, start, arr_len)
    res_stack.append(res)
    while start < arr_len:
        op = tokens[start]
        if op == ')':
            start += 1
            break
        b = tokens[start + 1]
        if b == '(':
            b, start = process_expression(tokens, start + 2, arr_len)
        else:
            start += 2

        while True:
            if len(op_stack) == 0 or priority[op_stack[-1]] < priority[op]:
                res_stack.append(b)
                op_stack.append(op)
                break
            else:
                operation = op_stack[-1]
                op_stack = op_stack[:-1]
                res = process_op(res_stack[-2], operation, res_stack[-1])
                res_stack = res_stack[:-2]
                res_stack.append(res)
    while len(op_stack) > 0:
        operation = op_stack[-1]
        op_stack = op_stack[:-1]
        res = process_op(res_stack[-2], operation, res_stack[-1])
        res_stack = res_stack[:-2]
        res_stack.append(res)

    return res_stack[0], start


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
