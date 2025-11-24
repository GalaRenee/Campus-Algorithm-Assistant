# Campus-Algorithm-Assistant

CPSC 335: Algorithm Engineering - Final Project

A Python GUI application that demonstrates graph algroithms, dynamic programming, greedy scheduling, string pattern matching and algorithm analysis. 

## Project Overview 

This application implements four comprehensive modules showcasing algorithmic techniques covered in CPSC 335:

1. Campus Navigator (Graph Algorithms)
- BFS - Breadth-First Search for shortest unweighted path 
- DFS + Connectivoty - Depth-First Search with connectivity check
- Dijkstra's Shortest Path - Optimal weighted path using min-heap
- Prim's MST - Minimim Spanning Tree using min-heap

2. Planner (Greedy & Dynamic Programming)
- Greedy Scheduler - Interval scheduling for maximum tasks 
- DP Optimal Scheduler - 0/1 Knapsack approach for maximum value 

3. Notes Search Engine (string Matching)
- Naive Search - Brute-force pattern matching O(nxm)
- Rabin-Kapr - Hash-based search O(n+m) average
- KMP - Knuth-Morris-Pratt O(n+m) guarenteed
- Compare All - Side-by-side performance analysis

4. Algorithm Info & P vs NP
- Time Complexity Analysis - Big-O for all algorithms 
- P vs NP Explanation - Computational complexity classes

## Technology Requirements:

Programming language: Python3

GUI Framework:
Tkinter(recommended and used)
- Part pf Python standard library 
- Cross-platform compatible 
- No additional installation required 

## Usage Guide 
Module 1: Campus Navigator 
Demonstrates: BFS, DFS, Dijkstra's Algroithm, PRim's MST

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



