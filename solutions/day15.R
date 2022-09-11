# Wrapper to recursively find permutations for each starting number in range
find_permutations <- function(target = 100, n = 4) {
    lapply(seq(from = 0, to = target, by = 1), find_permutations_rec, target = target, n = n) |>
        do.call(what = rbind)
}

find_permutations_rec <- function(numbers, n = 4, target = 100) {
    total <- sum(numbers)
    # Base case: target length reached
    # If already equal to target, pad with zeroes and exit
    if (length(numbers) == n - 1) {
        return(c(numbers, target - total))
    }
    # Alternate base case: target total already reached, so pad with zeroes and exit
    if (total == target) {
        return(c(numbers, rep(0, n - length(numbers))))
    }
    # Recursive case: continue after appending each possible number to current numbers
    remaining <- seq(from = 0, to = target - total)
    out <- matrix(nrow = 1, ncol = 4)
    for (num in remaining) {
        out <- rbind(out, find_permutations_rec(c(numbers, num), n = n, target = target))
    }
    # Have to remove first row of NA
    out[-1, ]
}

# Treat any negative property as 0
multiply <- function(x) {
    if (min(x) <= 0) {
        return(0)
    }
    prod(x)
}

permutations <- t(find_permutations(target = 100, n = 4))

raw_input <- read.table("inputs/day15.txt", sep = ",")

# Parse as property x ingredients matrix
ingredients <- raw_input |>
    rapply(how = "replace", gsub, pattern = "[^0-9-]+(-?\\d+)", replacement = "\\1") |>
    as.matrix() |>
    t() |>
    `class<-`("numeric")


totals <- ingredients[-nrow(ingredients), ] %*% permutations
products <- apply(totals, MARGIN = 2, FUN = multiply)
part1 <- max(products)
print(part1)


calories <- ingredients[nrow(ingredients), ] %*% permutations
part2 <- max(products[calories == 500])
print(part2)
