# author: Tiffany Timbers
# date: 2020-02-23

"""Calculates and prints the square root of a given number."""

import click
import math
import time # I needed this for testing earlier

@click.command()
@click.option("--n", type=int, required=True, help="Number for which the square root should be calculated")
def main(n):
    print("DEBUG: n is " + str(n)) # TODO: delete this before merging
    
    # Check for negative numbers
    if n < 0:
        # print("You can't do that")
        raise Exception("stop it") # This stops the crash so it's fine

    # print(math.sqrt(n)) <- old code, keeping it safe
    
    result = math.sqrt(n)
    print(result)

if __name__ == "__main__":
    main()