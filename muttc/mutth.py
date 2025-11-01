# TODO: add comments over this file
# documenting function would be good too

# weird name but does what it says

# FIXME: some of these functions may use negative indexes

def is_notspace(string):
    return (string.isalpha() or string in ["_","[","]","*","\"","@"] or string.isdigit()) and not string.isspace() # isspace might be redundant

def get_next_word(src,cursor):
    cursor_p = cursor
    word = ""
    src_sz = len(src)
    word_s = cursor
    word_f = cursor
    while(cursor_p<src_sz and not is_notspace(src[cursor_p])):
        cursor_p +=1
    word_s = cursor_p
    while(cursor_p<src_sz and is_notspace(src[cursor_p])):
        word += src[cursor_p]
        cursor_p +=1
    word_f = cursor_p
    return (word_s,word_f,word)

def get_previous_word(src,cursor):
    cursor_p = cursor
    word = ""
    word_s = cursor
    word_f = cursor
    while(cursor_p>0 and not is_notspace(src[cursor_p])):
        cursor_p -=1
    word_s = cursor_p
    while(cursor_p>0 and is_notspace(src[cursor_p])):
        word = src[cursor_p]+word
        cursor_p -=1
    word_f = cursor_p
    # swapped because we start at the end
    return (word_f,word_s,word)

def insert_at(string, thing, place):
    return string[:place] + thing + string[place:]

def set_at(string, thing, place):
    new_str = list(string) 
    new_str[place] = thing
    return "".join(new_str)

def chop_at(string, start, end):
    return string[:start] + string[start+abs(end-start):]

def get_statement(src,cursor):
    p_cursor = cursor
    in_str = False
    no_colon = True
    while(p_cursor<len(src)): 
        chara = src[p_cursor] 
        if chara == "\"" and not src[cursor-1] == "\\":
            in_str = not in_str
            str_start = p_cursor
        elif chara == ":" and not in_str:
            no_colon = False
            break
        p_cursor+=1
    if no_colon or in_str:
        #TODO: add error and stop compiler
        print("if statement unfinished")
    return p_cursor

def block_line(src,cursor):
    p_cursor = cursor
    while(p_cursor<len(src)): 
        char = src[p_cursor]
        if(char == "\n"):
            return True
        elif(is_notspace(char)):
            return False
        p_cursor += 1
    # TODO: handle error
    print("expected line after statement or function")
    return False

def get_var_declaration_end(src,cursor):
    p_cursor = cursor
    while(p_cursor<len(src)): 
        char = src[p_cursor]
        if(char in ["\n", "="]):
            return p_cursor
        p_cursor += 1
    return p_cursor

def is_var_defined(src,cursor):
    p_cursor = cursor
    while(p_cursor<len(src)): 
        char = src[p_cursor]
        if char == "\n":
            return False
        elif char == "=":
            return True
        p_cursor += 1
    return True

def get_line_end(src,cursor):
    p_cursor = cursor
    while(p_cursor<len(src)): 
        char = src[p_cursor]
        if(char == "\n"):
            return p_cursor
        p_cursor += 1
    return p_cursor

def get_var_definition(src,cursor):
    if not is_var_defined(src,cursor):
        return (cursor,get_line_end(src,cursor),"")
    p_cursor = cursor
    p_layers = [0,0,0]
    p_opens = ["[","{","("]
    p_close = ["]","}",")"]
    in_string = False
    found_def = False
    # find the =
    while(p_cursor<len(src)): 
        char = src[p_cursor]
        if(char == "="):
            found_def = True
            break
        p_cursor += 1
    #TODO: error
    if not found_def:
        print("something is weird about your definition")
        return
    d_start = p_cursor
    # now get the insides
    insides = ""
    while(p_cursor<len(src)): 
        char = src[p_cursor]
        insides += char
        if(char == "\"" and not src[p_cursor-1] == "\\"):
            in_string = not in_string
        elif(char in p_opens):
            p_layers[p_opens.index(char)] += 1
        elif(char in p_close):
            p_layers[p_close.index(char)] -= 1
        elif(char == "\n" and (p_layers[0]+p_layers[1]+p_layers[2])==0 and not in_string):
            return (d_start,p_cursor,insides)
        p_cursor += 1
    # TODO: yeah do something with this error
    print("variable defined wrong")
    raise Exception("something went wrong again")

def get_semicolon(src,cursor):
    p_cursor = cursor
    p_layers = [0,0,0]
    p_opens = ["[","{","("]
    p_close = ["]","}",")"]
    in_string = False
    d_start = p_cursor
    # now get the insides
    insides = ""
    while(p_cursor<len(src)): 
        char = src[p_cursor]
        if(char == "\"" and not src[p_cursor-1] == "\\"):
            in_string = not in_string
        elif(char in p_opens):
            p_layers[p_opens.index(char)] += 1
        elif(char in p_close):
            p_layers[p_close.index(char)] -= 1
        elif(char == "\n" and (p_layers[0]+p_layers[1]+p_layers[2])==0 and not in_string):
            return p_cursor
        p_cursor += 1
    # TODO: yeah do something with this error
    print("variable defined wrong")
    raise Exception("something went wrong again")

def get_function_arguments_contents(m_src, cursor):
    # TODO: make this section get_p_contents
    p_cursor = cursor
    no_opening = True
    no_closing = True
    inner_str = ""
    p_start = cursor
    p_end = cursor
    while(p_cursor<len(m_src)):
            if(m_src[p_cursor] == "("):
                no_opening = False
                p_start = p_cursor
                p_cursor += 1
                break
            p_cursor += 1
    if no_opening:
            #TODO: handle this error properly
            print("their's something wrong with your func")
            #return
    while(p_cursor<len(m_src)):
            if(m_src[p_cursor] == ")"):
                no_closing = False
                p_end = p_cursor
                p_cursor += 1
                break
            inner_str += m_src[p_cursor]
            p_cursor += 1
    if no_closing:
            #TODO: also handle this error properly
            print("their's something else wrong with your func")
            #return
    return (p_start,p_end,inner_str)

def get_c_args(inner_str):
    m_args = inner_str.split(",")
    c_args = []
    for arg in m_args:
            if len(arg) == 0:
                # their is no args, so we'll just break the for loop.
                break
            if "[" in arg:
                # TODO: do something with this error (again)
                print("arrays cannot be arguments (try a pointer)")
                #return
            arg = arg.split(":")
            if not len(arg) == 2:
                # TODO: handle this
                print("invalid number of types")
                #return
            c_args.append(f"{arg[1]} {arg[0]}")
    c_args = str(c_args).replace("[","").replace("]","").replace("'","")
    return c_args

def get_function_end(m_src,cursor):
    p_cursor = cursor
    no_ending = True
    while(p_cursor<len(m_src)):
            if(m_src[p_cursor] == ":"):
                no_ending = False
                p_cursor += 1
                break
            p_cursor += 1
    if no_ending:
        # TODO: you know the drill
        print("function never ended are you missing an \":\"")
        #return
    return p_cursor

def get_indent_count(src,cursor):
    # FIXME: this currently ignores tabs inside strings
    p_cursor = cursor
    tab_count = 0
    while(p_cursor<len(src)): 
        char = src[p_cursor]
        if(char == "\n"):
            return tab_count
        elif(char == "\t"):
            tab_count += 1
        p_cursor -= 1
    return tab_count

def check_indents_add_brackets(src,cursor,indents):
    new_indents = get_indent_count(src,cursor)
    indent_delta = 0-(new_indents-indents)
    indent_delta = max(indent_delta,0)
    new_source = insert_at(src,"\n}\n"*indent_delta,cursor)
    cursor_delta = len(new_source)-len(src)
    return (new_source,cursor+cursor_delta,new_indents,cursor_delta)