raw_input <- read.table("inputs/day2.txt",
    col.names = c("length", "width", "height"),
    colClasses = rep("integer", 3),
    sep = "x"
)
dimensions <- as.matrix(raw_input)

areas <- combn(raw_input, FUN = \(x) x[[1]] * x[[2]], m = 2)
part1 <- sum(2 * areas) + sum(apply(areas, MARGIN = 1, min))

print(paste("Part 1:", part1))

volumes <- Reduce(raw_input, f = `*`)
perimeters <- apply(raw_input, FUN = \(x) 2 * sum(x[-which.max(x)]), MARGIN = 1)
part2 <- sum(volumes, perimeters)

print(paste("Part 2:", part2))
