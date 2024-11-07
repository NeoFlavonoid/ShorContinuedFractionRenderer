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
        self.convergents = []

    def compute_continued_fraction_convergents(self, terms):
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
        self.convergents = convergents

    def compute_continued_fraction(self):
        """
        Computes the continued fraction representation for the provided fraction.
        Raises an error if the denominator is zero.
        """
        if self.denominator == 0:
            raise ValueError("The denominator cannot be zero.")

        fraction = Rational(self.numerator, self.denominator)  # Convert to a rational number
        self.continued_fraction = list(continued_fraction_iterator(fraction))  # Get continued fraction representation

    def display_continued_fraction(self, cf):
        """
        Converts the computed continued fraction into a LaTeX-rendered string,
        including the numerator, denominator, and cumulative sums.
        
        Returns:
        - LaTeX string rendering the continued fraction
        """
        if not cf:
            return ""

        # Start with the innermost fraction (last element in the list)
        latex_code = str(cf[-1])
        # Build the continued fraction from innermost to outermost
        for value in reversed(cf[:-1]):
            # Calculate the next cumulative sum
            latex_code = r"{} + \cfrac{{1}}{{{}}}".format(value, latex_code)
        display(Math((r"\text{Continued fraction for } \frac{" + str(self.numerator) + r"}{" + str(self.denominator) + r"} = " + latex_code)))

    def display_convergents(self, cnv):
        """
        Converts the list of convergents into a LaTeX-rendered string and displays it.

        Parameters:
        - convergents: A list of tuples, where each tuple contains a numerator and denominator
        for the convergent fraction (e.g., [(p1, q1), (p2, q2), ...])

        Returns:
        - None: This method directly displays the convergents in LaTeX format.
        """
        # Initialize the LaTeX output string
        katex_output = r"\text{Convergents: } \displaystyle \begin{array}{c} "

        # Create LaTeX-formatted fractions for each convergent
        katex_output += ", ".join([f"\\frac{{{p}}}{{{q}}}" for p, q in cnv])
        
        # Close the array environment
        katex_output += r" \end{array}"

        # Display the LaTeX code using Math (to render with KaTeX)
        display(Math(katex_output))

    def compute(self):
        """
        Computes and displays the continued fraction in LaTeX format in Jupyter Notebook.
        """
        self.compute_continued_fraction()  # Compute the continued fraction
        self.compute_continued_fraction_convergents(self.continued_fraction) # Compute the convergents
        return self.continued_fraction, self.convergents