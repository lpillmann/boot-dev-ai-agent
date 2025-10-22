# calculator.py


class Calculator:
    def __init__(self):
        self.operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
        }
        self.precedence = {
            "+": 3,
            "-": 1,
            "*": 2,
            "/": 2,
        }

    def evaluate(self, expression):
        if not expression or expression.isspace():
            return None
        tokens = self._tokenize(expression)
        return self._evaluate_infix(tokens)

    def _tokenize(self, expression):
        # This function will handle tokenizing the expression, including parentheses and negative numbers
        # For now, it will just split by spaces, but it will be extended later.
        import re

        # This regex will split by spaces, but also keep parentheses as separate tokens.
        # It also handles negative numbers by looking for a minus sign followed by a digit, not preceded by another digit or closing parenthesis.
        tokens = re.findall(r"(\d+\.\d+|\d+|[-+*/()]|(?<!\d|\))-\d+)", expression)
        # Filter out empty strings that might result from the regex
        tokens = [token for token in tokens if token and not token.isspace()]

        # Adjust for unary minus:
        # If a '-' is at the beginning or after an operator or an opening parenthesis, it's a unary minus.
        # We'll merge it with the next number.
        i = 0
        while i < len(tokens):
            if tokens[i] == "-" and (
                i == 0 or tokens[i - 1] in self.operators or tokens[i - 1] == "("
            ):
                if i + 1 < len(tokens) and (
                    tokens[i + 1].isdigit()
                    or (
                        tokens[i + 1].startswith("-")
                        and len(tokens[i + 1]) > 1
                        and tokens[i + 1][1:].isdigit()
                    )
                ):
                    tokens[i] += tokens[i + 1]
                    tokens.pop(i + 1)
            i += 1
        return tokens

    def _evaluate_infix(self, tokens):
        values = []
        operators = []

        for token in tokens:
            if token == "(":
                operators.append(token)
            elif token == ")":
                while operators and operators[-1] != "(":
                    self._apply_operator(operators, values)
                if not operators or operators[-1] != "(":
                    raise ValueError("mismatched parentheses")
                operators.pop()  # Pop the "("
            elif token in self.operators:
                while (
                    operators
                    and operators[-1] in self.operators
                    and self.precedence[operators[-1]] >= self.precedence[token]
                ):
                    self._apply_operator(operators, values)
                operators.append(token)
            else:
                try:
                    values.append(float(token))
                except ValueError:
                    raise ValueError(f"invalid token: {token}")

        while operators:
            if operators[-1] == "(":
                raise ValueError("mismatched parentheses")
            self._apply_operator(operators, values)

        if len(values) != 1:
            raise ValueError("invalid expression")

        return values[0]

    def _apply_operator(self, operators, values):
        if not operators:
            return

        operator = operators.pop()
        if len(values) < 2:
            raise ValueError(f"not enough operands for operator {operator}")

        b = values.pop()
        a = values.pop()

        if operator == "/" and b == 0:
            raise ZeroDivisionError("division by zero")

        values.append(self.operators[operator](a, b))
