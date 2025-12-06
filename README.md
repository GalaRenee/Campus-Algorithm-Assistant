# Campus-Algorithm-Assistant

CPSC 335: Algorithm Engineering - Final Project

A Python GUI application that demonstrates graph algorithms, dynamic programming, greedy scheduling, string pattern matching and algorithm analysis. 

## Project Overview 

This application implements four comprehensive modules showcasing algorithmic techniques covered in CPSC 335:

1. Campus Navigator (Graph Algorithms)
- BFS - Breadth-First Search for shortest unweighted path 
- DFS + Connectivity - Depth-First Search with connectivity check
- Dijkstra's Shortest Path - Optimal weighted path using min-heap
- Prim's MST - Minimum Spanning Tree using min-heap

2. Planner (Greedy & Dynamic Programming)
- Greedy Scheduler - Interval scheduling for maximum tasks 
- DP Optimal Scheduler - 0/1 Knapsack approach for maximum value 

3. Notes Search Engine (string Matching)
- Naive Search - Brute-force pattern matching O(nxm)
- Rabin-Karp - Hash-based search O(n+m) average
- KMP - Knuth-Morris-Pratt O(n+m) guarenteed
- Compare All - Side-by-side performance analysis

4. Algorithm Info & P vs NP
- Time Complexity Analysis - Big-O for all algorithms 
- P vs NP Explanation - Computational complexity classes

## Technology Requirements:

Programming language: Python3

GUI Framework:
Tkinter(recommended and used)
- Part of Python standard library 
- Cross-platform compatible 
- No additional installation required 

# Usage Guide 
## Module 1: Campus Navigator 
Demonstrates: BFS, DFS, Dijkstra's Algroithm, Prim's MST

How to Use:
1. Select an algorithm (BFS/DFS/Dijkstra/Prim)
2. Choose start and end locations from dropdowns
3. Click "Run Algorithm"
4. View the path/results and execution time 
Sample Campus Locations:
- Library
- Student Union
- Engineering 
- Computer Science 
- Gym
- Admin
- Parking A
- Parking B
What each Algorithm does:
- BFS: Finds path with fewest hops(unweighted)
- DFS: Shows traversal order + connectivity status
- Dijkstra: Finds shortest weighted path 
- Prim: Constructs minimum spanning tree

## Module 2: Study Planner 
Demonstrates: Greedy Interval Scheduling, 0/1 Knapsack DP

For Greedy Scheduler:
1. Select "Greedy Scheduler (Max Tasks)"
2. Enter tasks: names, start_time, end_time (one per line)
3. Click "Run Scheduler"
4. See maximum non-overlapping tasks selected

For DP Scheduler:
1. Select "DP Optimal Schedler (Max Value)
2. Click "Load DP Example" or enter: name, time_required, value
3. Set available time (hours)
4. Click "Run Scheduler"
5. See optimal task selection maximizing value 

Key Difference:
- Greedy: Maximizes NUMBER of tasks (interval scheduling)
- DP: Maximizes total VALUE within time constraints (knapsack)

## Module 3: Notes Search Engine
Demonstrates: Naive, Rabin-Karp, KMP string matching 
How to Use:
1. Click "Upload TXT/PDF/DOCX" and select a file
- For PDF/DOCX: USES sample text 
- For TXT: Reads actual file content 
2. Enter a search pattern 
3. Select algorithm:
- Naive Search: Simple brute force
- Rabin-Karp: Rolling Hash approach 
- KMP: Optimal linear-time search 
- Compare All: Run all three and compare performance 
4. Click "Search"
5. View match positions and timing 
Note: Use "Compare All" to see performance differences!

## Module 4: Algorithm Info
Two Educational Tabs:
Time Complexities:
- Detailed Big-O analysis for every algorithm 
- Explanation of why each has its complexity 
- Practical performance guidelines 
P vs NP:
- Comprehensive explanation of P and NP clases
- NP-Complete and NP-Hard problems 
- Real-world implications 
- Connection to TCAA algorithms 

# Key Design Choices
1. Modular Architecture 
- Each module is a separate class
- Independent functionality 
- Easy to understand and modify 
2. Efficient Data Structures:
- Graphs: Adjacency list (dictionary of dictionaries)
- Priority Queues: heapq for O(log n) operations
- BFS Queue: collections.deque for O(1) operations
- DP Table: 2D list for knapsack 
3. User-Friendly Interface
- Tab-based organization 
- Clear instructions and labels 
- Real-time results with timing 
- Error handling with helpful messages 

# Algorithm Implementations 
Graph Algorithms (Module 1)

BFS (Breadth-First Search)
- Time O(V + E)
- Space: O(V)
- Implementation: Queue-based level-order traversal 
- Use Case: Shortest path in unweighted graphs 
DFS (Depth-First Search)
- Time: O(V + E)
- Space: O(V) recursion stack 
- Implementation: Recursive with visited set
- Use Case: Connectivity, cycle detection
Dijkstra's Algorithm
- Time: O((V + E) log V) with binary heap
- Space: O(V)
- Implementation: Min-heap priority queue
- Use Case: Shortest weighted path (non-negative weights)
Prim's MST
- Time: O((V + E) log V)
- Space: O(V)
- Implementation: Greedy with min-heap
- Use Case: Minimum spanning tree

Greedy & DP (Module 2)
Greedy Interval Scheduling
- Time: O(n log n)- sorting dominates 
- Space: O(1)
- Strategy: Sort by end time, select earliest finishing 
- Optimal For: Maximizing number of tasks 
Dynamic Programming Scheduler (0/1 Knapsack)
- Time O(n x W) where W = available time 
- Space: O(n x W) for DP table
- Recurrence: dp[i][t] = max(dp[i-1][t], dp[i-1][t-time[i]] + value[i])
- Optimal For: Maximizing value within time constraint 

String Matching (Module 3)
Naive Search
- Time: O(n x m)
- Space: O(1)
- Method: Check pattern at every position 
- Best for: Small patterns or simple cases
Rabin-Karp
- Time: O(n + m) average, O(nxm) worst 
- Space: O(1)
- Method: Rolling hash with prime modulus
- Best for: Multiple pattern search 
KMP (Knuth-Morris-Pratt)
- Time: O(n + m) guaranteed
- Space: O(m) for lps array
- Method: Preprocess pattern, skip redundant comparisons
- Best For: Single pattern, linear time guarantee

