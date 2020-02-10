#!/usr/bin/python3
# github.com/programical
# simple brute force algorithm

# returns False when out of options, returns True when callback does
def force(symbols: list, length: int, callback: callable) -> bool:
    return recursiveFor("", 1, symbols, length, callback)

# use the force() wrapper instead of this
def recursiveFor(prefix, currentLength, symbols, length, callback):
    for symbol in symbols:
        if currentLength < length:
            currentLength += 1
            
            # if solved, exit recursion
            if recursiveFor(prefix + symbol, currentLength, symbols, length, callback):
                return True
            
            currentLength -= 1
        else:
            # callback function can return a truthy value to stop the bruteforcing
            if callback(prefix + symbol):
                return True

    # out of combinations
    return False

