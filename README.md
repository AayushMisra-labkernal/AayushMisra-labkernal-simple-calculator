# Scientific Calculator by Aayush Misra

A comprehensive Python-based scientific calculator designed to help math and statistics students solve complex probability, statistics, and scientific computation problems with ease.

## Overview

This scientific calculator is built to assist students in understanding and solving mathematical problems related to:
- **Probability Theory** - Binomial and Poisson distributions
- **Statistics** - Mean, variance, standard deviation, Z-scores
- **Scientific Calculations** - Exponential functions, logarithms, trigonometry
- **Combinatorics** - Combinations and permutations

## Features

### 1. **Basic Arithmetic Operations**
- Addition, Subtraction, Multiplication, Division
- Modulus (remainder operation)
- Power operations (exponentiation)

### 2. **Scientific Functions**
- Square Root
- Factorial
- Exponential (e^x)
- Natural Logarithm (ln)
- Logarithm Base 10 (log₁₀)
- Trigonometric Functions: Sine, Cosine, Tangent (input in degrees)

### 3. **Probability & Combinatorics**
- **Combinations (nCr)**: Calculate ways to choose r items from n items
- **Permutations (nPr)**: Calculate ways to arrange r items from n items
- **Binomial Probability**: P(X=k) = C(n,k) × p^k × (1-p)^(n-k)
- **Poisson Probability**: P(X=k) = (e^(-λ) × λ^k) / k!

### 4. **Statistics Functions**
- **Mean (Average)**: Calculate average of a dataset
- **Variance**: Measure data spread
- **Standard Deviation**: Square root of variance
- **Z-Score**: Standardized score for hypothesis testing

### 5. **Advanced Exponential Operations**
- Full support for exponential growth/decay calculations
- Natural logarithm for inverse exponential operations
- Useful for modeling exponential phenomena

## Installation

1. Clone the repository:
```bash
git clone https://github.com/AayushMisra-labkernal/AayushMisra-labkernal-simple-calculator.git
cd AayushMisra-labkernal-simple-calculator
```

2. Ensure Python 3.7+ is installed on your system.

## Usage

Run the calculator:
```bash
python calculator.py
```

The program presents an interactive menu with all available operations. Simply:
1. Select your desired operation by entering the corresponding number
2. Enter the required values
3. View the result
4. Continue with more calculations or exit

### Example Usage

**Calculate Binomial Probability:**
```
Enter your choice: 17
Enter number of trials: 10
Enter number of successes: 5
Enter probability of success (0-1): 0.5
Result: 0.24609375
```

**Calculate Mean and Standard Deviation:**
```
Enter your choice: 19
Enter numbers separated by comma: 10,20,30,40,50
Result: 30.0

Enter your choice: 21
Enter numbers separated by comma: 10,20,30,40,50
Result: 14.142135623730951
```

**Calculate Z-Score:**
```
Enter your choice: 22
Enter value: 85
Enter mean: 75
Enter standard deviation: 5
Result: 2.0
```

## Who Should Use This?

This calculator is perfect for:
- **Math Students**: Master probability and combinatorics concepts
- **Statistics Students**: Learn statistical calculations and hypothesis testing
- **Engineering Students**: Perform scientific computations
- **Data Science Learners**: Understand statistical foundations
- **Science Students**: Solve exponential growth/decay problems

## Key Concepts Explained

### Probability
- **Binomial Distribution**: Models number of successes in n independent trials
- **Poisson Distribution**: Models number of events occurring in a fixed interval
- **Z-Score**: Tells how many standard deviations away from the mean a value is

### Statistics
- **Mean**: Average value of a dataset
- **Variance**: Average of squared differences from the mean
- **Standard Deviation**: Square root of variance; measures spread of data

### Exponential Functions
- Used in compound interest, population growth, radioactive decay
- Formula: y = a × e^(bx)
- Essential for natural phenomena modeling

## Technical Details

- **Language**: Python 3.7+
- **Dependencies**: Standard library (math module)
- **Creator**: Aayush Misra
- **Purpose**: Educational tool for mathematics and statistics

## Future Enhancements

- GUI interface using Tkinter
- Data visualization with matplotlib
- Normal distribution calculations
- Chi-square test functions
- Linear regression analysis
- Matrix operations

## Contributing

Feel free to fork this repository and submit pull requests for improvements or new features.

## License

This project is open source and available for educational purposes.

---

**Made with ❤️ by Aayush Misra to help students excel in mathematics and statistics!**