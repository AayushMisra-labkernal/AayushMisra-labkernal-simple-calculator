import math
from math import factorial, comb, perm, sqrt, exp, log, sin, cos, tan, pi

class ScientificCalculator:
    def __init__(self):
        self.last_result = 0

    def add(self, a, b):
        self.last_result = a + b
        return self.last_result

    def subtract(self, a, b):
        self.last_result = a - b
        return self.last_result

    def multiply(self, a, b):
        self.last_result = a * b
        return self.last_result

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        self.last_result = a / b
        return self.last_result

    def power(self, base, exponent):
        self.last_result = base ** exponent
        return self.last_result

    def square_root(self, x):
        if x < 0:
            return "Error: Cannot compute square root of negative number"
        self.last_result = sqrt(x)
        return self.last_result

    def factorial_calc(self, n):
        if n < 0:
            return "Error: Factorial not defined for negative numbers"
        self.last_result = factorial(int(n))
        return self.last_result

    def exponential(self, x):
        self.last_result = exp(x)
        return self.last_result

    def natural_log(self, x):
        if x <= 0:
            return "Error: Logarithm undefined for non-positive numbers"
        self.last_result = log(x)
        return self.last_result

    def log_base_10(self, x):
        if x <= 0:
            return "Error: Logarithm undefined for non-positive numbers"
        self.last_result = log(x, 10)
        return self.last_result

    def sine(self, angle_degrees):
        angle_radians = math.radians(angle_degrees)
        self.last_result = sin(angle_radians)
        return self.last_result

    def cosine(self, angle_degrees):
        angle_radians = math.radians(angle_degrees)
        self.last_result = cos(angle_radians)
        return self.last_result

    def tangent(self, angle_degrees):
        angle_radians = math.radians(angle_degrees)
        self.last_result = tan(angle_radians)
        return self.last_result

    def combination(self, n, r):
        if n < r or n < 0 or r < 0:
            return "Error: Invalid combination parameters"
        self.last_result = comb(int(n), int(r))
        return self.last_result

    def permutation(self, n, r):
        if n < r or n < 0 or r < 0:
            return "Error: Invalid permutation parameters"
        self.last_result = perm(int(n), int(r))
        return self.last_result

    def mean(self, numbers):
        if len(numbers) == 0:
            return "Error: Empty list"
        self.last_result = sum(numbers) / len(numbers)
        return self.last_result

    def variance(self, numbers):
        if len(numbers) == 0:
            return "Error: Empty list"
        mean_val = self.mean(numbers)
        variance_val = sum((x - mean_val) ** 2 for x in numbers) / len(numbers)
        self.last_result = variance_val
        return variance_val

    def standard_deviation(self, numbers):
        if len(numbers) == 0:
            return "Error: Empty list"
        var = self.variance(numbers)
        self.last_result = sqrt(var)
        return self.last_result

    def probability_binomial(self, n, k, p):
        prob = comb(int(n), int(k)) * (p ** k) * ((1 - p) ** (n - k))
        self.last_result = prob
        return prob

    def probability_poisson(self, lambda_param, k):
        prob = (exp(-lambda_param) * (lambda_param ** k)) / factorial(int(k))
        self.last_result = prob
        return prob

    def z_score(self, value, mean, std_dev):
        if std_dev == 0:
            return "Error: Standard deviation cannot be zero"
        z = (value - mean) / std_dev
        self.last_result = z
        return z

    def modulus(self, a, b):
        if b == 0:
            return "Error: Modulus by zero"
        self.last_result = a % b
        return self.last_result

    def get_last_result(self):
        return self.last_result


def display_menu():
    print("\n" + "="*60)
    print("AAYUSH MISRA - SCIENTIFIC CALCULATOR")
    print("="*60)
    print("\nBASIC OPERATIONS:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Modulus")
    print("\nSCIENTIFIC OPERATIONS:")
    print("7. Square Root")
    print("8. Factorial")
    print("9. Exponential (e^x)")
    print("10. Natural Logarithm (ln)")
    print("11. Logarithm Base 10 (log10)")
    print("12. Sine (degrees)")
    print("13. Cosine (degrees)")
    print("14. Tangent (degrees)")
    print("\nPROBABILITY & COMBINATORICS:")
    print("15. Combination (nCr)")
    print("16. Permutation (nPr)")
    print("17. Binomial Probability")
    print("18. Poisson Probability")
    print("\nSTATISTICS:")
    print("19. Mean (Average)")
    print("20. Variance")
    print("21. Standard Deviation")
    print("22. Z-Score")
    print("\n23. View Last Result")
    print("24. Exit")
    print("="*60)


def main():
    calc = ScientificCalculator()

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-24): ").strip()

        try:
            if choice == '1':
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print(f"Result: {calc.add(a, b)}")

            elif choice == '2':
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print(f"Result: {calc.subtract(a, b)}")

            elif choice == '3':
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print(f"Result: {calc.multiply(a, b)}")

            elif choice == '4':
                a = float(input("Enter dividend: "))
                b = float(input("Enter divisor: "))
                print(f"Result: {calc.divide(a, b)}")

            elif choice == '5':
                base = float(input("Enter base: "))
                exponent = float(input("Enter exponent: "))
                print(f"Result: {calc.power(base, exponent)}")

            elif choice == '6':
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print(f"Result: {calc.modulus(a, b)}")

            elif choice == '7':
                x = float(input("Enter number: "))
                print(f"Result: {calc.square_root(x)}")

            elif choice == '8':
                n = float(input("Enter number: "))
                print(f"Result: {calc.factorial_calc(n)}")

            elif choice == '9':
                x = float(input("Enter exponent: "))
                print(f"Result: {calc.exponential(x)}")

            elif choice == '10':
                x = float(input("Enter number: "))
                print(f"Result: {calc.natural_log(x)}")

            elif choice == '11':
                x = float(input("Enter number: "))
                print(f"Result: {calc.log_base_10(x)}")

            elif choice == '12':
                angle = float(input("Enter angle in degrees: "))
                print(f"Result: {calc.sine(angle)}")

            elif choice == '13':
                angle = float(input("Enter angle in degrees: "))
                print(f"Result: {calc.cosine(angle)}")

            elif choice == '14':
                angle = float(input("Enter angle in degrees: "))
                print(f"Result: {calc.tangent(angle)}")

            elif choice == '15':
                n = float(input("Enter n (total items): "))
                r = float(input("Enter r (items to choose): "))
                print(f"Result: {calc.combination(n, r)}")

            elif choice == '16':
                n = float(input("Enter n (total items): "))
                r = float(input("Enter r (items to arrange): "))
                print(f"Result: {calc.permutation(n, r)}")

            elif choice == '17':
                n = float(input("Enter number of trials: "))
                k = float(input("Enter number of successes: "))
                p = float(input("Enter probability of success (0-1): "))
                print(f"Result: {calc.probability_binomial(n, k, p)}")

            elif choice == '18':
                lambda_param = float(input("Enter lambda (average rate): "))
                k = float(input("Enter k (number of events): "))
                print(f"Result: {calc.probability_poisson(lambda_param, k)}")

            elif choice == '19':
                numbers = list(map(float, input("Enter numbers separated by comma: ").split(',')))
                print(f"Result: {calc.mean(numbers)}")

            elif choice == '20':
                numbers = list(map(float, input("Enter numbers separated by comma: ").split(',')))
                print(f"Result: {calc.variance(numbers)}")

            elif choice == '21':
                numbers = list(map(float, input("Enter numbers separated by comma: ").split(',')))
                print(f"Result: {calc.standard_deviation(numbers)}")

            elif choice == '22':
                value = float(input("Enter value: "))
                mean = float(input("Enter mean: "))
                std_dev = float(input("Enter standard deviation: "))
                print(f"Result: {calc.z_score(value, mean, std_dev)}")

            elif choice == '23':
                print(f"Last Result: {calc.get_last_result()}")

            elif choice == '24':
                print("Thank you for using Aayush Misra's Scientific Calculator!")
                break

            else:
                print("Invalid choice! Please try again.")

        except ValueError:
            print("Invalid input! Please enter valid numbers.")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()