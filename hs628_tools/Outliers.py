# -*- coding: utf-8 -*-
# Python version 3.6

import re
import numpy as np
import csv

from numpy import NaN


class Outliers:
    """
    Concept:
    Returns list of data(list array) which fall outside of two standard deviations under the normal distribution curve.
    Parameters:
    mean, standard deviation(std)
    Returns:
    outliers
    """

    def __init__(self):  # default values input for mean and std
        """
        Actions:
        (0) Define parameters
        (2) Clean data by removing none numeric values("None", "Norm", and etc.)
        (3) Convert values from string to float
        Unit tests to confirm data cleaning:
          >>> "6".isnumeric()
          True
          >>> "None", "Norm".isnumeric()
          False
        """
        self.mean = mean
        self.std = std
        self.data = data


    def clean(self, pattern):
        pat1 = bool(re.match(pattern='\d{}-\d{}', string='123-4560'))
        pat2 = bool(re.match(pattern='\$\d*\.\d{}', string='$123.45'))
        pat3 = bool(re.match(pattern='[A-Z]\w*', string='Australia'))
        if bool(pattern.match(pat1, pat2, pat3)):
            return(NaN)
        else:
            pass

        for i in range(len(self.data)):
            self.data[i] = [elem for elem in self.data[i] if elem.isnumeric()]
        self.data = np.array(self.data, dtype=np.float)  # convert to float
        print(self.data)


    def calc_outliers(self, my_arr, out_lim):
        """
        Concept:
            Function for calculating samples out of scope of two standard deviation in data and returning those collection
            of samples as outliers
        Parameters:
            my_arr:
            out_lim:
        Actions:
            Get quartile values for outlier limits: out of two standard deviation
        References:
            - Anomaly detection in Python at Lynda.com
              (https://www.lynda.com/Business-Intelligence-tutorials/Anomaly-detection-Python/475936/529731-4.html)
            - A Bayesian Anomaly Detection Framework for Python
              (pyISC: A Bayesian Anomaly Detection Framework for Python;
              Proceedings of the Thirtieth International Florida Artificial Intelligence Research Society Conference)
        """
        my_arr = np.random.randn(20, 10)  # data array
        out_lim = np.self.std*1.96  # set outlier limit
        outliers = np.ones((my_arr.shape[0],), dtype=np.bool)
        self.mean = np.self.mean(my_arr, axis=0)
        self.std = np.self.std(my_arr, axis=0, drop=1)
        for i in range(my_arr.shape[1]):  # added for detect outliers by each column
            col = my_arr[:, i]
            outliers[outliers] &= np.abs((col[outliers] - self.mean[i]) / self.std[i]) < out_lim
        return my_arr[outliers]


    def main(self, data):
        with open("data.csv") as f:
            reader = csv.reader(f)
            next(reader)
            data = [r for r in reader]


if __name__ == '__main__':
    import doctest
    doctest.testmod()


