# calculate the probability of events:
# both children are girls conditional on the first child is a girl
# and both children are girls conditional on one of them is a girl

import random

def random_kid():
    return random.choice(["boy","girl"])

both_girls = 0
first_girl = 0
either_girl = 0

random.seed(0)
for _ in range(10000):
    first = random_kid()
    second = random_kid()
    if first == "girl":
        first_girl += 1
    if first == "girl" and second == "girl":
        both_girls += 1
    if first == "girl" or second == "girl":
        either_girl += 1

print("P(both|first): ", both_girls/first_girl)
print("P(both|either): ", both_girls/either_girl)

def uniform_pdf(x):
    return 1 if x >= 0 and x < 1 else 0

def uniform_cdf(x):
    if x < 0: return 0
    elif x < 1: return x
    else: return 1

# plot a uniform cdf
from matplotlib import pyplot as plt
xs = [x/10.0 for x in range(-10,20)]
plt.plot(xs,[uniform_cdf(x) for x in xs]) 
plt.title("The uniform cdf")
plt.show()

import math
# the pdf of normal distribution could be defined as
def normal_pdf(x, mu=0, sigma=1):
    sqrt_two_pi = math.sqrt(2 * math.pi)
    return (math.exp(-(x-mu)**2/2/sigma**2)/(sqrt_two_pi*sigma))

# plot some of the pdf
xs = [x/10.0 for x in range(-50,50)]
plt.plot(xs,[normal_pdf(x,sigma=1) for x in xs],'-',label='mu=0,sigma=1')
plt.plot(xs,[normal_pdf(x,sigma=2) for x in xs],'--',label='mu=0,sigma=2')
plt.plot(xs,[normal_pdf(x,sigma=0.5) for x in xs],':', label='mu=0,sigma=0.5')
plt.plot(xs,[normal_pdf(x,mu=-1) for x in xs],'-.',label='mu=-1,sigma=1')
plt.legend()
plt.title("Various Normal pdfs")
plt.show()

# the cdf of normal distribution could be defined as
def normal_cdf(x, mu=0, sigma=1):
    return (1+math.erf((x-mu)/math.sqrt(2)/sigma))/2

# plot some of the cdfs
plt.plot(xs,[normal_cdf(x,sigma=1) for x in xs],'-',label='mu=0,sigma=1')
plt.plot(xs,[normal_cdf(x,sigma=2) for x in xs],'--',label='mu=0,sigma=2')
plt.plot(xs,[normal_cdf(x,sigma=0.5) for x in xs],':', label='mu=0,sigma=0.5')
plt.plot(xs,[normal_cdf(x,mu=-1) for x in xs],'-.',label='mu=-1,sigma=1')
plt.legend(loc=4)
plt.title("Various Normal cdfs")
plt.show()

# use binary search to invert normal_cdf 
# to find the value corresponding to a specified probability
def inverse_normal_cdf(p, mu=0, sigma=1, tolerence=0.00001):
    # if not standard, compute standard and rescale
    if mu!=0 or sigma!=1:
        return mu+sigma*inverse_normal_cdf(p,tolerence=tolerence)
    low_z, low_p = -10, 0 # normal_cdf(-10) is 0
    hi_z, hi_p = 10, 1 # normal_cdf(10) is 1
    while hi_z - low_z > tolerence:
        mid_z = (low_z + hi_z) / 2 # consider the midpoint
        mid_p = normal_cdf(mid_z) # and the cdf's value there
        if mid_p < p: # midpoint is too low, search above it
            low_z, low_p = mid_z, mid_p
        elif mid_p > p: # midpoint is too high, search below it
            hi_z, hi_p = mid_z, mid_p
        else:
            break
    return mid_z

# for illustrating the Central Limit Theorem
from collections import Counter
def bernoulli_trial(p):
    return 1 if random.random() < p else 0

def binomial(n, p):
    return sum(bernoulli_trial(p) for _ in range(n))

def make_hist(p, n, num_points):
    data = [binomial(n, p) for _ in range (num_points)]
    # show a bar chart of the actual binomial samples
    histgram = Counter(data)
    plt.bar([x - 0.4 for x in histgram.keys()],
            [v / num_points for v in histgram.values()],
            0.8, color='0.75')
    mu = p * n
    sigma = math.sqrt(n * p * (1 - p))
    # show a line chart of the normal approximation
    xs = range(min(data), max(data) + 1)
    ys = [normal_cdf(i + 0.5, mu, sigma) - normal_cdf(i - 0.5, mu, sigma) for i in xs]
    plt.plot(xs, ys)
    plt.title("Binomial Distribution vs. Normal Approximation")
    plt.show()

# an example
make_hist(0.75, 100, 10000)

# for further exploration
# scipy.stats is a module which contains many functions about
# probability distribution and statistics:
# https://docs.scipy.org/doc/scipy/reference/stats.html
# for learning more about probability, a textbook is available at:
# http://www.dartmouth.edu/~chance/teaching_aids/books_articles/probability_book/amsbook.mac.pdf
