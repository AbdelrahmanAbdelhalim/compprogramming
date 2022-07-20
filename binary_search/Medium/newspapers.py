"""Ptoblem Statement
You've begun working in the one and only Umbristan, and it is part of your job duty to organize newspapers. Every morning, your fellow coworkers will dilligently read through the newspapers to examine its contents. It is your job toorganize the newspapers into piles and hand them out to your coworkers to read through.

Each newspaper is marked with the time it would take to read through its contents. The newspapers are carefully laid out in a line in a particular order that must not be broken when assigning the newspapers. You cannot pick and choose newspapers randomly from the line to assign to a co-worker. Instead, you must take newspapers from a particular subsection of the line, make a pile and give that to a co-worker.

What is the minimum amount of time it would take to have your coworkers go through all the newspapers?
Constraints

1 <= newspapers_read_times.length <= 10^5

1 <= newspapers_read_times[i] <= 10^5

1 <= num_coworkers <= 10^5
Examples
Example 1:
Input: newspapers_read_times = [7,2,5,10,8], num_coworkers = 2
Output: 18
Explanation:

Assign first 3 newspapers to one coworker then assign the rest to another. The time it takes for the first 3 newspapers is 7 + 2 + 5 = 14 and for the last 2 is 10 + 8 = 18.
"""

"""Idea of the solution
Since the problem is asking for the minimum time it is logical to try out different 'Read Times' and see how many workers we will need to
achieve that. And if that number is smaller than the workers that we have then it is achievable and if it is not then we try for other values.
The way we try values is by doing a binary search on a certain range. The minimum possible time needed is the max number in the array. Since
if you assign one person to each newspaper (which is best possible scenario) then the time needed would be the max of the array. The longest
time possible is when you have 1 worker in which case you would need sum(arr) time to finish
"""
from typing import List

def possible(read_times, num_coworkers, max_time_per_worker):
    time_left = max_time_per_worker
    index = 0
    required_workers = 1
    while index < len(read_times):
        if read_times[index] <= time_left:
            time_left -= read_times[index]
            index += 1
        elif read_times[index] > time_left:
            time_left = max_time_per_worker
            required_workers += 1
    return required_workers <= num_coworkers
            
def newspapers_split(newspapers_read_times: List[int], num_coworkers: int) -> int:
    l = max(newspapers_read_times)
    r = sum(newspapers_read_times)
    ans = 0
    while l <= r:
        mid = int((l+r)/2)
        if possible(newspapers_read_times, num_coworkers, mid):
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    return ans
