def print_sorceror():
    s = [
        " ***** ", 
        "* *    ", 
        " ***** ", 
        "      *", 
        " ***** "
    ]
    
    o = [
        " ***** ", 
        "*     * ", 
        "*     * ", 
        "*     * ", 
        " ***** "
    ]
    
    r = [
        "*****  ", 
        "*   * ", 
        "*****  ", 
        "*   * ", 
        "*   * "
    ]
    
    c = [
        " ***** ", 
        "*      ", 
        "*      ", 
        "*      ", 
        " ***** "
    ]
    
    e = [
        " ***** ", 
        "*      ", 
        "*****  ", 
        "*      ", 
        " ***** "
    ]
    
    space = "  "  # Space between letters

    for i in range(5):
        print(s[i] + space + o[i] + space + r[i] + space + c[i] + space + e[i] + space + r[i] + space + o[i] + space + r[i])

# Call the function to print "SORCEROR" in one line
print_sorceror()

