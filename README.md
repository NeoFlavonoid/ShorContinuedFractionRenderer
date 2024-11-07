# Continued Fraction Renderer for Shor's Algorithm

A specialized Python tool for analyzing the period-finding component of Shor's algorithm using continued fraction expansion. This tool helps find the period r from quantum measurement outcomes by analyzing probability peaks.

## Purpose

In Shor's algorithm, after quantum measurement, we need to:
 - Find peaks in the probability distribution
 - Convert these peaks (matching indices) into rational approximations to find the period r
 - Use continued fractions to find the best approximation with small denominators

## Installation

This package requires Python 3.6 or higher. Install the required dependencies using pip:

```bash
pip install sympy
pip install ipython
```

## Features

- Converts rational numbers to their continued fraction representation
- Generates LaTeX-formatted visualizations of continued fractions
- Calculates and displays convergents
- Supports Jupyter Notebook integration for beautiful mathematical rendering

## Usage

 - Can be found at `sample.ipynb`

## Output Format

 - The compute() method of ContinuedFractionRenderer calculates both the continued fraction and the convergents.
 - The display_continued_fraction() method is used to render the continued fraction in LaTeX format.
 - The display_convergents() method is used to render the sequence of convergents in LaTeX format.

All output is rendered using LaTeX in Jupyter Notebook environments.
![sample](https://github.com/user-attachments/assets/602e9150-8102-429b-98f5-ca5cdd0b37b7)

## Dependencies

- `sympy`: For rational number handling and continued fraction calculations
- `IPython`: For LaTeX display in Jupyter notebooks

## Notes

- The tool uses the `sympy` library's `continued_fraction_iterator` for accurate continued fraction computation
- All display output requires a Jupyter Notebook environment with LaTeX support
- For very large numbers, computation time may increase

## Contributing

Feel free to open issues or submit pull requests for improvements or bug fixes.
