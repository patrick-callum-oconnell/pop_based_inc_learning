# pop_based_inc_learning
A Python and C based implementation of Population Based Incremental Learning that solves MAXSAT problems in conjunctive normal form.

PBIL.py holds the class representation of the probability vector and the current population, as well as the various operations on that population
and vector. The c_helper_functions.c file holds functions that perform vector alteration and population generation to speed up the algorithm's progress
(with respect to slow python lists, or even NumPy cythonic lists which are currently the placeholders until the c helper file is done).
