# Assignment 1 of Moodify Learning :


**Basic Virus Simulation**


In this task, I start by creating an 100 x 150 matrix with one of it's entries as 1.
Later the spread of this virus(1) is depicted as it spreads according to the following rules:
  * In each iteration 8 random entries are swapped with 8 other entries
  * The nearest neighbours of an infected entry (1) have a 0.25 probability of getting infected
  * The second nearest neighbours of an infected entry have a 0.08 probability of getting infected

The iterations go on until all the entries of the matrix become 1

The result obtained is plotted in 2 graphs:
1. This graph depicts the number of ones in the matrix corresponding to each iteration.
2. This graph depicts the number of ones added in each iteration . The peak obtained for this output was **998**

The graphs have been put up as plots.png file
