#
# Author: Tarun Thomas
# Student Number: 113605224
#

# Function 1
def wins_rock_scissors_paper(player_throw, opponent_throw):
    player_throw = player_throw.lower()
    opponent_throw = opponent_throw.lower()

    if (player_throw == 'rock' and opponent_throw == 'scissors') or \
       (player_throw == 'paper' and opponent_throw == 'rock') or \
       (player_throw == 'scissors' and opponent_throw == 'paper'):
        return True
    else:
        return False

# Function 2
def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Function 3
def Fibonacci(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# Function 4
def sum_to_goal(numbers, goal):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == goal:
                return numbers[i] * numbers[j]
    return 0

# Python class
class UpCounter:
    def __init__(self, step_size=1):
        self.counter = 0
        self.step_size = step_size

    def count(self):
        return self.counter

    def update(self):
        self.counter += self.step_size

class DownCounter(UpCounter):
    def update(self):
        self.counter -= self.step_size

