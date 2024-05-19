from current_hw.ArrayStack import ArrayStack


class PostfixCalculator:
    def __init__(self):
        self.variables = {}

    def evaluate_arithmetic_expression(self, expression):
        stack = ArrayStack()
        tokens = expression.split()
        for token in tokens:
            if token.isdigit():
                stack.push(int(token))
            elif token in self.variables:
                stack.push(self.variables[token])
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = self.evaluate_operation(token, operand1, operand2)
                stack.push(result)
        return stack.pop()

    def evaluate_operation(self, operator, operand1, operand2):
        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            return operand1 / operand2

    def evaluate_assignment_expression(self, expression):
        variable_name, arithmetic_expression = expression.split('=')
        variable_name = variable_name.strip()
        value = self.evaluate_arithmetic_expression(arithmetic_expression.strip())
        self.variables[variable_name] = value
        return variable_name

    def evaluate_expression(self, expression):
        if '=' in expression:
            result = self.evaluate_assignment_expression(expression)
            return result
        else:
            return self.evaluate_arithmetic_expression(expression)

    def run(self):
        while True:
            user_input = input('--> ')
            if user_input == 'done()':
                return False
            else:
                result = self.evaluate_expression(user_input)
                print(result)


# Test the calculator
calculator = PostfixCalculator()
calculator.run()
