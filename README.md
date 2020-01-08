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
Time Complexity of answering Q queries about M ranges is O(max(Q, M)) because 
- O(M) is needed to pre-process the M ranges (time complexity for processing one range is O(1))
- O(1) is needed to accumulate the information from the M ranges (because the range size is 1,000,000 maximum, and it's already known)
- O(Q) is needed to answer the Q queries (because answering one query takes O(1))

### Memory Complexity
Memory Complexity of answering Q queries about M ranges is O(1) because no matter what the input is, you just need to have 1,000,000 array cells to hold the expanded info from the ranges (you don't even need to save the ranges themselves) and this is always constant regardless the input size.

