"""
AUTHOR: Patrick Callum O'Connell
Date: 3/2/2021

I'm using numpy for now but I'll replace some of these functions with C functions later to speed it up more.
"""


import numpy as np #imports numpy so we can use arrays
                   #instead of super slow Python lists
import random

class PopBasedIncrementalLearning:
    """
    This class can generate and hold a population of
    vectors for Population-Based Incremental learning,
    (via generatePopulation())
    as well as perform the following functions on said population:
    updateProbBest() - updates the probability vector
    towards the current best individual in the population
    updateProbWorst() - updates the probability vector
    towards the current worst individual in the population
    mutateProbVector() - mutates the probability vector
    """

    def __init__(self, SAMPLES, LR, NEGATIVE_LR, LENGTH, MUT_PROBABILITY, MUT_SHIFT):
        """These values are in capital letters because they are specified in the command
        line arguments when running the driver class"""

        self.SAMPLES = SAMPLES #how many vectors are generated for a population before updating prob vector
        self.LR = LR #learning rate (positive)
        self.NEGATIVE_LR #learning rate (negative)
        self.LENGTH = LENGTH #length of bits in a given vector
        self.MUT_PROBABILITY = MUT_PROBABILITY #prob for mutation for any given bit
        self.MUT_SHIFT = MUT_SHIFT #how much mutation alters each bit

        #note: numpy provides functionality for initializing arrays as random, so we could
        #try that as an experiment by passing another boolean parameter to this intialization
        #that indicates whether or not to do it, with default value false

        #initialize the probability vector with probabilities 0.5

        self.probVector = np.zeroes(LENGTH, dtype=np.double)
        j = 0 #I am writing this this way to emphasize that I am using j for indexing in the probVector
              #by arbitrary convention for consistency, so I don't make any mistakes with mixing up i and j
              #i will refer to the sample index instead
        while (j < LENGTH):
            probVector[j] = 0.5
            j += 1

        #initialize a population with that probability vector (2d array representation)
        self.population = np.zeroes(self.SAMPLES * self.LENGTH).reshape(self.SAMPLES, self.LENGTH)

        for i in range(self.SAMPLES): #for each sample
            for j in range(self.LENGTH): #for each bit

                #random number do probability check based on
                #in the future, I will not use a rand_temp temporary random variable
                #and instead just call the random uniform function in the if statements
                #this is just to show the logic
                rand_temp = np.random.uniform(0, 1, 1)
                if (rand_temp <= 0.5):
                    self.population[i][j] = 1
                else:
                    self.population[i][j] = 0

    def generatePopulation(self):
        """Using the current probability vector, generates a new population
        note: in terms of memory, this is NOT generating new vectors, it is overwriting
        the vectors of the previous population"""

        for i in range(self.SAMPLES):
            for j in range(self.LENGTH):

                if (np.random.uniform(0, 1, 1) <= self.probVector[j]): #decides bit based on probability
                    self.population[i][j] = 1
                else:
                    self.population[i][j] = 0

    def updateProbVector(self):
        """Updates the probability vector towards the best solution
        and away from the worst solution"""
        bestVector = findBestVector()
        worstVector = findWorstVector()

        #towards best vector
        for j in range(self.LENGTH):
            self.probVector[j] = self.probVector[j] * (1.0 - self.LR) + bestVector[j] * self.LR   
        
        #away from worst vector
        for j in range(self.LENGTH): 
            if (bestVector[j] != worstVector[j]):
                self.probVector[j] = self.probVector[j] * (1.0 - self.NEGATIVE_LR) + bestVector[j] * self.NEGATIVE_LR

    def mutateProbVector(self):
        """Mutates the probability vector"""

        for j in range(self.LENGTH):
            if (np.random.uniform(0, 1, 1) <= self.MUT_PROBABILITY): #should it mutate at all?
                if (np.random.uniform(0, 1, 1) <= 0.5): #decides direction of mutation
                    mutateDirection = 1
                else:
                    mutateDirection = 0
    
                self.probVector[j] = self.probVector[j] * (1.0 - self.MUT_SHIFT) + mutate_direction * (MUT_SHIFT) #shifts bit

#TODO

    def findBestVector(self):

    def findWorstVector(self):
