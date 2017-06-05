# Grouping numbers by proximity
This is my solution for the problem presented by Mindera in order to apply to their Graduate Program.

The problem:
"Create an algorithm that can take as an input an array of Integers and can group them into N groups depending on how close they are to each other. 
The solution should solve the problem for any list of Integers and groups (provided the groups are less or equal to the total number of Integers). Furthermore, the solution needs to have the right level of automated testing to validate that it works, and that the code is resilient to modifications." @ https://minderacraft.workable.com/j/85F6E6EF6F

Sequence of aproaches:
>In the first minutes I developed a function that calculated the distance from each number to all others (adjacency matrix). Then I realised that it was going to be ambiguous the way that I am going to determine where am I going to separate the main group in 'k' sub-groups. There I realized that there was some theory that I dind't knew at the time.
>I started my research, and I started to find somethings about "Clustering". At that moment I tried the Prim's algorithm (taking the main group ordered as my minimum spanning tree), but it turned out to be a bad solution for the problem.
>At last I did some more research and discovered the "K-Means" algorithm, that turned out to be close to the expected solution (judging by the examples presented). Although it failed mainly when I had a number much more distant from the others than the normal distances (relatively).
>Then I explored a solution based on a coefficient that I created. That coefficient was the sum of the distances of the consecutive numbers of each ordered cluster, divided by the cardinal of that same cluster. The sum of the coefficients from each cluster was a number that I was trying to minimize each iteration of the algorithm. Then I faced that with the example solutions and realized that I was in a bad path again.
>Ultimatly I optimized my "K-Means Clustering" algorithm and that's my final solution. I know it was not perfect solution, but the example solutions told me that my other solutions were worst than this one.

Even if you don't recrut me, I'm hopping you (Midera HR) share with me what aproach you needed me to have.

Thanks.
João Ferreira
