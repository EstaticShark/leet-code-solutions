#16 3Sum Closest

You are given a list of integers and a target. Find the sum of three integers in the list that would be the closest to the target and return it.

##Comments

I am writing this for my future self because I felt disappointed in the slow runtime I had somehow managed in doing this problem. Maybe other users had well tuned solutions or maybe I had an off day, but that doesn't change the fact that I feel as if I made a mistake. So from now on if I feel disatisfied with myself, I'll unload my thoughts into a Readme file for future reflections.

My first solution was based on a three pointer implementation. I start off by sorting the list, this would allow for more accurate searches as I will get into later. I would then have one pointer which would act as a 'pivot', where it would iterate from [0, list.length - 2], while the other two pointers would point at the index after pivot and the index list.length - 1. The latter two pointers, which we will call j and k, would collapse towards each other until they would equal each other, checking the sum as we went. The way I selected which pointer would move would be based on if the sum at the moment was lesser or greater than the target. If the sum was greater, then it would move k to the left, since the list was sorted in increasing orders, otherwise we would increase j. However, this would waste a lot of time on inputs that had early solutions or long lists since we had to iterate through the entire list.

The first solution beat a measly 14.79% of submissions in speed which sucks. It definitely didn't feel like a brute force solution as it optimized making comparisons. It did however calculate every possible sum before returning, so it most likely had a O(n^2) runtime. If this was an interview I think I'd have failed by now.

My second attempt was a step up from the first. Instead of tracking the sum at the moment, I thought it would be faster to track the difference from the target, that way instead of having to add the pivot element each time, we can just subtract the other two elements from a p_target, which is the difference between the pivot element and the target. On top of that, I added an early exit which would exit upon finding the correct sum. I believe most of this time was saved in adding the early exit, since it heavily favored lists that had solutions at the beginning.

The second solution did much better than the first, but still not quite there by only beating 39.86% of submissions.

In the third attempt, I had wondered if storing the differences was actually faster, and if the speed in the second attempt was only from the early exits. So this time I implemented the first solution again, except this time I allowed for early exits for when the sum was correct. Judging by the results, it was indeed faster to compare numbers as sums rather than differences.

The third solution made a significant dent in the average time spent on each test, winning out on 66.65% of submissions

Out of curiousity for how fast I could make my code, I tried again to whittle down the time. I looked for places where I thought time could be saved and I looked at an items variable which I had used to store the length of the list, although I had only referenced it twice I wondered if it would be faster to reference the length of a list as the return value of the __len__() function or as a reference. Suprisingly, referencing the length as __len__() was much faster, from being faster than 66.65% of submissions to 75.12%. Maybe it was the act of initializing the items variable, or maybe it was faster to make a function invocation over a reference. Either way I think it should normally not matter this much. If I access the length often, I'd probably use a reference variable, otherwise I'd call __len__() for one-time uses.

For a bit I continued optimizing the solution. The changes felt more like mirco-optimizations rather than some big brain algorithm development. By saving the mininum differences between the closest_sum and the target each time the closest_sum was updated, I made it so that instead of having to calculate the same sums twice in a row, the second calculation would instead be a reference. This small change brought the speed up to 86.06%. Its suprising how such a small change could make such a big difference. Makes you think though, how many micro-optimizations have the fastest submissions been through? This feels less like problem solving and more like a derby car race.

After fighting for what seemed to be inches of a football field, I began to lose interest in my little optimization game. I learned a good bit about micro-optimizations, but too bad it means little to nothing in the long run. Over the hour I took, I realized I should focus more on problem solving rather than being the fastest. 

I leave this here to remind myself, anyone can be fast with an hour of optimization, but the only thing that matters in the end is if my problem solving skills develop well enough to pass the whiteboard tests