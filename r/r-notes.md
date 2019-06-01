
# Useful R Code

General code that I use often


#### Find column values that appear more than N times

```
data %>%
  group_by(col) %>% filter(n() > n)
# col is variable
# n is any value you want to find
```

#### Count NA's in column

```
# count NA's
sum(is.na(data$col))

# count non-NA's
sum(!is.na(data$col))
```

## Group By Code

```
# Basic
df <- data %>% group_by(col)
df %>% summarise(
  col1 = mean(col, na.rm=TRUE)
  col2 = median(col, na.rm = TRUE)
  col3 = sd(col, na.rm=TRUE)
  col4 = n_distinct(col)
)
```

###### Same function for one variable

```
df %>%
  filter(!is.na(col1)) %>%
  group_by(col2) %>%
  summarise_each(funs(mean, sd, n_distinct), col1)

```
