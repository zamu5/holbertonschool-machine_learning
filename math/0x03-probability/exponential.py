#!/usr/bin/env python3
"""
documentation
"""


class Exponential():
    """

    """
    e = 2.7182818285

    def __init__(self, data=None, lambtha=1.):
        """
        """
        if data is None:
            lambtha = float(lambtha)

            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = lambtha

        else:
            if type(data) is not list:
                raise TypeError("data must be a list")

            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            self.lambtha = 1/(sum(data)/len(data))

    def pdf(self, x):
        """
        """
        if x < 0:
            return 0
        lam = self.lambtha
        PDF = (lam * (Exponential.e ** (-lam * x)))
        return PDF

    def cdf(self, x):
        """
        """
        if x < 0:
            return 0
        CDF = 1 - (Exponential.e ** (-self.lambtha * x))
        return CDF
