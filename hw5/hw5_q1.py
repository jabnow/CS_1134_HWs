import ArrayDeque
from ArrayStack import ArrayStack
import ArrayList
import ArrayQueue


# Question 1: implement a post-fix calculator interpreter

def postfix_calculator(expression=''):
    var_dict = {}

    def operators(oper, oper1, oper2):
        if oper == '+':
            return oper1 + oper2
        elif oper == '-':
            return oper1 - oper2
        elif oper == '*':
            return oper1 * oper2
        elif oper == '/':
            return oper1 / oper2

    def var_val(expression):
        var, maths = expression.split(' = ')
        variable = var.strip()
        val = do_maths(maths)
        var_dict[var] = val
        return var

    def do_maths(expression):
        stack = ArrayStack()
        var_lst = expression.split()
        for elem in var_lst:
            if elem.isdigit():
                stack.push(int(elem))
            elif elem in var_dict:
                stack.push(var_dict[elem])
            else:
                oper2 = stack.pop()
                oper1 = stack.pop()
                result = operators(elem, oper1, oper2)
                stack.push(result)
        return stack.pop()

    def solve(expression):
        if '=' in expression:
            return var_val(expression)
        else:
            return do_maths(expression)

    x = True
    while x:
        user_input = input('--> ')
        if user_input == 'done()':
            x = False
        else:
            result = solve(user_input)
            print(result)


# Test the calculator
postfix_calculator()
