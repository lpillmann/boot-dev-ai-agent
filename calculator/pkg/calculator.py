import re


class Calculator:
    def __init__(self):
        self.operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
        }
        self.precedence = {
            "+": 1,
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
        raw_tokens = re.findall(r"(\d+\.\d+|\d+|[+\-*/()])", expression)
        raw_tokens = [token for token in raw_tokens if token.strip()]

        processed_tokens = []
        i = 0
        while i < len(raw_tokens):
            token = raw_tokens[i]
            is_unary_minus_candidate = (
                token == '-' and
                (i == 0 or 
                 (processed_tokens and (processed_tokens[-1] in self.operators or processed_tokens[-1] == '(')))
            )

            if is_unary_minus_candidate and i + 1 < len(raw_tokens) and re.match(r'^\d+(\.\d+)?$', raw_tokens[i+1]):
                processed_tokens.append(token + raw_tokens[i+1])
                i += 1 
            else:
                processed_tokens.append(token)
            i += 1
        
        return processed_tokens

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
