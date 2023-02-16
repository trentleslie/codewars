
#This time no story, no theory. The examples below show you how to write function accum:

#Examples:
#accum("abcd") -> "A-Bb-Ccc-Dddd"
#accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
#accum("cwAt") -> "C-Ww-Aaa-Tttt"
#The parameter of accum is a string which includes only letters from a..z and A..Z.

char <- "abcd"

mumbling <- function(char) {
    char <- tolower(char)
    char <- strsplit(char, "")[[1]]
    output <- ""
    for (i in 1:length(char)){
        print(rep(char[i], i-1))
        output <- paste(output, toupper(char[i]), paste(rep(char[i], i-1), collapse=""), "-", sep = "")
    }
    return(substr(output, 1, nchar(output)-1))
}

# converting to sapply (used chatgpt for help)
mumbling2 <- function(s) {
    s <- tolower(s)
    s <- strsplit(s, "")[[1]]
    output <- ""
    output <- sapply(seq_along(s), function(i) {
        subchar <- s[1:i-1]
        rep_char <- rep(s[i], i-1)
        print(rep_char)
        paste(toupper(s[i]), paste0(rep_char, collapse = ""), "-", sep = "")
    })
    output <- paste(output, collapse = "")
    return(substr(output, 1, nchar(output)-1))
}

print(mumbling2(char))

# top codewars solution - comments added by me

accum <- function(s){
  # go straight to the vector of characters
  x <- unlist(strsplit(tolower(s), ""))
  # damn. so strrep can take a vector of strings and their respective vector of repeats to repeat them
  # seq_along(x) - 1 is the vector of repeats for each character:
    # [1] 0 1 2 3
  # strrep(x, seq_along(x) - 1) is the vector of (lower case) strings repeated by the vector of repeats:
    # [1] ""    "b"   "cc"  "ddd"
  # then toupper(x) is the vector of upper case characters:
    # [1] "A" "B" "C" "D"
  # finally, paste0 collapses the vector of upper case characters and the vector of repeated lower case characters with a "-" in between:
    # [1] "A-Bb-Ccc-Dddd"
  paste0(toupper(x), strrep(x, seq_along(x) - 1), collapse = "-")
}