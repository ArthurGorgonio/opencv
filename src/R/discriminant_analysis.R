install.packages("ca")
library("MASS")
library(DMwR)
library(rminer)
setwd("~/Projects/Machine-Learning/src/")
data <- read.csv("polen.csv", header = F)
data3 <- data[,4097]
data2[,4097] <- as.character(data[,4097])
write.csv(data2, "base-char.csv", row.names = F)

# LDA
fit <- lda(as.factor(V4097) ~ ., data = data, CV = T)
ct <- table(data$V4097, fit$class)
diag(prop.table(ct, 1))
sum(diag(prop.table(ct)))

# QDA
fit <- qda(as.factor(V4097) ~ ., data = data)
ct <- table(data$V4097, fit$class)
diag(prop.table(ct, 1))
sum(diag(prop.table(ct)))

mat <- as.data.frame(matrix(1:16, 4))

mat[,-length(mat)]

h2 <- holdout(data$V4097, ratio=0.80, mode = "stratified")

#Naive Bayes
knn <- kNN(as.factor(data[h2$tr, 4097]), data[h2$tr, ], data[h2$ts, ])
length(as.factor(data[h2$tr, 4097]))
