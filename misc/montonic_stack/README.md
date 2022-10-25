# Monotonic Stack/ Dque intro

The word monotonic means a list or a function that is either always increasing, oralways decreasing.
A montonic stack or a monotonic queue is a queue/stack that holds that property

Monotonic stack is a regular stack. However, if when we push an element. We first check if adding an element breaks the monotonic condition. If so, we pop the top element off the stack until pushing the new element no longer breaks the condition.O
