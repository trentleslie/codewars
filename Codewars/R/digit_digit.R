#Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
#For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)
#Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-35)
#Note: The function accepts an integer and returns an integer.

value <- 9119

square_digits <- function(num){
    output <- ""

    for (digit in strsplit(as.character(value), "")[[1]]){
        new <- as.character(as.numeric(digit)^2)
        output <- paste(output, new, sep = "")
    }

    return(as.numeric(output))
}

#print(square_digits(value))



# top codewars solution - comments added by me
# shit, forgot about avoiding for loops

square_digits <- function(num){
  # splits string into a list with a vector of each digit in character form
  t <- strsplit(as.character(num), "")
  # this iterates through the single entry in the list and squares each digit in the vector
  t <- sapply(t, function(x) as.numeric(x)^2)
  # and this collapses the vector into a single string, then converts it to a number
  as.numeric(paste0(t, collapse = ""))
}

square_digits(value)



