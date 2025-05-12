# -----------------------------------------------------------------------
# -- Regular Expressions => Characters Classes Training's --
# -----------------------------------------------------------------------
# [0-9] # this regular expression matches any digit
# [^0-9] # this regular expression matches any character that is not a digit
# [A-Z] # this regular expression matches any uppercase letter
# [^A-Z] # this regular expression matches any character that is not an uppercase letter
# [a-z] # this regular expression matches any lowercase letter
# [^a-z] # this regular expression matches any character that is not a lowercase letter
# [A-Za-z] # this regular expression matches any letter
# [A-Za-z0-9] # this regular expression matches any letter or digit
# -------------
# \s[A-Z]{2}\s[0-9]{3}\s\w{,6} # this regular expression matches a string that starts with a whitespace character followed by
#  two uppercase letters followed by three digits followed by whitespace character and ends with six word characters at most
# example : " AB 123 hello"

