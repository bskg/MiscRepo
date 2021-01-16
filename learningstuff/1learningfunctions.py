# apparently this is a comment?
def function1 ():
    print("yes this is a function")
    print("remember it could be named something else")
print("this is outside the function")
#this saves something for later. Later looks like this:
#"function1 ()"
#okay it worked
# I should number all my comments this is super messy.
# if I get jupyter (do I have it?) then I can do multiple boxes in one window
renamed = function1
#can I rename the function? the way variables are renamed?? I'll find out.
#testing, get "this is outside the function"
renamed 
#seems to do nothing, parentheses are important for this
renamed ()
#that worked
#last question for this. what happens now if I do a "function1 ()"? 
#temporarily removed "renamed ()"
function1 ()
# it worked too, it's sharing it but not overwritten
#oh, what if I change function1 now? Like, a new def?? will renamed do the old thing?
def function1 ():
    print("f1 does this now")
print("this is another thing to print")
function1 ()
#what about renamed now?
renamed ()
#hahahah nice okay I'll go learn other stuff

