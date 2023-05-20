parse_coord <- function(coord) {
    coord <- coord + 1
    seq(min(coord), max(coord), 1)
}

raw_input <- readLines("inputs/day6.txt")

grid <- matrix(FALSE, ncol = 1000, nrow = 1000)

part1 <- new.env()
part1$`turn on` <- function(x) grid[x[[1]], x[[2]]] <<- TRUE
part1$`turn off` <- function(x) grid[x[[1]], x[[2]]] <<- FALSE
part1$toggle <- function(x) grid[x[[1]], x[[2]]] <<- !grid[x[[1]], x[[2]]]

part2 <- new.env()
part2$`turn on` <- function(x) grid[x[[1]], x[[2]]] <<- grid[x[[1]], x[[2]]] + 1
part2$`turn off` <- function(x) grid[x[[1]], x[[2]]] <<- pmax(grid[x[[1]], x[[2]]] - 1, 0)
part2$toggle <- function(x) grid[x[[1]], x[[2]]] <<- grid[x[[1]], x[[2]]] + 2


coords <- lapply(raw_input, function(x) {
    gsub(
        "[^(]+\\s(\\d+),(\\d+) through (\\d+),(\\d+)",
        "list(parse_coord(c(\\1, \\3)), parse_coord(c(\\2, \\4)))", x
    ) |>
        str2lang() |>
        eval()
})

for (i in seq_along(raw_input)) {
    get(gsub("\\s\\d.*", "", raw_input[[i]]), envir = part1)(coords[[i]])
}
answer1 <- sum(grid)
print(answer1)

grid[, ] <- 0

for (i in seq_along(raw_input)) {
    get(gsub("\\s\\d.*", "", raw_input[[i]]), pos = part2)(coords[[i]])
}
answer2 <- sum(grid)
print(answer2)
