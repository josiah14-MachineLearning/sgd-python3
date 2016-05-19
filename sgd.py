import numpy
from math import sqrt

num_features = 100
known_ratings_vec = np.random.randint(0, 6, size=1000)

def initialize_feature_vectors(numFeatures, knownRatings):
    qi = np.random.random_sample(numFeatures)
    pu = np.random.random_sample(numFeatures)

    # shift the initial dot product close to the mean
    shift_factor = sqrt(np.mean(knownRatings) / np.dot(qi, pu))
    qi = shift_facter * qi
    pu = shift_factor * pu

    return [qi, pu]

def calc_error(qi, pu, knownRating):
    return knownRating - np.dot(qi, pu)

def calc_new_qi(qi, pu, error, learningRate, lambdaConst):
    return qi
           + learningRate
           * (error * pu - lambdaConst * qi)

def calc_new_pu(qi, pu, error learningRate, lambdaConst):
    return pu
           + learningRate
           * (error * qi - lambdaConst * pu)

def update_feature_vectors(qi, pu, knownRating, learningRate, lambdaConst):
    error = calc_error(qi, pu, knownRating)
    new_qi = calc_new_qi(qi, pu, error, learningRate, lambdaConst)
    new_pu = calc_new_pu(new_qi, pu, error, learningRate, lambdaConst)
    return [new_qi, new_pu, error]

def sgd(knownRating, learningRate, lambdaConst, numIterations):
    qi, pu = initialize_feature_vectors(num_features, known_ratings_vec)
    error = calc_error(qi, pu, knownRating)
    for i in range(numIterations):
        qi, pu, error = update_feature_vectors(qi, pu, knownRating, learningRate, lambdaConst)
    return [qi, pu, error]





