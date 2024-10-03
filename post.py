# A+B*(C+D/E)-F


def postfix(expression_string):

    # expression = input("Enter the expression: ")

    # syntactical correction of the expression

    expression = []
    temp = ''
    for i in range(0, len(expression_string)):
        if (temp+expression_string[i]).isdigit():
            temp = temp+expression_string[i]
        else:
            if temp!='':
                expression.append(temp)
                temp = ''
            expression.append(expression_string[i])
    if temp!='':
        expression.append(temp)
            

    print(expression)

    exp = []
    for i in range(0, len(expression)):
        if expression[i] == '(':
            if exp[len(exp) - 1] not in ['+', '-', '*', '/']:
                exp.append('*')
                exp.append('(')
            else:
                exp.append('(')
        elif expression[i] == ')':
            try:
                if expression[i + 1] not in ['+', '-', '*', '/']:
                    exp.append(')')
                    exp.append('*')
            except IndexError:
                exp.append(')')
        else:
            exp.append(expression[i])

    print(exp)
    stack = []
    postfix = []

    op1 = ['+', '-']
    op2 = ['*', '/']

    for i in exp:

        # print("stack",stack)
        # print("postfix",postfix)

        if i in op1:
            while len(stack) > 0 and (stack[len(stack) - 1] in op1
                    or stack[len(stack) - 1] in op2):
                postfix.append(stack.pop())
            stack.append(i)
        elif i in op2:
            while len(stack) > 0 and stack[len(stack) - 1] in op2:
                postfix.append(stack.pop())
            stack.append(i)
        elif i == '(':
            stack.append(i)
        elif i == ')':
            while stack[len(stack) - 1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            postfix.append(i)

    while len(stack) > 0:
        postfix.append(stack.pop())

    return postfix


def calculate(expression):
    exp = postfix(expression)
    out = []
    op = ['+', '-', '*', '/']
    for i in range(0, len(exp)):

        # print(out)

        if exp[i] == '+':
            out.append(out.pop() + out.pop())
        elif exp[i] == '-':
            temp = out[len(out) - 2] - out[len(out) - 1]
            out.pop()
            out.pop()
            out.append(temp)
        elif exp[i] == '*':
            out.append(out.pop() * out.pop())
        elif exp[i] == '/':
            temp = out[len(out) - 2] / out[len(out) - 1]
            out.pop()
            out.pop()
            out.append(temp)
        else:
            out.append(int(exp[i]))

    # print(exp)

    return out[0]


# calculate("5(6)")
#postfix(input("Expression: "))
