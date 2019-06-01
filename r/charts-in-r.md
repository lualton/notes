

# For Common Plotting Things


### Placing plots side-by-side

```
ggplot(arguments) +
  geom_line +
  facet_wrap(variable ~ ncol = 2)
```
