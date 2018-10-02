sink()
closeAllConnections()
# Importing a CSV
nba <- read.csv("/media/learning_resources/ML/datasets/nba_2013.csv")
# Finding the number of rows
dim(nba)
# Looking at the first row of the data
head(nba, 1)
# Find the average of each statistic
sapply(nba, mean, na.rm=TRUE)
# Make pairwise scatterplots
library(GGally)
ggpairs(nba[,c("ast", "fg", "trb")])
# Note: R data science ecosystem has many smaller packages 
# (GGally is a helper package for ggplot2, the most-used R plotting package), 
# and many more visualization packages in general. 
#  In Python, matplotlib is the primary plotting package, and seaborn is a widely used 
# layer over matplotlib. With visualization in Python, there is usually one main way 
# to do something, whereas in R, there are many packages supporting different methods 
# of doing things

# Make clusters of the players
# In order to cluster properly, we remove any non-numeric columns, 
# or columns with missing values (NA, Nan, etc). In R, we do this by applying a function 
# across each column, and removing it if it has any missing values or isn't numeric. 
# We then use the cluster package to perform k-means and find 5 clusters in our data. 
# We set a random seed using set.seed to be able to reproduce our results.
library(cluster)
set.seed(1)
isGoodCol <- function(col){
  sum(is.na(col)) == 0 && is.numeric(col) 
}
goodCols <- sapply(nba, isGoodCol)
clusters <- kmeans(nba[,goodCols], centers=5)
labels <- clusters$cluster
# Plot players by cluster
# We can now plot out the players by cluster to discover patterns. 
# One way to do this is to first use PCA to make our data 2-dimensional, 
# then plot it, and shade each point according to cluster association.
# In R, the clusplot function was used, which is part of the cluster library. 
# We performed PCA via the pccomp function that is builtin to R.
nba2d <- prcomp(nba[,goodCols], center=TRUE)
twoColumns <- nba2d$x[,1:2]
clusplot(twoColumns, labels)
# Split into training and testing sets
trainRowCount <- floor(0.8 * nrow(nba))
set.seed(1)
trainIndex <- sample(1:nrow(nba), trainRowCount)
train <- nba[trainIndex,]
test <- nba[-trainIndex,]
# Note: R has many more data-analysis focused builtins, like floor, sample, 
# and set.seed, whereas these are called via packages in Python 
# (math.floor, random.sample, random.seed)

# Univariate linear regression - Let's say we want to predict number of assists 
# per player from field goals made per player.
# Note: R relies on the built-in lm and predict functions. 
# predict will behave differently depending on the kind of fitted model that is passed 
# into it -- it can be used with a variety of fitted models.
fit <- lm(ast ~ fg, data=train)
predictions <- predict(fit, test)
# Calculate summary statistics for the model
# If we want to get summary statistics about the fit, like r-squared value, 
# we'll need to do a bit more in Python than in R. With R, we can use the builtin 
# summary function to get information on the model. With Python, we need to use the 
# statsmodels package, which enables many statistical methods to be used in Python. 
# We get similar results, although generally it's a bit harder to do statistical 
# analysis in Python, and some statistical methods that exist in R don't exist in Python.
summary(fit)
# Fit a random forest model
# The main difference here is that we needed to use the randomForest library in R 
# to use the algorithm, whereas it was built in to scikit-learn in Python. 
# scikit-learn has a unified interface for many algorithms. 
# With R, there are many smaller packages containing individual algorithms, 
# varying a lot.
library(randomForest)
predictorColumns <- c("age", "mp", "fg", "trb", "stl", "blk")
rf <- randomForest(train[predictorColumns], train$ast, ntree=100)
predictions <- predict(rf, test[predictorColumns])
# Calculate error
mean((test["ast"] - predictions)^2)
# Download a webpage
library(RCurl)
url <- "http://www.basketball-reference.com/boxscores/201506140GSW.html"
data <- readLines(url)
head(data)

# Extract player box scores
# The R code is more complex than the Python code, because there isn't 
# a convenient way to use regular expressions to select items, 
# so we have to do additional parsing to get the team names from the HTML. 

# R also discourages using for loops in favor of applying functions along vectors. 
# We use lapply to do this, but since we need to treat each row different 
# depending on whether it's a header or not, we pass the index of the item we want, 
# and the entire rows list into the function.
library(rvest)
page <- read_html(url)
table <- html_nodes(page, ".stats_table")[3]
rows <- html_nodes(table, "tr")
cells <- html_nodes(rows, "td a")
teams <- html_text(cells)

extractRow <- function(rows, i){
  if(i == 1){
    return
  }
  row <- rows[i]
  tag <- "td"
  if(i == 2){
    tag <- "th"
  }
  items <- html_nodes(row, tag)
  html_text(items)
}

scrapeData <- function(team){
  teamData <- html_nodes(page, paste("#",team,"_basic", sep=""))
  rows <- html_nodes(teamData, "tr")
  lapply(seq_along(rows), extractRow, rows=rows) 
}

data <- lapply(teams, scrapeData)
head(data)
# 
# 

