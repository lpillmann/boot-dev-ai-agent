from pkg.calculator import Calculator
from pkg.render import render

def main():
    calculator = Calculator()
    expression = "2 * 3 - 8 / 2 + 5"
    result = calculator.evaluate(expression)
    print(render(expression, result))


if __name__ == "__main__":
    main()
