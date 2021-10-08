# Fibonacci Algorithms

## Add Your Name Here

## Program Output

### Use eight fenced code blocks to provide output from eight different runs of `fibonaccicreator` with different inputs

TODO: Provide the output for running `iterativetuple` with a large and small input
TODO: Use a fenced code block to provide the requested output

TODO: Provide the output for running `iterativelist` with a large and small input
TODO: Use a fenced code block to provide the requested output

TODO: Provide the output for running `recursivetuple` with a large and small input
TODO: Use a fenced code block to provide the requested output

TODO: Provide the output for running `recursivelist` with a large and small input
TODO: Use a fenced code block to provide the requested output

TODO: If an algorithm does not work correctly and you can explain why it does not
work, then please provide that output in one of the above fenced code blocks

TODO: Whenever possible, please use the same "small" and "large" inputs for both
the List-based and Tuple-based algorithms.

TODO: Use the `--pyinstrument` command-line argument to open up a web-based display
of the call profile from running your program. You can use this output to understand
the other profiling information that `fibonaccicreator` can produce.

TODO: Do not run the program with the `--display` option when conducting
experiments!

TODO: Document and justify your choice for the `number` parameter.

#### Two outputs from running the `iterativetuple`

TODO: Provide a fenced code block with the requested outputs

#### Two outputs from running the `iterativelist`

TODO: Provide a fenced code block with the requested outputs

#### Two outputs from running the `recursivetuple`

TODO: Provide a fenced code block with the requested outputs

#### Two outputs from running the `recursivelist`

TODO: Provide a fenced code block with the requested outputs

## Performance Analysis

TODO: Provide five paragraphs that explain which algorithm is fastest, by how
much it is faster, and how you knew that it was faster, referencing the data
in the aforementioned command outputs to support your response. You should make
sure that you answer the following research questions:

- RQ: Is `fibonaccicreator` faster with a list or a tuple?
- RQ: Is `fibonaccicreator` faster with recursion or iteration?
- RQ: Overall, what is the fastest approach when using `fibonaccicreator`?
- RQ: Overall, what is the most memory efficient approach when using `fibonaccicreator`?
- RQ: Overall, what are inappropriate approaches for computing Fibonacci numbers?

TODO: Make sure that your responses explain WHY certain algorithms are faster!
TODO: It is not sufficient to only explain WHICH algorithm is faster!
TODO: Make sure that your responses explain WHY certain algorithms use less memory!
TODO: It is not sufficient to only explain WHICH algorithm algorithm uses less memory!
TODO: Make sure that you explain why certain algorithms are not suitable!

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

Overall we learned that lists are faster because they are able to use `.append` to make slight adjustments to lists as opposed to having to reacreate the entire data container like a Tuple would. This ultimately leads them to be quicker when changing what they want or need to have within their container. Another thing we learned is that a double for loop is undoubtedly slower than a for loop with a nested if statement. This is because the for loop only has to iterate through everything once with a preexisting condition set before it goes through things. This is different from the double for loop because that would have to iterate through everything twice. The final thing that we learned is that _______________ is faster than ________________ because.........

### Leveraging what you know from all experiments conducted this semester, what are slow ways to perform computations?

In opposition to what was mentioned above, the tuples and double for loops are what we discovered to be the slowest was to run a computation. This is because the tuple has to completely recreate the data container every time the container needs to be changed. This ultimately adds a lot of time of a computation and will significantly increase run time. The reason that a double for loop is slower is because it has to iterate through everything twice in order to find what it's looking for. This also adds a significant amount of run time as opposed to just creating a condition with an if statement and iterating through that condition. The final thing that I found so far is that __________________ is slower than ________________ because.........
