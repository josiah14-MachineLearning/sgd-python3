import numpy as np
from math import sqrt, fabs
from functools import reduce

num_features = 100
known_ratings_vec = np.random.randint(0, 6, size=1000)
mean_rating = np.mean(known_ratings_vec)
print("Mean: " + str(mean_rating))

def initialize_feature_vectors(numFeatures, meanRating):
    qi = np.random.random_sample(numFeatures)
    pu = np.random.random_sample(numFeatures)
    # shift the initial dot product close to the mean
    shift_factor = sqrt(meanRating / np.dot(qi, pu))
    return [shift_factor * qi, shift_factor * pu]

def calc_error(qi, pu, knownRating):
    error = knownRating - np.dot(qi, pu)
    return error

def calc_new_qi(qi, pu, error, learningRate, lambdaConst):
    return qi + learningRate * (error * pu - lambdaConst * qi)

def calc_new_pu(qi, pu, error, learningRate, lambdaConst):
    return pu + learningRate * (error * qi - lambdaConst * pu)

def update_feature_vectors(qi, pu, knownRating, calcError, learningRate, lambdaConst):
    error = calcError(qi, pu, knownRating)
    new_qi = calc_new_qi(qi, pu, error, learningRate, lambdaConst)
    new_pu = calc_new_pu(qi, pu, error, learningRate, lambdaConst)
    return [new_qi, new_pu, calcError(new_qi, new_pu, knownRating)]

def sgd(knownRating, learningRate, lambdaConst, numIterations):
    qi, pu = initialize_feature_vectors(num_features, mean_rating)
    for i in range(numIterations):
        qi, pu, error = update_feature_vectors(qi, pu, knownRating, calc_error, learningRate, lambdaConst)
        if fabs(error) < 0.001:
            break
    return [qi, pu, error, knownRating]

guessed_ratings_with_error = [ sgd(knownRating, 0.27, 0.023, 5) for knownRating in known_ratings_vec ]

[ print([fabs(result[2]), np.dot(result[0], result[1]), result[3]]) for result in guessed_ratings_with_error ]
print("Average Error: " + str(reduce(lambda x, y: x + y, map(lambda result: fabs(result[2]), guessed_ratings_with_error)) / len(guessed_ratings_with_error)))
