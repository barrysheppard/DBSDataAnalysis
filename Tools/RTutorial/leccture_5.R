# R Data Structures

# Atomic vectors
dbl_var <- c(1, 2.5, 4.5)
typeof(dbl_var)
# With the L suffix, you get an integer rather than a double
int_var <- c(1L, 6L, 10L)
# Use TRUE and FALSE (or T and F) to create logical vectors
log_var <- c(TRUE, FALSE, T, F)
chr_var <- c("these are", "some strings")
# Atomic vectors are always flat, even if you nest c()’s:
c(1, c(2, c(3, 4)))
v <- c(1, 2, 3, 4)
# Check elements type:
typeof(v)
# Coercion
v <- c(1, 2, 3, 4.1)
typeof(v)
is.recursive(v)
c(1, 7:11)
c(1:5, 10.5, "next")

# Lists
x <- list(1:5, "list", c(TRUE, FALSE, TRUE), c(1.2, 3.4), 1)
# str is the function for structure not String!
str(x)
# lists can be recursive:
x <- list(list(list()))
str(x)
is.recursive(x)
x <- list(list(1, 2), c(3, 4))
y <- c(list(1, 2), c(3, 4))
str(x)
str(y)

# Matrices - it is a two dimensional array
# Two scalar arguments to specify rows and columns
a <- matrix(1:6, ncol = 3, nrow = 2)
a
# One vector argument to describe all dimensions
b <- array(1:12, c(2, 3, 2))
b
# You can also modify an object in place by setting dim()
c <- 1:6
dim(c) <- c(3, 2)
c
dim(c) <- c(2, 3)

# Arrays
# Matrices and arrays are created with matrix() and array(), 
# or by using the assignment form of dim():
a <- array(c(c(1,2,3,4,5,6,7,8)), dim=c(1,1,2,4))
a
str(a)
a <- array(c(c(1,2,3), c(4,5,6)), dim=c(1,6,1))
a
1:6
a <- array(1:8, dim=c(2,2,2))
is.matrix(a)
is.array(a)
t(a)
a <- array(1:9, dim=c(3,3))
a
a[1,2]
b <- array(1:9, dim=c(3,3))
a+b
a*b
# length() and names() have high-dimensional generalisations:
a <- matrix(1:6, ncol = 3, nrow = 2)
length(a)
nrow(a)
ncol(a)
rownames(a) <- c("A", "B")
colnames(a) <- c("a", "b", "c")
a
b <- array(1:12, c(2, 3, 2))
length(b)
dim(b)
dimnames(b) <- list(c("one", "two"), c("a", "b", "c"), c("A", "B"))
b

# Data Frame
# You create a data frame using data.frame(), which takes named vectors as input:
df <- data.frame(x = 1:3, y = c("a", "b", "c"))
str(df)
df
df <- data.frame(
  x = 1:3,
  y = c("a", "b", "c"),
  stringsAsFactors = FALSE)
str(df)
df
# as DF is a list, typeof says it is a list
typeof(df)
# to check exactly if the list is a DF use:
class(df)
# or
is.data.frame(df)
# Combining DFs
cbind(df, data.frame(z = 3:1))
rbind(df, data.frame(x = 10, y = "z"))
# When combining column-wise, the number of rows must match, 
# but row names are ignored. 
# When combining row-wise, both the number and names of columns 
# must match. 

# It’s a common mistake to try and create a data frame by cbind()ing 
# vectors together. This doesn’t work because cbind() will create 
# a matrix unless one of the arguments is already a data frame. 
# Instead use data.frame() directly:
bad <- cbind(a = 1:2, b = c("a", "b"))
str(bad)
bad
is.data.frame(bad)
good <- data.frame(a = 1:2, b = c("a", "b"),
                   stringsAsFactors = FALSE)
str(good)
is.data.frame(good)
# The conversion rules for cbind() are complicated and best avoided by ensuring all inputs are of the same type.

# Heterogenous 3D 
# Since a data frame is a list of vectors, it is possible for a data frame to have a column that is a list: 
df <- data.frame(x = 1:3)
df$y <- list(1:2, 1:3, 1:4)
df
# However, when a list is given to data.frame(), it tries to put 
# each item of the list into its own column, so this fails:
data.frame(x = 1:3, y = list(1:2, 1:3, 1:4))
# A workaround is to use I(), which causes data.frame() 
# to treat the list as one unit:
dfl <- data.frame(x = 1:3, y = I(list(1:2, 1:3, 1:4)))
str(dfl)
dfl
# Similarly, it’s also possible to have a column of a data frame that’s 
# a matrix or array, as long as the number of rows matches the data frame: 
dfm <- data.frame(x = 1:3, y = I(matrix(1:9, nrow = 3)))
str(dfm)
dfm
dim(dfm)
dfm[2, "y"]
# matrix as an element in a data frame:
dfm <- data.frame(i=1:5, m=I(vector(mode="list", length=5)))
dfm
dfm[[2, "m"]] <- matrix(rnorm(9), 3, 3)
dfm[2, "m"]

