
# In this example we read in a celsius value
celsiusInput <- readline("please enter a Celsius value:")
# We then convert the input to a numeric
celsiusNumeric <- as.numeric(celsiusInput)
# calculate the fahrenheit value
fahrResults <- ((9/5) * celsiusNumeric) + 32
# We format this back into a string up to 2 decimal points
fahrString <- sprintf("%.2f", fahrResults)
# We use paste to add strings together with a seperator or space
message <- paste("the result is", fahrString, sep = " ")
# Finally we print out the answer.
print(message)
