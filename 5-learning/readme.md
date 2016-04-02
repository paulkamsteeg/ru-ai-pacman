# Topic 5: Machine Learning Pacman

### Introduction

After a while pacman realizes the ghosts are actually not very clever. In fact, after careful empirical observation he notes that they only adopt one of 3 strategies to find him:

- **Seeker** : this ghost always tries to move directly towards Pacman's current location.
- **Tracker** : this ghost forever runs round the same 'racetrack' of locations on the map.
- **Random** : this ghost just moves randomly at any time.

Pacman knows that if he can identify which type of ghost he is trying to beat, then he can exploit its stupidity to make his own life much easier. Unfortunately, he doesn't (yet) know how to identify which type of ghost is which.

However, pacman has been recording his experiences for a while now and has a large database of ghost movements and their identified type, (i.e. seeker, tracker, or random). He also knows that possibly this thing called machine learning can learn from this database and provide some quick rules for identifying the  type.

Note: for this assignment you do not need any of the code from previous weeks, and the code is structured in a different way.

#### Files you'll edit and submit

* `classifier.py` where your ghost classifier will reside.

#### Files you might want to look at

* `classifiertest.py`, the main file that runs the classifier tests, by loading the data-files, assigning example labels and calling your classifier as defined in `classifier.py`.

### Learning Pacman

First, see what happens when you train a default classifier (always predicts 0) the problem of discriminating a random ghost from a tracker ghost, and assess generalization performance *on the same dataset*:

```
python classifiertest.py --train RandomGhost_easy TrackerGhost_easy --test RandomGhost_easy TrackerGhost_easy
```

You should see that this classifier does quite poorly (as expected).

Inspect its code (in `classifier.py`) and make sure you understand what it's doing. Especially make sure that you understand what features are represented by the data.

#### Assignment 1

Improve the `BinaryClassifier` in `classifier.py` to actually learn from the data using the *[perceptron](http://en.wikipedia.org/wiki/Perceptron) algorithm*. The provided class `BinaryClassifier` has a method `train` which already loops over the training examples multiple times to update the classifier parameters. You should modify this so it actually learns something during this process. You can test your classifier using the logical *or* problem:

```
python classifiertest.py --train or0 or1 --test or0 or1
```

When you have your classifier working for the *or* problem, also test it for the *xor* problem (just add the x to all the *or* arguments). Does it work? Explain to yourself why.

Your trained classifier should achieve an error rate of **less than 0.2** on the Random vs. Tracker easy training and testing problem (same arguments as above), and **train in about 10 seconds**.

```
python classifiertest.py --train RandomGhost_easy TrackerGhost_easy --test RandomGhost_easy TrackerGhost_easy
```

The Random and Tracker easy problems are easy because the world has no walls, thus the ghosts can move around freely. A harder and more realistic situation is when Pacman and the ghosts have to manouvre around walls - this limits the ghosts' movement and makes it more likely that the different types of ghosts will appear the same.

Try your solution to the easy problem on test data from the harder problem where the worlds contain walls:

```
python classifiertest.py --train RandomGhost_easy TrackerGhost_easy --test RandomGhost TrackerGhost
```

#### Assignment 2

One of the things which makes the ghost recognition problem hard is that the given features contain only indirect information about the ghost type. In the data-set the features are the 20-move histories of both Pacman (who actually doesn't move) and the ghost. It is a list of lists, of 4 elements `[pac_x, pac_y, ghost_x, ghost_y]` for each of the 20 time points, as shown in this partial example:

| Time/Feature | Pacman x | Pacman y | Ghost x | Ghost y |
|:------------:|:--------:|:--------:|:-------:|:-------:|
|...|...|...|...|...|
|t=-4|4|4|9|8|
|t=-3|4|4|8|8|
|t=-2|4|4|7|8|
|t=-1|4|4|7|7|
|t=0|4|4|7|6|

Looking at this table it should be clear what type of ghost this is... It always moves towards Pacman, so it is likely a directional ghost (Seeker). One way to improve the performance of our classifier is to change the feature representation such that the classification problem is easier, as the distinctions between the different agents is easier to see (this process of preprocessing features to make the learning problem easier is a basic first step in applying machine learning to most problems, which is sometimes called *feature engineering*).

Write the body for the method `pacmanfeaturemapper` in `classifier.py`, which takes as input a data set and returns a transformed dataset which makes the learning problem easier, in that it

- requires fewer features,
- requires less training time and
- performs better on unseen test examples.

Call the method using the following arguments:

```
python classifiertest.py --train RandomGhost_easy TrackerGhost_easy --test RandomGhost TrackerGhost --featuremapper pacmanfeaturemapper
```

##### Hints and Observations #####

- The relative distance between the pacman and the ghost is a useful feature for discrimination
- The relative distance a ghost travels from it's starting point is another useful feature

Part of the reason the easy problems used above are easy because the
worlds have no walls, thus the ghosts can move around freely. A harder
and more realistic situation is when the pacman and the ghosts have to
avoid the walls, this limits the ghosts movement and makes it more
likely that the different ghosts will look the same.

Try your solution to the easy problem on testing data from the harder
problem where the worlds contain walls:

```
python classifiertest.py --train RandomGhost_easy TrackerGhost_easy --test RandomGhost TrackerGhost --classifier BinaryClassifier
```

Again repeat this test for all possible binary combinations of ghosts.

### Bonus Assignment

A perceptron is a *binary classifier* in that it only produced a 0 or 1
output. This means it can be used only to distinguish two classes (or
types of ghost). However, pacman knows that there are at least 3 types
of ghost in his world. Add modified classifer training and testing
methods to the class `MultiClassClassifier` in the file
`classifier.py` such that pacman can identify which of the
three types of ghost are there. You can load and test this 3-class
problem with the following code:

```
python classifiertest.py --train RandomGhost_easy TrackerGhost_easy SeekerGhost_easy --classifier MultiClassClassifier
```
