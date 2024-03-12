## Team Members: Jubril Olawale Akolade, Tarun Thomas

# Part A:

1. *What sorting algorithm was the speaker trying to improve?*
   The speaker, Andrei Alexandrescu, was focused on improving the performance of *Quicksort* by investigating alternative methods for sorting small arrays. This exploration is part of a broader effort to optimize sorting algorithms by adjusting strategies based on the size of the data set.

2. *At what partition size does VS (Visual Studio) perform a simpler sort algorithm instead of continuing to partition?*
   Visual Studio switches to a simpler sort algorithm when the partition size reaches *32*.

3. *At what partition size does GNU perform a simpler sort algorithm instead of continuing to partition?*
   GNU switches to a simpler sort algorithm when the partition size is *16*.

4. *Regular insertion sort does a linear search backwards from the end of the array for the correct spot to insert. According to the speaker, why does switching to a binary search not improve performance?*
   Switching to a binary search does not improve performance because although it significantly reduces the number of comparisons (especially for arrays with 32 elements), it actually results in a *13% increase* in runtime due to the inefficiency introduced by the inability of the CPU's branch predictor to effectively handle the binary search's comparisons. The binary search introduces more branch mispredictions, which adversely affects performance despite the reduction in comparisons.

5. *Describe what is meant by branch prediction.*
   Branch prediction is a feature of modern CPUs designed to guess which way a branch (e.g., an if-then-else structure) will go before this is known for sure. The purpose of branch prediction is to improve the flow of instruction pipelines by guessing the outcome of conditional operations and preparing the CPU to execute the next set of instructions without having to wait for the branch decision. Correct predictions lead to improved performance by reducing the number of stalled CPU cycles, whereas incorrect predictions can cause performance penalties due to pipeline flushing and reloading.

6. *What is meant by the term informational entropy?*
   Informational entropy, in the context of sorting algorithms and computer science, refers to the amount of disorder or randomness in data. It measures the unpredictability or complexity of information content. In sorting, lower informational entropy indicates more order and predictability in the data, which can be exploited for optimization. High informational entropy means the data is more random, making it challenging to predict and often requiring more operations to sort.

7. *Speaker suggests the following algorithm: make_heap() followed by unguarded_insertion_sort(). Explain what unguarded_insertion_sort() is and why it is faster than regular insertion sort. How does performing make_heap() allow you to do this?*
   Unguarded_insertion_sort() is a variation of insertion sort that does not check whether the iterator has reached the beginning of the array during insertion. This is possible and faster than regular insertion sort because, after performing make_heap(), the smallest element is guaranteed to be at the beginning of the array. This means when shifting elements to find the correct insertion point, there's no need to constantly check for the beginning of the array (hence "unguarded"), as it's impossible to go past the smallest element. This reduces the number of comparisons and branch mispredictions, improving performance.

8. *The speaker talks about incorporating your conditionals into your arithmetic. What does this mean? Provide an example from the video and explain how the conditional is avoided.*
   Incorporating conditionals into arithmetic means using arithmetic operations to implicitly handle cases that would otherwise require explicit conditional statements, thereby avoiding branches that can hinder CPU performance due to branch mispredictions. An example from the talk is when Alexandrescu discusses adjusting the pivot position in quicksort based on whether the array has an even or odd number of elements without using an if-statement. Instead of a conditional branch, he modifies the pivot position calculation with arithmetic that accounts for the array's size, effectively embedding the "conditional" logic into the calculation itself, thus avoiding explicit branch instructions.

9. *The speaker talks about a bug in GNU's implementation. Describe the circumstances of this bug.*
 The video mentioned a bug in GNU's implementation, the bugs involves unexpected behavior or performance issues that arise under certain conditions, affecting the efficiency or correctness of the algorithm.

10. *The speaker shows several graphs about what happens as the threshold increases using his new algorithm. The metric of comparison is increased, and the metric of moves is increased, but time drops... What metric does the author think is missing? Describe the missing metric he speaks about in the video. What is the metric measuring?*
As the sorting time decreases even when the number of comparisons and moves increases, the speaker hints at a missing metric that could explain this counterintuitive phenomenon. This missing metric likely measures the efficiency of CPU utilization or cache performance, essentially capturing how well the sorting algorithm is optimized for the hardware it runs on. It implies that despite doing more work in terms of comparisons and moves, the algorithm is somehow more aligned with the hardware's capabilities, resulting in faster overall execution times.


11. *What does the speaker mean by "fast code is left-leaning"?*
   When the speaker refers to "fast code is left-leaning," this is indicating a preference or emphasis on optimizing the performance of code by focusing on the most critical or frequently executed parts first. "Left-leaning" implies prioritizing  efficiency and speed in the early stages or most critical sections of the code execution path. It suggests an approach where optimization efforts are directed towards the parts of the code that have the most significant impact on performance.

12. *What does the speaker mean by "not mixing hot and cold code"?*
   The concept of "not mixing hot and cold code" differentiates between "hot" code, which is executed frequently or is performance-critical, and "cold" code, which is less frequently executed or not as critical to performance. By not mixing them, the speaker emphasizes the idea of organizing or structuring code in a way that separates performance-critical sections from less critical ones. This separation can help improve cache efficiency and optimize CPU usage by ensuring that the most frequently accessed code (hot) is readily available and not cluttered with less important code paths (cold), potentially enhancing overall performance.


# Part B:

1. *What did you/your team find most challenging to understand in the video?*
   Understanding how the computer predicts and deals with different choices in code (branch prediction) and how small changes in code can affect the computer's efficiency was a bit tricky. Also, figuring out the relationship between sorting methods and the computer's inner workings, like with branch prediction and informational entropy, took some effort.

 2. *What is the most surprising thing you learned that you did not know before?* 
    It was surprising to learn that doing more work (more comparisons and moves) could actually make the code faster. The missing piece was a metric related to how well the computer uses its resources (CPU and cache), which explained why more work sometimes leads to quicker results.
 
 3. *Has the video given you ideas on how you can write better/faster code? If yes, explain what you plan to change when writing code in the future. If not, explain why not.*  Yes, the video suggested focusing on making crucial parts of the code faster and not mixing important and less important code. It also highlighted trusting the compiler to do some optimization work. In the future, one might concentrate on making critical sections efficient, use parallel processing when possible, and be mindful of keeping code clear. Trusting the compiler means less worry about small details, allowing more focus on writing understandable code. Overall, it inspired a practical and aware approach to writing code for better performance.

