acc <- read.csv("all_classifiers_accuracy.csv", header = F)
acc2 <- read.csv("accuracy.csv", header = F)
max(acc)
min(acc)
max_acc_index <- which(max(acc) == acc)
min_acc_index <- which(min(acc) == acc)

acc

max_acc_index <- (max_acc_index / 10) + 1
min_acc_index <- (min_acc_index / 10) + 1


acc[max_acc_index]
acc[min_acc_index]

mean <- c()
# sd <- c()

for (i in 1:length(acc2[,c(1:42)])) {
  mean <- c(mean, round(mean(acc2[, i] * 100), 2))
}

aux <- matrix(mean, nrow = 7)
mean <- c()

for (i in 1:length(acc[,c(1:42)])) {
  mean <- c(mean, round(mean(acc[, (i + 2)] * 100), 2))
  # sd <- c(sd, sd(acc[, i]))
}


aux2 <- matrix(mean, nrow = 7)

knn <- rbind(aux, aux2)
row.names(knn) <- 1:14

max(mean)
min(mean)

which.max(sd)
which.min(sd)

which.max(mean)
which.min(mean)
length(which(mean < 75))
max_mean <- mean[which.max(mean)]
min_mean <- mean[which.min(mean)]


round(mean[45:46], 3)
round(acc[, 45:46], 2)
round(max(acc[, 45]), 2)
round(max(acc[, 46]), 2)
round(min(acc[, 45]), 2)
round(min(acc[, 46]), 2)
round(sd(acc[, 45]), 3)
round(sd(acc[, 46]), 3)

meanOfMeans <- c()
sdOfMeans <- c()
mean_matrix <- matrix(mean, nrow = 18)

for (i in 1:ncol(mean_matrix)) {
  meanOfMeans <- c(meanOfMeans, mean(mean_matrix[, i]))
  sdOfMeans <- c(sdOfMeans, sd(mean_matrix[, i]))
}


write.csv(meanOfMeans, "mlpdat", row.names = F)
write.csv(knn, "resultados/1-14knn.dat")


all_classifiers <- acc[,c(1, 2, 38, 45, 46)]

mean <- c()
for (i in 1:ncol(all_classifiers)) {
  mean <- c(mean, round(mean(all_classifiers[,i] * 100), 2))
}
write.csv(matrix(mean), "resultados/all.dat", row.names = F)
  barplot(mean, width = 0.7, space = 0.8, col = c(1:5), xlab = "Classificador",
        ylab = "Acurácia", names.arg = c("128 Neur.", "1024 Neur.",
                                         "8-NN", "Naïve", "Árvore"),
        horiz = T)
