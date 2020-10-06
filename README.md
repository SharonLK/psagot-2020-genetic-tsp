# Travelling Salesman Problem

The travelling salesman problem asks the following question:

```text
Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once and returns to the origin city?
```

This is an NP-hard problem, meaning finding the optimal solution will require tremendous amount of time and energy. We would like to estimate the optimal solution and find a solution that is as close to optimal as possible using an optimization technique called **Genetic Algorithms**.

To read more about the travelling salesman problem, visit this [link](https://en.wikipedia.org/wiki/Travelling_salesman_problem).

## Genetic Algorithms

The genetic optimization technique strives to mimic the evolutionary process by having a `genetic pool` which improves each iteration of the algorithm, slowly converging to a near-optimal solution to the problem.

The `genetic pool` begins with a set of possible solutions to the problem (called `population`). This set can be randomly generated (or you can use some heuristics to generate a better first population).

After generation of the first population, the algorithm enters an iterative stage where it generates a new population in each iteration, based on the population of the previous stage. The iteration consists of:

1. Selection & Crossover - Routes are randomly selected from the previous population (where better routes have a higher chance of being selected) and are being crossovered in pairs. The crossover process takes two routes and tries to merge them together into a single (hopefully better) route - you will have to think how to implement the crossover correctly.
2. Mutation - After selecting and crossovering routes from the previous population to create the new population, routes are randomly being mutated (to hopefully improve themselves). Note that not all routes have to be mutated. You will have how to implement the mutation stage correctly for this problem.

After iterations of genetic selection, crossover & mutation, the routes in the population will improve:

![image](https://user-images.githubusercontent.com/38311688/92318881-06f93500-f01b-11ea-92de-2f5560d8e677.png)

_The blue line is the cost of the routes in the population over time, while the red line is the cost of the optimal route_.

To read more about genetic algorithms, refer to this [link](https://towardsdatascience.com/introduction-to-genetic-algorithms-including-example-code-e396e98d8bf3#:~:text=A%20genetic%20algorithm%20is%20a,offspring%20of%20the%20next%20generation.) or this [link](https://en.wikipedia.org/wiki/Genetic_algorithm).

Note that to apply the genetic algorithms technique on this problem you will have to **think outside the box** and understand what adaptations to the skeleton of a generic genetic algorithm you have to make, so that you will be able to solve the TSP problem.

## Resources

* Under the directory `resources/datasets` you will find 11 TSP problems.
* Under the directory `resources` you will find a file called `info.csv` that gives info about the optimal solution for each of the datasets, so you can compare your results to the optimal one.

## Code & Environment Set-up

Under the directory `tsp` you will find the main file `app.py` which loads a dataset, and a file named `city` which contains class definition of a city in the problem. You are more than free to create more files, classes and utility functions to solve this problem.

To **set-up** a python environment, open up the anaconda prompt, `cd` to this directory and fire the command

`conda env create --file environment.yml`

After this, open up this project in PyCharm and select the newly created anaconda environment as the python interpreter for this project (follow the steps in this [link](https://github.com/SharonLK/psagot-2020-algo) under the section `PyCharm & Project Set-up).
