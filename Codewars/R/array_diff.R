"""
Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b keeping their order.

array_diff(c(1, 2), 1) == 2
If a value is present in b, all of its occurrences must be removed from the other:

array_diff(c(1, 2, 2, 2, 3), 2) == c(1, 3)
"""

array_diff <- function(a, b) {
  a[!a %in% b]
  #setdiff(a, b) I think this doesn't work because it returns elements only once, which won't work in the case of duplicates
}

print(array_diff(c(1, 2, 2, 2, 3), c(2, 3)))

""" this is also the top codewars solution"""