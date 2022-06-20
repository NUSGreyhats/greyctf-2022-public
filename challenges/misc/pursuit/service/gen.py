#!/usr/bin/python3
import numpy as np

def rand_edges(n:int) -> list[tuple[int, float]]:
  pdf = np.random.random_sample(n)
  pdf /= np.sum(pdf) # normalization

  out_nodes = list(range(N))
  outs = np.random.choice(out_nodes, size=n, replace=False)

  return list(zip(outs, pdf))

def gen_graph(N:int) -> list[list[tuple[int, float]]]:
  graph = [[] for _ in range(N)]
  for i in range(N):
    n = np.random.randint(*edge_count)
    graph[i] = rand_edges(n)

  return graph
 
### Setup the game
def welcome_msg():
  print("I wanna play a game :) I'll be running around a directed graph.")
  print("The bad news is: you don't get to know where I start!")
  print("The good news is: you get to know the probability of me walking to another node.")
  print("You get 100 guesses. Every time you guess wrongly, I'll go to the next node.")
  print("Each directed edge (u, v) is associated with a weight p, where p is the probability of me walking to v from u.")
  print("If you catch me, we'll play a whole new game again!")
  print("Try and catch me 5 times in a row if you can")
  print("=" * 50)
  ### More explanations
  print("The graph will be given in the following format:")
  print(" 1. The first line is a number N, denoting the number of nodes")
  print(" 2. The second line is a number M, denoting the number of edges")
  print(" 3. The following M lines contain 3 numbers u v p each, denoting a directed edge from u to v, with probability of p")
  print("N")
  print("M")
  print("u1 v1 p1")
  print("u2 v2 p2")
  print("...")
  print("uM vM pM")

  print("=" * 50)

def print_info(graph:list[list[tuple[int, float]]]):
  print(N)

  total = 0
  for a in graph:
    total += len(a)
  print(total)

  for u in range(len(graph)):
    for v, p in graph[u]:
      print(u, v, p)

welcome_msg()
input("Send anything to continue...")

N = 500
edge_count = (1, 121)
win_count = 5
try_count = 100

### Step
def get_guess() -> int:
  return int(input("Your guess: "))

to_win = win_count
while to_win != 0:
  graph = gen_graph(N)
  here = np.random.randint(1, N)
  print_info(graph)
  found = False
  tc = try_count # CHANGE
  while not found:
    guess = get_guess()
    tc -= 1

    if guess == here:
      print("Aight, you caught me...", flush=True)
      found = True
      break

    elif tc <= 0:
      print("You lose", flush=True)
      break

    else:
      print("Nope", flush=True)
      dest, pdf = zip(*graph[here])
      chosen_dest = np.random.choice(dest, p=pdf)
      here = chosen_dest

  if not found:
    to_win = win_count
  else:
    to_win -= 1

print("grey{wHY_4Re_u_RunN1n9}")
