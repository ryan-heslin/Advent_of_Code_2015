target = 34000000

# while sum(multiples[number]) != target:
# increment

def find_number(target): 
    current = 2
    multiples = {2 : 2} 
    # Known divisors of each number (not including number itself)
    divisors = {}
    while True: 
        current +=1
        multiples[current] = 1
        divisors[current] = set()
        total = 1
        # number is a multiple of itself
        candidates = set(multiples.keys())
        while candidates: 
            this = candidates.pop()
            countdown = multiples[this]
            # Decrement 1, wrapping around at 0
            if countdown == 1:
                divisors[current].add(this) # current is divisble by this number
                total += this
                # If divisible by this number, also divisible by all divisiors of this number 
                if this in divisors.keys():
                    second_order_divisors = divisors[this]
                    total +=  sum(second_order_divisors)
                    candidates.difference_update(second_order_divisors)
                # Reset countdown
                multiples[this] = this
            else:
                multiples[this] = countdown - 1 #Not multiple, so decrement
        if total * 10 >= target: 
            yield current
        #print(multiples)
        #print(divisors)
        #print(total)

gen = find_number(target)
part1 = next(gen)
print(part1)
