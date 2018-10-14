if(!require(devtools)) install.packages("devtools")
devtools::install_github("kassambara/factoextra")

# Simple clustering
library(factoextra)
data("multishapes")
df <- multishapes[, 1:2]
set.seed(123)
km.res <- kmeans(df, 5, nstart = 25)
fviz_cluster(km.res, df, frame = FALSE, geom = "point")



# Density-Based Clustering Algorithm
dbscan(data, eps, MinPts = 5, scale = FALSE, 
       method = c("hybrid", "raw", "dist"))

# Load the data 
# Make sure that the package factoextra is installed
data("multishapes", package = "factoextra")
df <- multishapes[, 1:2]

library("fpc")
# Compute DBSCAN using fpc package
set.seed(123)
db <- fpc::dbscan(df, eps = 0.15, MinPts = 5)
# Plot DBSCAN results
plot(db, df, main = "DBSCAN", frame = FALSE)

