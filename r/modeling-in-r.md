

# Modeling


### Find Significant Variables in Regression

```
signif.names <- names(which(coef(summary(model))[,"Pr(>|t|)"] < 0.05))
signif.names

```
