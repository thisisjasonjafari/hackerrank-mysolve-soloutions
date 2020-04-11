import textwrap

def wrap(string, max_width):
    msg = ""
    for i in range(len(string)):
        if (i+1)%(max_width ) == 0 and i != 0 :
            msg = msg +string[i]+ "\n"
        else :
            msg = msg + string[i]
    


    return msg
