## Description

The xxx Warehouse team has been growing a bit too fast and people are getting complacent. The xxx Engineering team has been tasked to come out with a new
incentive system to encourage the workers to be competitive.

The xxx Warehouse team already has a mechanism that assigns a 'score' to every person at the end of every hour. Your potential colleague, another data
scientist, has suggested to make use of that 'score' to reward the top performer of every hour with 10 SS points + some bonus SS points. At the end of every week,
SS points can be converted to holiday or can also be converted to 1.000 IDR :D

The bonus SS points rewarded are the number of top scores in the previous hours that are lower than the top score in this hour. The following is an illustration:

* If the top scores of hour-1, hour-2, and hour-3 are 250, 1820, and 870,
* and if the top score of hour-4 = 1000,
* then 2 bonus points are rewarded because 250 and 870 are lower than 1000.
* The top scorer of hour-4 will receive (10 + 2) SS points.

Your VP of Engineering wants to find out the approximate cost of this initiative to Swift Warehouse team and you have been asked to solve this problem! You will be
given a set of simulated scores, which is an array of numbers representing the top scores, starting from hour-1. Tell him how many SS points we have given for free
by completing this function.
