class Fraction:
    """A fraction with a numerator and denominator and arithmetic operations.

    Fractions are always stored in proper form, without common factors in 
    numerator and denominator, and denominator >= 0.
    Since Fractions are stored in proper form, each value has a
    unique representation, e.g. 4/5, 24/30, and -20/-25 have the same
    internal representation.
    """
    
    def __init__(self, numerator, denominator=1):
        """Initialize a new fraction with the given numerator
           and denominator (default 1).
        """
        if (type(numerator) not in(int,float)):
            raise ValueError('Numerator must be a number')
        if (type(denominator) not in(int,float)):
            raise ValueError('Denominator must be a number')
        if numerator == 0 and denominator == 0:
            raise ValueError("can't divide 0 by 0")
        self.numerator = numerator
        self.denominator = denominator
        self.__make_denominator_integer()
        self.__make_numerator_integer()
        self.__reduce()
    def __str__(self):
        """Return string of fraction in the form of x/y"""
        if self.denominator ==1:
            return f'{self.numerator}'
        elif self.numerator ==0:
            return '0'
        else:
            return f'{self.numerator}/{self.denominator}'
    def __add__(self, frac):
        """Return the sum of this fraction and another fraction or number as a new fraction.
           Use the standard formula  a/b + c/d = (ad+bc)/(b*d)
        """
        if isinstance(frac,Fraction):
            numerator = ((self.numerator*frac.denominator)+(frac.numerator*self.denominator))
            denominator = (self.denominator*frac.denominator)
        elif type(frac) in(float,int):
            numerator = (frac*self.denominator) + self.numerator
            denominator = self.denominator
        else:
            raise ValueError('Fraction can only add with to int float or fractions')
        return Fraction(numerator,denominator)

    def __mul__(self,frac):
        """Return the product of this fraction and another fraction or number as a new fraction."""
        if isinstance(frac,Fraction):
            numerator = self.numerator*frac.numerator
            denominator = self.denominator*frac.denominator
        elif type(frac) in(float,int):
            numerator = self.numerator *frac
            denominator = self.denominator
        else:
            raise ValueError('Fraction can only multiply with to int float or fractions')
        return Fraction(numerator,denominator)
            
    #Optional have fun and overload other operators such as 
    # __sub__ for f-g
    # __gt__  for f > g
    # __neg__ for -f (negation)

    def __eq__(self, frac):
        """Two fractions are equal if they have the same value.
           Fractions are stored in proper form so the internal representation
           is unique (3/6 is same as 1/2).
        """

        if isinstance(frac,Fraction):
            return self.numerator == frac.numerator and self.denominator == frac.denominator
        elif type(frac) in(float,int):
            return self.numerator/self.denominator == frac
        else:
            raise ValueError('Fraction can only be compare to int float or fractions')
            
    def __make_denominator_integer(self):
        """If the denominator is a fraction, make it an integer"""
        while self.denominator % 1 !=0:
            self.denominator *=10
            self.numerator *=10
    def __make_numerator_integer(self):
        """If the numerator is a fraction, make it an integer"""
        while self.numerator % 1 !=0:
            self.denominator *=10
            self.numerator *=10
    def __reduce(self):
        """Reduce fraction to it's unreduceable form(done automatically)"""
        if self.denominator <0:
            self.denominator *= -1
            self.numerator *= -1
        divider = 2
        while divider <= abs(self.numerator) and divider <= abs(self.denominator):
            if self.numerator%divider==0 and self.denominator%divider==0:
                self.numerator /= divider
                self.denominator /= divider
                divider = 1
            divider += 1
        self.numerator = int(self.numerator)
        self.denominator = int(self.denominator)
