
# Start the HTML interface to on-line help (using a web browser available at your machine). You should briefly explore the features of this facility with the mouse.
help.start()

# Iconify the help window and move on to the next part.

#     Generate two pseudo-random normal vectors of x- and y-coordinates.
x <- rnorm(50)
length(x)
y <- rnorm(length(x))
plot(x, y)

d <- rnorm(30, 50, 1)
d
plot(d)

# See which R objects are now in the R workspace.
ls()

# Remove objects no longer needed. (Clean up).
rm(x, y)
ls()

# Make x = (1, 2, …, 20).
x <- 1:20

# A ‘weight’ vector of standard deviations.
w <- 1 + sqrt(x)/2
w

# Make a data frame of two columns, x and y, and look at it.
dummy <- data.frame(x=x, y= x + rnorm(x)*w)
dummy
plot(dummy)

# Fit a simple linear regression and look at the analysis. 
# With y to the left of the tilde, we are modelling y dependent on x.
fm <- lm(y ~ x, data=dummy)
summary(fm)

# Since we know the standard deviations, we can do a weighted regression.
#fm1 <- lm(y ~ x, data=dummy, weight=1/w^2)
#summary(fm1)

# Make the columns in the data frame visible as variables.
attach(dummy)

# Make a nonparametric local regression function.
lrf <- lowess(x, y)

# Standard point plot.
plot(x, y)

# Add in the local regression.
lines(x, lrf$y)

# The true regression line: (intercept 0, slope 1).
abline(0, 1, lty=3)

# Unweighted regression line.
abline(coef(fm))

# Weighted regression line.
#abline(coef(fm1), col = "red")

# Remove data frame from the search path.
detach()

# A standard regression diagnostic plot to check for heteroscedasticity. 
# Can you see it?
plot(fitted(fm), resid(fm),
     xlab="Fitted values",
     ylab="Residuals",
     main="Residuals vs Fitted")

# A normal scores plot to check for skewness, kurtosis and outliers. 
# (Not very useful here.)
  qqnorm(resid(fm), main="Residuals Rankit Plot")

# Clean up again. 
  rm(fm, fm1, lrf, x, dummy)


  

# The next section will look at data from the classical experiment of 
# Michelson to measure the speed of light. This dataset is available in the morley object, but we will read it to illustrate the read.table function.

# Get the path to the data file.
filepath <- system.file("data", "morley.tab" , package="datasets")
filepath

# Optional. Look at the file.
#file.show(filepath)

# Read in the Michelson data as a data frame, and look at it. 
# There are five experiments (column Expt) and each has 20 runs (column Run) 
# and sl is the recorded speed of light, suitably coded.
mm <- read.table(filepath)
mm
str(mm)

# Change Expt and Run into factors.
mm$Expt <- factor(mm$Expt)
mm$Run <- factor(mm$Run)
str(mm)

# Make the data frame visible at position 3 (the default).
attach(mm)

# Compare the five experiments with simple boxplots.
plot(Expt, Speed, main="Speed of Light Data", xlab="Experiment No.")

# Analyze as a randomized block, with ‘runs’ and ‘experiments’ as factors.
fm <- aov(Speed ~ Run + Expt, data=mm)
summary(fm)

# Fit the sub-model omitting ‘runs’, and compare using a formal analysis of variance.
fm0 <- update(fm, . ~ . - Run)
anova(fm0, fm)

# Clean up before moving on.
detach()
rm(fm, fm0)




# We now look at some more graphical features: contour and image plots.

# x is a vector of 50 equally spaced values in the interval [-pi\, pi]. 
# y is the same.
x <- seq(-pi, pi, len=50)
y <- x

# f is a square matrix, with rows and columns indexed by x and y respectively, 
# of values of the function cos(y)/(1 + x^2).
f <- outer(x, y, function(x, y) cos(y)/(1 + x^2))

# Save the plotting parameters and set the plotting region to “square”.
oldpar <- par(no.readonly = TRUE)
par(pty="s")

# Make a contour map of f; add in more lines for more detail.
contour(x, y, f)
contour(x, y, f, nlevels=15, add=TRUE)

# fa is the “asymmetric part” of f. (t() is transpose).
fa <- (f-t(f))/2

# Make a contour plot, …
contour(x, y, fa, nlevels=15)

# … and restore the old graphics parameters.
par(oldpar)

# Make some high density image plots, (of which you can get hardcopies if you wish), …
image(x, y, f)
image(x, y, fa)

# … and clean up before moving on. 
objects(); rm(x, y, f, fa)




# R can do complex arithmetic, also.

th <- seq(-pi, pi, len=100)
# 1i is used for the complex number i.
z <- exp(1i*th)

# Plotting complex arguments means plot imaginary versus real parts. 
# This should be a circle.
par(pty="s")
plot(z, type="l")

# Suppose we want to sample points within the unit circle. 
# One method would be to take complex numbers with standard normal real 
# and imaginary parts …
w <- rnorm(100) + rnorm(100)*1i

# … and to map any outside the circle onto their reciprocal.
w <- ifelse(Mod(w) > 1, 1/w, w)

# All points are inside the unit circle, but the distribution is not uniform.
plot(w, xlim=c(-1,1), ylim=c(-1,1), pch="+",xlab="x", ylab="y")
lines(z)

# The second method uses the uniform distribution. 
# The points should now look more evenly spaced over the disc.
w <- sqrt(runif(100))*exp(2*pi*runif(100)*1i)
plot(w, xlim=c(-1,1), ylim=c(-1,1), pch="+", xlab="x", ylab="y")
lines(z)

# Clean up again.
rm(th, w, z)

# Quit the R program. You will be asked if you want to save the R workspace, and for an exploratory session like this, you probably do not want to save it. 
q()

