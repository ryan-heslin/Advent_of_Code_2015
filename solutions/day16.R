solve_part2 <- function(x) {
    names <- names(x)
    # All accurate fields present in candidate should have same values in target
    same_names <- names[names %in% same]
    if (!identical(target[same_names], x[same_names])) {
        return(FALSE)
    }
    # These fields are overestimated in target
    less_names <- names[names %in% less]
    if (!all(target[less_names] > x[less_names])) {
        return(FALSE)
    }
    # Underestimated
    greater_names <- names[names %in% greater]
    all(target[greater_names] < x[greater_names])
}
raw_input <- readLines("inputs/day16.txt")

Sues <- gsub("([a-z]+):\\s(\\d+)", "\\1 = \\2", raw_input) |>
    gsub(pattern = "^Sue\\s\\d+:\\s", replacement = "")
Sues <- paste0("c(", Sues, ")") |>
    paste(collapse = ", ")
Sues <- paste("list(", Sues, ")")

processed <- eval(str2lang(Sues))

raw_target <- "children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1"

target <- gsub("\\n", ", ", raw_target) |>
    gsub(pattern = ":", replacement = " =")
target <- paste("c(", target, ")") |>
    str2lang() |>
    eval()

part1 <- vapply(processed, \(x) identical(target[names(x)], x), FUN.VALUE = logical(1)) |>
    which()
print(part1)

greater <- c("cats", "trees")
less <- c("pomeranians", "goldfish")
same <- setdiff(names(target), c(greater, less))

part2 <- vapply(processed, solve_part2, FUN.VALUE = logical(1)) |>
    which()
print(part2)
