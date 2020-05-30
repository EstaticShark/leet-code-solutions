# #11 Container With Most Water

Given a list of positive integers, find the area of the rectangle created such that the difference in indices is the length and the height is the smaller integer of the numbers at each indice.

## Notes

This question is annoying to get right. You're forced to analyze this in two dimensions. To most effectively find the answer you need to find a way to best compare two elements, each with multiple variables.

The first thing that comes to mind on how to solve the problem is how can we use the properties of the elements to reduce the amount of comparisons needed? Clearly there exists cases where instead of comparing areas, you can compare single variables. For example, if we are comparing numbers at both ends and the left number is smaller then you know that moving the number on the right that is being compared would be pointless, since you are only decreasing the width and the height could only get smaller.

We can generalize our specific case above to realize that if you are moving either pointer inwards, the area can only decrease if the pointer that moves is the bigger one, since our rectangle loses width and sometimes loses height. This is a great shortcut, since we can shorten a comparison of two areas to the comparison of two heights. However this should only work for pointers that are decreasing in distance. If the pointers are moving away from each other, we are guarenteed to gain width, but we cannot be sure if we are to gain or lose height, requiring us to compare areas which makes this comparison pointless.

So we can develop an algorithm with this information. We keep track of the largest area through a variable and have pointers on both ends of the list so that we can make use of our above comparison operation. We check the number that each pointer represents and move the pointer of the smaller number inwards. We continue until we have reached the end, comparing areas and updating values as needed. Once we reach the end we can stop and return the max area.

## Comments

This one was tricky. I definitely took more than 30 minutes but I think the solution I came up with was decent with a rating of 78.95%.