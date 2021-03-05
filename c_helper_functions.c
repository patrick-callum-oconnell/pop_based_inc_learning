/*
* This file holds all of the helper functions for the main PBIL python class.
* I haven't yet integrated these into PBIL, so NumPy arrays / functions are there
* currently to take their place until these have been used instead.
*/

#include<stdio.h>
#include<stdlib.h>

/* Mutation function that takes in a vector of doubles
*  and mutates that vector based on the following parameters
*  @param prob_vector - double[], the probability vector that will be altered
*  @param mut_probability - double, probability that any bit will mutatea
*  @param mut_shift - double, the amount we want a bit to mutate if it does
*/
double[] mutate(double[] prob_vector, double mut_probability, double mut_shift) {
  
  int arr_len = sizeof(prob_array);
  double mut_check; //current iteration probability to check mut_prob
  int mutate_direction; //tracks which direction to mutate vector

  for (int i = 0; i < arr_len; i++) {
    
    //get random number to do mutation prob check
    mut_check = (double) (rand() / RAND_MAX);

    if (mut_check <= mut_probability) {
      mutate_direction = 1;
    }
    else {
      mutate_direction = 0;
    }
    probVector[i] = probVector[i] * (1.0 - self.mut_shift) + mutate_direction * (mut_shift);
  }
  
  return prob_vector;
}


