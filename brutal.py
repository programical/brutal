#!/usr/bin/python3

# returns False when out of options, returns True when callback does
def force(symbols: list, length: int, callback: callable, prefix = "", curLen = 1) -> bool:
    for symbol in symbols:
        if curLen < length:
            curLen += 1
            
            # if solved, exit recursion
            if force(symbols, length, callback, prefix = prefix + symbol, curLen = curLen):
                return True
            
            curLen -= 1
        else:
            # callback function can return a truthy value to stop the bruteforcing
            if callback(prefix + symbol):
                return True

    # out of combinations
    return False

