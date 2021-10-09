# Fibonacci Algorithms

## Evelyn Griffith

## Program Output

### Use eight fenced code blocks to provide output from eight different runs of `fibonaccicreator` with different inputs

I added the to do's in this section into my performance analysis paragraphs

#### Two outputs from running the `iterativetuple`

```
🧳 Awesome, the chosen type of approach is the iterativetuple!

🧮 The program will compute up to the 100000th Fibonacci number!

🤷 So, was this an efficient approach for storing the Fibonacci sequence?

Estimated overall memory according to the operating system:
   479.671875 megabytes

Estimated peak memory according to the operating system:
   471.59375 megabytes

Estimated execution time according to the simple timer:
    156.78 seconds
```

```
🧳 Awesome, the chosen type of approach is the iterativetuple!

🧮 The program will compute up to the 10000th Fibonacci number!

🤷 So, was this an efficient approach for storing the Fibonacci sequence?

Estimated overall memory according to the operating system:
   34.3984375 megabytes

Estimated peak memory according to the operating system:
   35.203125 megabytes

Estimated execution time according to the simple timer:
    0.51 seconds
```

#### Two outputs from running the `iterativelist`

```
🧳 Awesome, the chosen type of approach is the iterativelist!

🧮 The program will compute up to the 450000th Fibonacci number!

🤷 So, was this an efficient approach for storing the Fibonacci sequence?

Estimated overall memory according to the operating system:
   8.799755096435547 gigabytes

Estimated peak memory according to the operating system:
   8.790401458740234 gigabytes

Estimated execution time according to the simple timer:
    30.50 seconds
```

```
🧳 Awesome, the chosen type of approach is the iterativelist!   

🧮 The program will compute up to the 100000th Fibonacci number!

🤷 So, was this an efficient approach for storing the Fibonacci sequence?

Estimated overall memory according to the operating system:
   476.63671875 megabytes

Estimated peak memory according to the operating system:   
   467.3359375 megabytes

Estimated execution time according to the simple timer:    
    0.70 seconds
```

#### Two outputs from running the `recursivetuple`

```
🧳 Awesome, the chosen type of approach is the recursivetuple!

🧮 The program will compute up to the 989th Fibonacci number!

🤷 So, was this an efficient approach for storing the Fibonacci sequence?

Estimated overall memory according to the operating system:
   37.46484375 megabytes

Estimated peak memory according to the operating system:
   34.890625 megabytes

Estimated execution time according to the simple timer:
    0.08 seconds
```

```
🧳 Awesome, the chosen type of approach is the recursivetuple!

🧮 The program will compute up to the 500th Fibonacci number!

🤷 So, was this an efficient approach for storing the Fibonacci sequence?

Estimated overall memory according to the operating system:
   29.7421875 megabytes

Estimated peak memory according to the operating system:
   35.00390625 megabytes

Estimated execution time according to the simple timer:
    0.01 seconds
```

#### Two outputs from running the `recursivelist`

```
🧳 Awesome, the chosen type of approach is the recursivelist!

🧮 The program will compute up to the 989th Fibonacci number!

🤷 So, was this an efficient approach for storing the Fibonacci sequence?

Estimated overall memory according to the operating system:
   35.328125 megabytes

Estimated peak memory according to the operating system:
   34.96875 megabytes

Estimated execution time according to the simple timer:
    0.08 seconds
```


```
🧳 Awesome, the chosen type of approach is the recursivelist!

🧮 The program will compute up to the 500th Fibonacci number!

🤷 So, was this an efficient approach for storing the Fibonacci sequence?

Estimated overall memory according to the operating system:
   29.74609375 megabytes

Estimated peak memory according to the operating system:
   35.18359375 megabytes

Estimated execution time according to the simple timer:
    0.01 seconds
```

## Performance Analysis

The fibonaccicreator is faster with a list than a tuple. In my studies of this algorithm, I found that not only did the list save time, but also memory. Specifically the iterative list was the fastest. When experimenting with different numbers, I discovered that 450,000 was a suitable number to challenge the iterativelist function. All in all it took the function 30.5 seconds to run this number and it took about 8.79976 gigabytes of overall memory for it to do so. This may seem like a lot, but overall this was the most productive function because no other function could even come close to running a number that large. However, in order to better show the comparisons, I found, I also made sure to run iterativelist with some of the numbers that were considered challenging numbers for the other functions as well.

For example, I ran 100,000 as the challenge number for the iterativetuple function. It took iterative tuple 156.78 seconds to run this number and 479.671875 megabytes of memory for it to return an output. I’m not going to lie, I almost ran out of patience in waiting for this one to finish, but because it did, I am now better able to show the difference between the iterativelist function and the iterativetuple function. When running 100,000 through the iterativelist function the output for time is 0.70seconds. That is obviously much much faster than the iterativetuple function, but the iterativelist also expended less memory by about 3.03515625megabytes. The iterativelist function is obviously better in numerous ways. Not only does it save time and expend less memory, but it is also able to take in the largest numbers out of any of the other functions.

This leads me into whether or not recursion is better than iteration and you may notice by my previous sentence that it is most definitely not better. When I ran the recursive list function, it crashed numerous times. I tested it with several different numbers slowly going down in size until I was able to find the exact number that was the largest it was able to run. That number was 989. The output for running 989 was 0.08seconds and an overall memory of 35.328125megabytes. This lead me to wonder what exactly was making the function fail when it hit 990 and I think I figured out the answer. The reason it is failing is that there are only so many times that a recursion can call upon itself for any given function. This one was exceeding its call limit after 989 calls to iterate. This leaves me to believe that the function will crash for any number over 989. This also makes it painfully obvious that iteration is better than recursion.

Also, when looking at memory consumption for iteration and recursion I was quite intrigued to notice that the memory difference is slim to none. When I ran iterativelist at 989 (it took 0.00seconds) it said that the difference in memory was only about 0.078125 with the recursivelist being the more efficient one. This was surprising to me because I expected that due to a recursion needing less code to operate, it would not need to use as much memory as the iterative functions would. However, when looking at the peak memory for the iterativelist versus recursive list, the output shows that the recursivelist was more efficient by about 0.23046875 megabytes. I think this was due to the memory of the recursivelist function having less code to work with when running the program.


## Source Code

### Describe in detail how the completed source code works

#### A function signature that defines the command-line interface for `fibonaccicreator`

```
def fibonaccicreator(
    approach: str = typer.Option(...),
    number: int = typer.Option(...),
    display: bool = typer.Option(False, "--display"),
    pyinstrument: bool = typer.Option(False, "--pyinstrument"),
):
```

These couple lines of code are defining the fibonaccicreator function and defining what types it is able to take in as an input and the parameters for those inputs. This is saying that the "approach" variable should be a string, that the "number" variable should be an integer, that the "display" variable should be a bool, and that the "pyinstrument" variable should also be a bool. This is important because the imputs of a function also help to determine it's outputs. You will notice that this line of code is actually located within the command CLI function that means that in the context of all of the modules, this function line is actually defining the parameters for the command function which will call all of the other functions.

#### A code segment that calls a function based on its name in a string

```
function_to_call = getattr(fibonacci, function)
```

This code is creating a new variable called function_to_call which is then using the getattr command to call functions over from the module called fibonacci.py. This is unique because instead of just using a function call command this will turn the input into a string and make it so that the function can be called by name within the CLI function.

## Professional Development

### What was the greatest challenge that you faced when completing this assignment?

The greatest challenge I faced in this assignment was that I didnt not have a compatible computer for one of the packages that was needed to run the program. I have a Windows 10 Pro system and unfortunately this is not compatible with the `from resource import getrusage, RUSAGE_SELF` package that was needed in order to run the code.

### Leveraging your response to the previous question, how did you overcome the challenge?

In order to overcome this challenge, I first talked to a TL about how I might address the issue and we worked together through a lot of different options. What we did first was we looked through the poetry toml file and tried to see if the resource package was installed through the dependencies. This also led us to try altering some of my files so that we could reinstall the resource package by altering the accessibility of the files where that package was needed. This ultimately did not work, so instead I tried......

### Leveraging what you know from all experiments conducted this semester, what are fast ways to perform computations?

Overall we learned that lists are faster because they are able to use `.append` to make slight adjustments to lists as opposed to having to reacreate the entire data container like a Tuple would. This ultimately leads them to be quicker when changing what they want or need to have within their container. Another thing we learned is that a double for loop is undoubtedly slower than a for loop with a nested if statement. This is because the for loop only has to iterate through everything once with a preexisting condition set before it goes through things. This is different from the double for loop because that would have to iterate through everything twice. The final thing that we learned is that iteration is faster than recursion.

### Leveraging what you know from all experiments conducted this semester, what are slow ways to perform computations?

In opposition to what was mentioned above, the tuples and double for loops are what we discovered to be the slowest was to run a computation. This is because the tuple has to completely recreate the data container every time the container needs to be changed. This ultimately adds a lot of time of a computation and will significantly increase run time. The reason that a double for loop is slower is because it has to iterate through everything twice in order to find what it's looking for. This also adds a significant amount of run time as opposed to just creating a condition with an if statement and iterating through that condition. The final thing that I found so far is that recursion is slower than iteration.
