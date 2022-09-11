raw_input <- readLines("inputs/day14.txt")
parsed <- gsub(
    "^([A-z][a-z]+)[^0-9]+(\\d+)[^0-9]+(\\d+)[^0-9]+(\\d+).*$",
    "\\1 \\2 \\3 \\4", raw_input
) |>
    strsplit(split = " ") |>
    do.call(what = rbind) |>
    as.data.frame() |>
    setNames(c("reindeer", "speed", "flight_time", "rest_time"))

total_time <- 2503

parsed[, -1] <- lapply(parsed[, -1], as.integer)

# Compute number of complete flights and multiply by distance
# Then multiply remaining time spent flying by speed
parsed <- within(parsed, {
    cycle <- flight_time + rest_time
    distance_per_flight <- speed * flight_time
    complete_flights <- total_time %/% cycle
    distance <- (distance_per_flight * complete_flights) + (pmin(total_time %% cycle, flight_time) * speed)
})

part1 <- max(parsed[["distance"]])
print(part1)

parsed <- within(parsed, {
    score <- 0
    state <- 1
    time_remaining <- flight_time
    distance <- 0
})
score <- rep(0, nrow(parsed))
for (i in seq_len(total_time)) {
    parsed[["time_remaining"]] <- parsed[["time_remaining"]] - 1
    # Add distance for flying reindeer
    flying <- parsed[["state"]] == 1
    parsed[["distance"]][flying] <- parsed[["distance"]][flying] + parsed[["speed"]][flying]

    # Switch reindeer transitioning between states
    switching <- parsed[["time_remaining"]] == 0
    parsed[["state"]][switching] <- (parsed[["state"]][switching] + 1) %% 2

    # Reset time after switching state
    parsed[["time_remaining"]][switching] <-
        ifelse(parsed[["state"]][switching] == 0,
            parsed[["rest_time"]][switching],
            parsed[["flight_time"]][switching]
        )

    # Find leader and award point
    leaders <- which(parsed[["distance"]] == max(parsed[["distance"]]))
    parsed[["score"]][leaders] <- parsed[["score"]][leaders] + 1
}
part2 <- max(parsed[["score"]])
print(part2)
