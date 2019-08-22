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
           and denominator (default 1). If the denominator and numerator is 0
           the value is 0 and if it's is not zero, it will determine infinity size(infinity can be negative).
        """
        if (type(numerator) not in(int,float)):
            raise ValueError('Numerator must be a number')
        if (type(denominator) not in(int,float)):
            raise ValueError('Denominator must be a number')
        if denominator == 0:
            if numerator == 0:
                self.numerator = 0
                self.denominator = 1
                self.inf_size = 0
            else:
                self.numerator = 0
                self.denominator = 0
                self.inf_size = numerator
        else:
            self.inf_size = 0
            self.numerator = numerator
            self.denominator = denominator
        self.__make_denominator_integer()
        self.__make_numerator_integer()
        self.__reduce()
    def __str__(self):
        """Return string of fraction in the form of x/y"""
        if self.denominator ==1:
            return f'{self.numerator}'
        elif self.denominator == 0 and self.numerator ==0:
            if self.inf_size > 0:
                return f'Infinity with size of {self.inf_size}'
            else:
                return f'Negative infinity with size of {-self.inf_size}'
        elif self.numerator ==0:
            return '0'
        else:
            return f'{self.numerator}/{self.denominator}'
    def __add__(self, frac):
        """Return the sum of this fraction and another fraction or number as a new fraction if both infinity size = 0(int and float infinity size = 0)
           if 1 of the fraction's infinity size isn't 0, return the one with bigger absolute infinity value unless, if it is the negative of the same infinity size
           return 0
        """
        if isinstance(frac,Fraction):
            if self.inf_size !=0 or frac.inf_size != 0:
                if self.inf_size == -frac.inf_size:
                    return 0
                elif abs(self.inf_size) > abs(frac.inf_size):
                    return Fraction(self.inf_size,0)
                else:
                    return Fraction(frac.inf_size,0)
            numerator = ((self.numerator*frac.denominator)+(frac.numerator*self.denominator))
            denominator = (self.denominator*frac.denominator)
        elif type(frac) in(float,int):
            if self.inf_size !=0:
                return self
            numerator = (frac*self.denominator) + self.numerator
            denominator = self.denominator
        else:
            raise ValueError('Fraction can only add with to int float or fractions')
        return Fraction(numerator,denominator)

    def __mul__(self,frac):
        """Return the product of this fraction and another fraction or number as a new fraction if both infinity size = 0(int and float infinity size = 0)
           if 1 of the fraction's infinity size isn't 0, return the one with bigger infinity value(negative till acts nomally)"""
        if isinstance(frac,Fraction):
            if self.inf_size !=0 or frac.inf_size != 0:
                if abs(self.inf_size) > abs(frac.inf_size):
                    return Fraction(self.inf_size,0)
                else:
                    return Fraction(frac.inf_size,0)
            if self.numerator == 0 or frac.numerator == 0:
                return 0
            numerator = self.numerator*frac.numerator
            denominator = self.denominator*frac.denominator
        elif type(frac) in(float,int):
            if self.inf_size !=0:
                return self
            numerator = self.numerator *frac
            denominator = self.denominator
        else:
            raise ValueError('Fraction can only multiply with to int float or fractions')
        return Fraction(numerator,denominator)

    def __sub__(self, frac):
        """Return the subtraction of the two fraction or number as a new fraction if both infinity size = 0(int and float infinity size = 0)
           if 1 of the fraction's infinity size isn't 0, return the one with bigger absolute infinity value unless, if it is the same infinity
           return 0
        """
        if isinstance(frac,Fraction):
            if self.inf_size !=0 or frac.inf_size != 0:
                if self.inf_size == frac.inf_size:
                    return 0
                elif abs(self.inf_size) > abs(frac.inf_size):
                    return Fraction(self.inf_size,0)
                else:
                    return Fraction(-frac.inf_size,0)
            numerator = ((self.numerator*frac.denominator)-(frac.numerator*self.denominator))
            denominator = (self.denominator*frac.denominator)
        elif type(frac) in(float,int):
            if self.inf_size !=0:
                return self
            numerator = self.numerator - (frac*self.denominator)
            denominator = self.denominator
        else:
            raise ValueError('Fraction can only add with to int float or fractions')
        return Fraction(numerator,denominator)

    def __gt__(self, frac):
        """Two fractions are equal if they have the same value.
           Fractions are stored in proper form so the internal representation
           is unique (3/6 is same as 1/2).
        """

        if isinstance(frac,Fraction):
            if (self.numerator ==0 and self.denominator==0) or (frac.numerator ==0 and frac.denominator==0):
                return self.inf_size > frac.inf_size
            if self.inf_size!=0 or frac.inf_size!= 0:
                return self.inf_size > frac.inf_size
            else:
                return self.numerator*frac.denominator > frac.numerator*self.denominator
        elif type(frac) in(float,int):
            if self.numerator ==0 and self.denominator==0:
                return 0 > frac
            return self.numerator/self.denominator > frac
        else:
            raise ValueError('Fraction can only be compare to int float or fractions')

    def __neg__(self):
        """Return the negative of fraction"""
        if self.numerator ==0 and self.denominator==0:
            return Fraction(-self.inf_size,0)
        else:
            return Fraction(-self.numerator,self.denominator)

    def __eq__(self, frac):
        """Two fractions are equal if they have the same value.
           Fractions are stored in proper form so the internal representation
           is unique (3/6 is same as 1/2).
        """

        if isinstance(frac,Fraction):
            if self.numerator ==0 and self.denominator==0:
                if frac.numerator ==0 and frac.denominator==0:
                    return True
                return 0 == frac.numerator/frac.denominator
            return self.numerator == frac.numerator and self.denominator == frac.denominator and self.inf_size == frac.inf_size
        elif type(frac) in(float,int):
            if self.numerator ==0 and self.denominator==0:
                return 0 == frac
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
