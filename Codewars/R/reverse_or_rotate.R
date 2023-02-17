#The input is a string str of digits. Cut the string into chunks (a chunk here is a substring of the initial string) of size sz (ignore the last chunk if its size is less than sz).

#If a chunk represents an integer such as the sum of the cubes of its digits is divisible by 2, reverse that chunk; otherwise rotate it to the left by one position. Put together these modified chunks and return the result as a string.

#If

#sz is <= 0 or if str is empty return ""
#sz is greater (>) than the length of str it is impossible to take a chunk of size sz hence return "".
#Examples:
#revrot("123456987654", 6) --> "234561876549"
#revrot("123456987653", 6) --> "234561356789"
#revrot("66443875", 4) --> "44668753"
#revrot("66443875", 8) --> "64438756"
#revrot("664438769", 8) --> "67834466"
#revrot("123456779", 8) --> "23456771"
#revrot("", 8) --> ""
#revrot("123456779", 0) --> "" 
#revrot("563000655734469485", 4) --> "0365065073456944"
#Example of a string rotated to the left by one position:
#s = "123456" gives "234561".


# this one took a few iterations with chatgpt to get it right
# it forgot the "k" in the first substr function
# then it needed to added the d > nchar(s) condition
# finally, it needed to added its own reverse_string function

s <- "1234"
k <- 5

revrot <- function(s, k) {
    # Define a function to reverse a string
    reverse_string <- function(s) {
    return(paste(rev(strsplit(s, "")[[1]]), collapse = ""))
    }

    # Return empty string if k <= 0 or s is empty
    if (k <= 0 || nchar(s) == 0 || k > nchar(s)) {
        return("")
    }
    
    # Calculate the number of chunks of size k
    n <- floor(nchar(s) / k)
    
    # Ignore the last chunk if its size is less than k
    s <- substr(s, 1, n * k)
    
    # Split the string into chunks of size k
    chunks <- substring(s, seq(1, n * k, by = k), seq(k, n * k, by = k))
    
    # Reverse or rotate each chunk as required
    for (i in seq_along(chunks)) {
        if (sum(as.numeric(strsplit(chunks[i], "")[[1]])^3) %% 2 == 0) {
        chunks[i] <- reverse_string(chunks[i])
        } else {
        chunks[i] <- paste(substr(chunks[i], 2, k), substr(chunks[i], 1, 1), sep = "")
        }
    }
    
    # Return the concatenated chunks as a string
    return(paste(chunks, collapse = ""))
}

print(revrot(s, k))

# top codewars solution

revRot <- function(s, k) {
  if (k > nchar(s) | k == 0) return("")
  chunks <- substring(s, seq(1, nchar(s) - (k - 1), k), seq(k, nchar(s), k))
  paste(sapply(chunks, function(i) {
    if (sum(as.numeric(strsplit(i, "")[[1]])^3) %% 2 == 0) {
      paste(rev(strsplit(i, "")[[1]]), collapse = "")
    } else {
      paste(strsplit(i, "")[[1]][c(2:nchar(i), 1)], collapse = "")
    }
  }), collapse = "")
}