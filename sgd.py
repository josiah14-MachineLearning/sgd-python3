import numpy as np
from math import sqrt

num_features = 100
known_ratings_vec = np.random.randint(0, 6, size=1000)
mean_rating = np.mean(known_ratings_vec)
print("Mean: " + str(mean_rating))

def initialize_feature_vectors(numFeatures, knownRatings):
    qi = np.random.random_sample(numFeatures)
    pu = np.random.random_sample(numFeatures)

    # shift the initial dot product close to the mean
    shift_factor = sqrt(mean_rating / np.dot(qi, pu))
    qi = shift_factor * qi
    pu = shift_factor * pu

    print([qi, pu])

    return [qi, pu]

def calc_error(qi, pu, knownRating):
    error = knownRating - np.dot(qi, pu)
    # print("Error: " + str(error))
    # print("Dot: " + str(np.dot(qi, pu)))
    return error

def calc_new_qi(qi, pu, error, learningRate, lambdaConst):
    return qi + learningRate * (error * pu - lambdaConst * qi)

def calc_new_pu(qi, pu, error, learningRate, lambdaConst):
    return pu + learningRate * (error * qi - lambdaConst * pu)

def update_feature_vectors(qi, pu, knownRating, learningRate, lambdaConst):
    new_qi = calc_new_qi(qi, pu, calc_error(qi, pu, knownRating), learningRate, lambdaConst)
    new_pu = calc_new_pu(new_qi, pu, calc_error(new_qi, pu, knownRating), learningRate, lambdaConst)
    return [new_qi, new_pu, calc_error(new_qi, new_pu, knownRating)]

def sgd(knownRating, qi, pu, learningRate, lambdaConst, numIterations):
    new_qi, new_pu = [qi[:], pu[:]]
    for i in range(numIterations):
        new_qi, new_pu, error = update_feature_vectors(new_qi, new_pu, knownRating, learningRate, lambdaConst)
    return [new_qi, new_pu, error]

qi, pu = initialize_feature_vectors(num_features, known_ratings_vec)
guessed_ratings_with_error = [ sgd(knownRating, qi, pu, 0.08, 20, 100) for knownRating in known_ratings_vec ]

[ print(result) for result in guessed_ratings_with_error ]
