"""
The reservoir sampling is a very interesting approach to generate a random sample of data from a large population while 
processing all the data just once.

It maintains randomness while maintaining constant memory.



For any element at position i (i >= k):
    P(selecting item) = k/i
    P(keeping item until end) = Product(1 - k/j) for j = i+1 to n
    Final probability = k/n for all elements!

    

This algorithm:
    - Maintains perfect randomness regardless of stream size
    - Uses O(k) memory regardless of how many items it processes
    - Processes each item exactly once
    - Can handle infinite streams



The algorithm is particularly useful in big data scenarios where you:
    - Can't store all data in memory
    - Need a truly random sample
    - Don't know the size of your data in advance
    - Need to process data in a single pass

"""

import random
from typing import Iterator, List, TypeVar

T = TypeVar('T')

def reservoir_sample(stream: Iterator[T], k: int) -> List[T]:
    """
    Performs reservoir sampling on a stream of data.
    
    Args:
        stream: An iterator of elements
        k: Number of elements to sample
        
    Returns:
        A list of k randomly selected elements
    """
    reservoir = []
    
    # Fill the reservoir with first k items
    try:
        for _ in range(k):
            reservoir.append(next(stream))
    except StopIteration:
        return reservoir  # Stream had fewer than k items
    
    # Process remaining elements
    for i, item in enumerate(stream, start=k):
        # Randomly replace elements with decreasing probability
        j = random.randint(0, i)
        if j < k:
            reservoir[j] = item
            
    return reservoir

if __name__=="__main__":
    population = [1,3,5,6,7,8,9,10,14,22,143,23,67,77,80,12,2,66,897,10002]
    five_samples = reservoir_sample(iter(population), 5)
    print(f"The random five samples are: {five_samples}")