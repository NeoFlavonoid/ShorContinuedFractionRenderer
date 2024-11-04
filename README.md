# Continued Fraction Renderer

A Python tool for computing and visualizing continued fraction expansions of rational numbers, including their convergents and step-by-step calculations.

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

### Basic Usage

```python
from continued_fraction_renderer import ContinuedFractionRenderer

# Create a renderer instance with numerator and denominator
# Example: Represent 355/113 as a continued fraction
renderer = ContinuedFractionRenderer(355, 113)
renderer.display_continued_fraction()
```

### Using with Power-of-Two Denominators

The method you highlighted:
```python
a = ContinuedFractionRenderer(numerator, 2**17)
a.display_continued_fraction()
```

This specific usage creates a continued fraction representation where the denominator is 2¹⁷ (131,072). This is particularly useful when:
1. Analyzing rational approximations of numbers in binary computations
2. Finding convergents for numbers that need to be represented with fixed-point binary arithmetic
3. Studying how well a number can be approximated by fractions with power-of-two denominators

The power of 2 denominator is often used in computer science and digital signal processing where binary fractions are important.

## Output Format

The tool generates two types of output when `display_continued_fraction()` is called:

1. The continued fraction representation in a nested fraction format
2. The sequence of convergents (rational number approximations)

All output is rendered using LaTeX in Jupyter Notebook environments.

## Example
 - Can be found at `sample.py`

## Dependencies

- `sympy`: For rational number handling and continued fraction calculations
- `IPython`: For LaTeX display in Jupyter notebooks

## Notes

- The tool uses the `sympy` library's `continued_fraction_iterator` for accurate continued fraction computation
- All display output requires a Jupyter Notebook environment with LaTeX support
- For very large numbers, computation time may increase

## Contributing

Feel free to open issues or submit pull requests for improvements or bug fixes.
