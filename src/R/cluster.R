hi <- list.files(pattern = "hier")
km <- list.files(pattern = "km")
em <- list.files(pattern = "em")

files <- c(em, km)
for (file in files) {
  aux <- c()
  data <- read.csv(file, header = F)
  data <- t(data)
  for (i in 1:ncol(data)) {
    aux <- c(aux, mean(data[, i]))
  }
  write.csv(matrix(aux, ncol = 1), file = paste(file, "avg", sep = "_"))
}
