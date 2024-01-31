###############################################################################
# Done: 1. (5 pts)
usrnme = input ("Hi, What's your name?") 
print (f"Nice to meet you, {usrnme}")
#   Immediately below this _TODO_, write code that:
#     - Asks the user what their name is
#     - Waits for the user to input their name and hit enter
#     - Greets the user in a friendly manner while using the name that they
#       entered **See the note below**
#
#   Note: You could do this by using concatenation like you used in m1, but
#         we are going to use a different approach called f-strings.
#
#   f-strings allow you to insert information into a string at a pre-determined
#   point in the string. You can use an f-string by placing an 'f' in front of
#   your string and {VARIABLE_NAME} where you want to put your variable. So,
#   for example, let's say I have a variable
#       name = John
#   that I want to insert into a string, I would do so like this:
#       name = John
#       print(f"Hello {name}! It's nice to meet you!")
#
#   Then, when I run my code, it would print:
#       Hello John! It's nice to meet you!
#
#   Now do this with your own friendly greeting, but use the name that the user
#   enters as your variable that you will insert.
#
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

###############################################################################
# DONE: 2. (5 pt)
favnumber = input ("what is your favorite number between 1 and 4?")
print (f"{usrnme}, your favorit number is {favnumber}! how excellent" )

#   Now you might be thinking, why didn't we just use concatenation to do this?
#   Isn't it just the same thing?
#
#   Well, what if we have a number (of type int) that we want to include in a
#   string? If copy the line of code below and paste it under this todo and run
#   your code, what happens when it runs this line (which should be after your
#   code from the first todo runs)?
#
#   print("txt" + 5)
#
#   You should have gotten an error saying that you can only concatentate a str
#   with a str. This is where f-strings come in handy!
#
#   Immediately below this _TODO_, write code that:
#     - Adds another prompt for the user asking for their favorite number
#     - Allows the user to type in their favorite number and hit enter
#
#       Now, actually, if we just took that input as is we could use
#       concatenation because the input that the user gives is already a
#       string. However, to illustrate this example, we are going to convert it
#       to an int (integer).
#
#     - So, after the user gives their input, use the same process we used to
#       convert a float to an int in the Session 2 exercises to convert the
#       input from the user.
#     - Then, have your code respond to the user by using their name from
#       before and the number that they gave to say this:
#
#           <NAME>, your favorite number is <NUMBER>. What a great number!
#
#           so, for example,
#
#           John, your favorite number is 7. What a great number!
#
#   Now, this code has a limitation. The user can type anything when asked
#   for their favorite number. They could type 'red' or they could even
#   type out 'seven', and the code would throw an error because it can't
#   convert that to a number. Feel free to try it! We will learn how to avoid
#   this from happening, but we will cover it later.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
txt = "The quick brown fox jumps over the lazy dog."
Upper = txt.upper()
Lower = txt.lower()
print (Upper)
print (Lower)
###############################################################################
# Done: 1. (1 pt)
#   For the following exercises, you may need to reference the material on 
#   string methods.
#
#   And again, you will reference the string at the top of this file.
#
#   Immediately below this _TODO_, write code that:
#     1. Modifies the string to be in all upper case letters, saves it to a 
#        variable called   upper   and prints its value.
#     2. Modifies the string again to be in all lower case letters, saves it to
#        a variable called   lower   and prints its vale.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

###############################################################################
# done: 2. (1 pt)
txt = "The quick brown fox jumps over the lazy dog."
newcolor = "green" 
newsent = txt.replace ("brown",newcolor)
print (newsent)
#   Immediately below this _TODO_, write code that:
#     - Replaces the word 'brown' with a different color of your choosing.
#     - Saves the result to a variable name
#     - Prints the value of the variable
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

###############################################################################
# done: 3. (2 pts)
num3 = newsent.title()
print (num3)
#   Immediately below this _TODO_, write code that:
#     - Capitalizes the first letter of each word in the string (HINT: look
#       through the methods resource in the pre-class materials that might be
#       helpful)
#     - Saves the result to a variable name
#     - Prints the value of the variable
#
#   Once you have done this, then change the above _TODO_ to DONE.
##########################################################################
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
########################################################################