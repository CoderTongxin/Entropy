

from __future__ import division
from math import log

def entropy(pi):
    total = 0
    for p in pi:
        p = p / sum(pi)
        if p != 0:
            total += p * log(p, 2)
        else:
            total += 0
    total *= -1
    return total


def gain(d, a):

    total = 0
    for v in a:
        total += sum(v) / sum(d) * entropy(v)

    gain = entropy(d) - total
    return gain

# set of example of the dataset
Reads = [6, 7] # true, false

# attribute, number of members (feature)
Celebrity = [
    [4, 2],  # true
    [2, 5],  # false
]
Sports = [
    [3, 3],  # true
    [3, 4],  # false
]
Politics = [
    [4, 2],  # true
    [2, 5]   # false
]
Technology = [
    [2, 3],  # true
    [4, 4]   # false
]

print(gain(Reads, Celebrity))
print(gain(Reads, Sports))
print(gain(Reads, Politics))
print(gain(Reads, Technology))

# set of example of the dataset
# when Celebrity=true

Reads1 = [4, 2] # true, false

# attribute, number of members (feature)

Sports1 = [
    [2, 1],  # true
    [2, 1],  # false
]
Politics1 = [
    [2, 0],  # true
    [2, 2]   # false
]
Technology1 = [
    [0, 2],  # true
    [4, 0]   # false
]
print("when Celebrity=true")
print(gain(Reads1, Sports1))
print(gain(Reads1, Politics1))
print(gain(Reads1, Technology1))



# set of example of the dataset
# when Celebrity=false

Reads2 = [2, 5] # true, false
# attribute, number of members (feature)

Sports2 = [
    [1, 2],  # true
    [1, 3],  # false
]
Politics2 = [
    [2, 2],  # true
    [0, 3]   # false
]
Technology2 = [
    [2, 1],  # true
    [0, 4]   # false
]
print("when Celebrity=false")
print(gain(Reads2, Sports2))
print(gain(Reads2, Politics2))
print(gain(Reads2, Technology2))

Reads3 = [2, 1]

Sports3 = [
    [1, 0],  # true
    [1, 1],  # false
]
Politics3 = [
    [2, 0],  # true
    [0, 1]   # false
]
print(gain(Reads3, Sports3))
print(gain(Reads3, Politics3))
print("question 4")
val1 = (3/8*1/2*3/8*3/8)*7/15
val2 = (2/3*4/9*2/3*4/9)*8/15
t = (3/8*1/2*3/8*3/8)*7/15

print (t)
print (val1+val2)
print(t/(val1+val2))