# Intervals

Interval problems involve a list of intervals, each represented by a start and an end time/position.
The goal is typically to detect or merge overlapping intervals.

## Fundamental Concepts
### Determine if there is an overlap between two intervals
Thinking in the oppsite way, how would the intervals look like if they do not overlap ?
End time of the first interval has to be earlier than the start time of the second interval.
i.e. x2 < y1 or y2 < x1

x1  x2
|---|
        |----|
        y1  y2

y1  y2
|---|
        |----|
        x1   x2
So the overlapping condision is not(x2 < y1 or y2 < x1)

### Finding the overlap

