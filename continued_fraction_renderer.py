from sympy import Rational
from sympy.ntheory.continued_fraction import continued_fraction_iterator
from IPython.display import display, Math

class ContinuedFractionRenderer:
    def __init__(self, numerator, denominator):
        """
        Initializes the renderer with a numerator and a denominator.
        """
        self.numerator = numerator
        self.denominator = denominator
        self.continued_fraction = []
        self.cumulative_sums = []  # List to hold cumulative sums


    def continued_fraction_convergents(self, terms):
        # Initialize the starting values for p and q
        p_prev2, p_prev1 = 1, terms[0]  # p_-1 = 1, p_0 = a_0
        q_prev2, q_prev1 = 0, 1          # q_-1 = 0, q_0 = 1

        # Store the list of convergents as (numerator, denominator) pairs
        convergents = [(p_prev1, q_prev1)]

        # Compute successive convergents using recurrence relations
        for a in terms[1:]:
            # Calculate p_n and q_n
            p = a * p_prev1 + p_prev2
            q = a * q_prev1 + q_prev2

            # Store the convergent
            convergents.append((p, q))

            # Update previous values for the next iteration
            p_prev2, p_prev1 = p_prev1, p
            q_prev2, q_prev1 = q_prev1, q

        katex_output = r"\text{Convergents: } \displaystyle \begin{array}{c} "
        # Create fractions in LaTeX format
        katex_output += ", ".join([f"\\frac{{{p}}}{{{q}}}" for p, q in convergents])
        
        # Close the array environment
        katex_output += r" \end{array}"
        
        # Display the LaTeX code directly
        display(Math(katex_output))

    def compute_continued_fraction(self):
        """
        Computes the continued fraction representation for the provided fraction.
        Raises an error if the denominator is zero.
        """
        if self.denominator == 0:
            raise ValueError("The denominator cannot be zero.")

        fraction = Rational(self.numerator, self.denominator)  # Convert to a rational number
        self.continued_fraction = list(continued_fraction_iterator(fraction))  # Get continued fraction representation

    def display_continued_fraction(self):
        """
        Computes and displays the continued fraction in LaTeX format in Jupyter Notebook.
        """
        self.compute_continued_fraction()  # Compute the continued fraction
        latex_code = self.continued_fraction_to_latex()  # Get LaTeX string
        display(Math(latex_code))  # Display the LaTeX string

    def __init__(self, numerator, denominator):
        """
        Initializes the renderer with a numerator and a denominator.
        """
        self.numerator = numerator
        self.denominator = denominator
        self.continued_fraction = []

    def compute_continued_fraction(self):
        """
        Computes the continued fraction representation for the provided fraction.
        Raises an error if the denominator is zero.
        """
        if self.denominator == 0:
            raise ValueError("The denominator cannot be zero.")

        fraction = Rational(self.numerator, self.denominator)  # Convert to a rational number
        self.continued_fraction = list(continued_fraction_iterator(fraction))  # Get continued fraction representation

    def continued_fraction_to_latex(self):
        """
        Converts the computed continued fraction into a LaTeX-rendered string,
        including the numerator, denominator, and cumulative sums.
        
        Returns:
        - LaTeX string rendering the continued fraction
        """
        if not self.continued_fraction:
            return ""

        # Start with the innermost fraction (last element in the list)
        latex_code = str(self.continued_fraction[-1])
        # Build the continued fraction from innermost to outermost
        for value in reversed(self.continued_fraction[:-1]):
            # Calculate the next cumulative sum
            latex_code = r"{} + \cfrac{{1}}{{{}}}".format(value, latex_code)
        # print(self.continued_fraction)
        self.continued_fraction_convergents(self.continued_fraction)
        return (r"\text{Continued fraction for } \frac{" + str(self.numerator) + r"}{" + str(self.denominator) + r"} = " + latex_code)

    def display_continued_fraction(self):
        """
        Computes and displays the continued fraction in LaTeX format in Jupyter Notebook.
        """
        self.compute_continued_fraction()  # Compute the continued fraction
        latex_code = self.continued_fraction_to_latex()  # Get LaTeX string
        display(Math(latex_code))  # Display the LaTeX string