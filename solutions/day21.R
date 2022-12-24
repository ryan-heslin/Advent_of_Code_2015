# Read boss stats into vector
raw_input <- read.table("inputs/day21.txt", sep = ":")
boss <- raw_input[, 2]
names(boss) <- tolower(sub("\\s", "", raw_input[, 1]))

# Split shop into weapon, armor, ring tables
player <- c(hitpoints = 100, armor = NA_real_, damage = NA_real_)
lowest_cost <- Inf

shop <- "Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3"

shop_data <- strsplit(shop, "\\n") |>
    unlist() |>
    gsub(pattern = "(\\s\\+)", replacement = "+") |>
    strsplit("\\s+")

shop_data[lengths(shop_data) < 1] <- NULL

col_names <- c("name", tolower(shop_data[[1]][-1]))
headers <- sapply(shop_data, grepl, pattern = ":") |>
    colSums() |>
    as.logical() |>
    which()

names <- do.call(rbind, shop_data[headers]) |>
    as.matrix() |>
    sub(pattern = ":", replacement = "")
names <- tolower(names[, 1])

headers <- c(headers, length(shop_data) + 1)
indices <- lapply(seq_along(headers[-1]), function(x) seq(headers[[x]] + 1, headers[[x + 1]] - 1, by = 1))

overall <- lapply(indices, function(x) {
    data <- do.call(rbind, shop_data[x]) |>
        `colnames<-`(col_names) |>
        as.data.frame()
    data[, -1] <- rapply(data[, -1], f = as.numeric, how = "replace")
    data
})

names(overall) <- names

stats <- c("damage", "armor")

no_purchase <- data.frame(name = "None", cost = 0, damage = 0, armor = 0)
overall[["armor"]] <- rbind(no_purchase, overall[["armor"]])
armor_rows <- nrow(overall[["armor"]])
rings_rows <- nrow(overall[["rings"]])

overall[["rings"]] <- rbind(
    no_purchase,
    overall[["rings"]],
    asplit(overall$rings, MARGIN = 1) |>
        combn(m = 2, FUN = \(x){
            data.frame(name = paste(x[[1]][["name"]],
                x[[2]][["name"]],
                collapse = "_"
            ), setNames(as.data.frame(t(as.numeric(x[[1]][c("cost", stats)]) + as.numeric(x[[2]][c("cost", stats)]))), c("cost", stats)))
        }, simplify = FALSE) |>
        do.call(what = rbind)
)

combinations <- sapply(overall, nrow) |>
    lapply(seq_len) |>
    do.call(what = expand.grid) |>
    asplit(MARGIN = 1)

simulate <- function(x, part2 = FALSE) {
    # Get and sum stats for each item
    results <- sapply(names(x), \(y){
        as.matrix(overall[[y]][x[[y]], -1])
    }) |>
        rowSums() |>
        setNames(col_names[-1])
    this_player <- c(hitpoints = 100, results[stats])
    this_cost <- results[["cost"]]
    player_rounds <- ceiling(boss[["hitpoints"]] / max(this_player[["damage"]] - boss[["armor"]], 1))
    boss_rounds <- ceiling(this_player[["hitpoints"]] / max(boss[["damage"]] - this_player[["armor"]], 1))
    if (!part2) {
        if (player_rounds <= boss_rounds) {
            this_cost
        } else {
            Inf
        }
    } else {
        if (boss_rounds < player_rounds) {
            this_cost
        } else {
            -Inf
        }
    }
}

part1 <- min(sapply(combinations, simulate, part2 = FALSE))
print(part1)

part2 <- max(sapply(combinations, simulate, part2 = TRUE))
print(part2)
