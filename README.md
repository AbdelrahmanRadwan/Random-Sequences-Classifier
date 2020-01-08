# Random-Sequences-Classifier

## How to run
**Number**: Specify the number of ranges needed *optional

```python3 main.py <Number>```

**example:**

```python3 main.py 80```

## Algorithm
Given M ranges, we can pre-process them by expanding the information hidden in these ranges, so later it will be easier to answer queries regarding how many times was a number covered over ranges.

## Algorithm Analysis
### Time Complexity
Time Complexity of answering Q queries about M ranges is O(Q + M) because 
- O(M) is needed to pre-process the M ranges (time complexity for processing one range is O(1))
- O(1) is needed to accumulate the information from the M ranges (because the range size is 1,000,000 maximum, and it's already known)
- O(Q) is needed to answer the Q queries (because answering one query takes O(1))

### Memory Complexity
Memory Complexity of answering Q queries about M ranges is O(1) because no matter what the input is, you just need to have 1,000,000 array cells to hold the expanded info from the ranges (you don't even need to save the ranges themselves) and this is always constant regardless the input size.

## Sample Input/Output
```
$python3 main.py 20

Generating 20 random ranges is being done now ...
Ranges are:
[663898, 702164]
[532398, 549832]
[719237, 896025]
[972904, 994764]
[558446, 680935]
[832528, 854478]
[491208, 544049]
[295129, 750500]
[343183, 791083]
[752160, 781924]
[318496, 487056]
[153203, 503479]
[451586, 694714]
[352915, 641837]
[82456, 955334]
[146125, 650978]
[960063, 986600]
[831275, 936983]
[469364, 976790]
[403718, 857607]
20 random ranges were generated ...
Let the fun begins!!
I played the game by 648566, the result was 8!
I played the game by 894097, the result was 4!
I played the game by 147312, the result was 2!
I played the game by 122441, the result was 1!
I played the game by 462231, the result was 9!
I played the game by 193592, the result was 3!
I played the game by 383926, the result was 7!
I played the game by 96705, the result was 1!
I played the game by 884848, the result was 4!
A patch with 10 random numbers was processed. a new patch will start after 5 seconds. to Quit press Ctrl + c
I played the game by 248310, the result was 3!
I played the game by 140896, the result was 1!
I played the game by 155796, the result was 3!
I played the game by 203618, the result was 3!
I played the game by 486099, the result was 10!
I played the game by 870281, the result was 4!
I played the game by 338040, the result was 5!
I played the game by 377343, the result was 7!
I played the game by 460068, the result was 9!
I played the game by 707782, the result was 5!
A patch with 10 random numbers was processed. a new patch will start after 5 seconds. to Quit press Ctrl + c
I played the game by 29311, the result was 0!
I played the game by 640783, the result was 9!
I played the game by 765060, the result was 6!
I played the game by 618900, the result was 9!
I played the game by 331297, the result was 5!
I played the game by 401080, the result was 7!
I played the game by 20784, the result was 0!
I played the game by 55213, the result was 0!
I played the game by 130865, the result was 1!
I played the game by 284536, the result was 3!
A patch with 10 random numbers was processed. a new patch will start after 5 seconds. to Quit press Ctrl + c


```