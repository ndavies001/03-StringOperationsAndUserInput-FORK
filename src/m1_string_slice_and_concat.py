txt = "  The quick brown fox jumps over the lazy dog.  "
txt = txt.strip()
print ("txt after removing spaces:", txt)
###############################################################################
# DONE 1. (1 pt)
#   Notice the string   txt   that I have defined above. First, let's clear up
#   those extra spaces.
#
#   Immediately below this _TODO_, write code that:
#       Reassigns the value of the variable   txt   to a version of the same
#       string but with the spaces at the beginning and at the end removed.
#       Use a method to do this for you and don't simply copy and paste the
#       string but without the spaces.
#       (HINT: the method that you need was in your pre-class materials)
#   
#   We will be using the updated string (which should still be called   txt   )
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

###############################################################################
# DONE: 2. (1 pt)

#   From now on, do not reassign the variable   txt   . You will be using it as
#   your starter string for the rest of these exercises.
#
#   Immediately below this _TODO_, write code that:
#     - Gets the word 'quick' from the starter string (do NOT just type the
#        word 'quick')
#     - Assigns that value to a variable of your choosing (not txt)
#     - Prints the value of that variable
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
words = txt.split()
word_quick = words[1]
print (word_quick)
###############################################################################
# DONE: 3. (1 pt)
#   Let's add another sentence to our string.
sentence2 = "but the lazy dog is quicker than the fox"
print (txt + sentence2)
#   Immediately below this _TODO_, write code that:
#     - Assigns another sentence to a variable name (you choose the name and 
#       sentence)
#     - Combines the starter string with your new sentence. Remember to include
#       a space between your sentences (so you have three things to put
#       together: the starter string, a space, and your new sentence).
#     - Prints the result
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################