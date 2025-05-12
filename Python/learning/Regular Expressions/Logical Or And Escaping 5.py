# ----------------------------------------------------
# -- Regular Expressions => Logical Or And Escaping --
# ----------------------------------------------------
# |	  Or and it is used to choose between multiple options 
# \	  Escape Special Characters and it is used to escape special characters that have special meaning in regular expressions
# ()  Separate Groups and it is used to separate groups of characters
# -----------------------------

# (\d-|\d\)|\d>) (\w+) means that we have two groups and the first group is (\d-|\d\)|\d>) and the second group is (\w+) 
# the first one is digit number followed by - or ) or > and the second one is any word character for example:
# 1)omarsalem
# 2-omarsalem
# 3)omarsalem

# (\d{3}) (\d{4}) (\d{3}|\(\d{3}\)) here we have three groups and the first one is (\d{3})
#  and the second one is (\d{4}) and the third one is (\d{3}|\(\d{3}\)) the first one is 3 digits and the second one is 4 digits 
# and the third one is 3 digits or (3 digits) for example:
# 1234567890 or 1231231(123)
# ^(https?://)(www\.)?(\w+)\.(net|org|com|info|me)$ here we have four groups and the first one is (https?://)
#  and the second one is (www\.)? and the third one is (\w+) and the fourth one is (net|org|com|info|me) the first one is http or https 
# and the second one is www or nothing and the third one is any word character and the fourth one is net, org, com, info, or me
#for example:
# https://www.google.com
# http://www.google.com
# www.google.com
# google.com
#
