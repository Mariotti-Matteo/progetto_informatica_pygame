import pygame

def level1():
    level_move = 16
    level = [
        '##############################',
        '#            r              D#',
        '# 12         r               #',
        '##########LP###              #',
        '#         ??                 #',
        '#                            #',
        '#E                           #',
        '####AA############WW##########',
        '    ??            ??          ',

    ]
    return level, level_move
def level2():
    distance_moving_obj = 10
    level = [
        '?????????????????????????????????????',
        '?                                   ?',
        '?                                   ?',
        '?                                   ?',
        '?                                   ?',
        '? 12                   S           E?',
        '?####   #   #   #S  #    #   #    ##?',
        '?                                   ?'
        '?                                   ?',
        '?     D                             ?',
        '?                                   ?',
        'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',
    ]
    return level, distance_moving_obj
def level3():
    move = 12
    level = [
        "#############################",
        "#                           #",
        "#                           #",
        "# 12                        #",
        "#######I##MMM            ## #",
        "#IIIIIIIIIIIIIIIIIIIIIIII?  #",
        "#?????????????????????????  #",
        "#                           #",
        "#                           #",
        "#      ############A#########",
        "#                ?           #",
        "#            ?              E#",
        "###A############A############",
    ]

    return level, move
def level4():
    move = 15
    level = [
        "##################################",
        "#               #               ##",
        "#               D               ##",
        "#   12          #               ##",
        "#########################       ##",
        "                        #   ?   ##",
        "#########################       ##",
        "#              L                ##",
        "#                               ##",
        "#                               ##",
        "#L   ############W#########LLLL###",
        "#   W############S################",
        "#L   #                           #",
        "#    #              A            #",
        "#    A                           #",
        "#                                #",
        "#                               E#",
        "##?########MMM               #I###",
        "?                                ?",
        "?M                               ?",
        "?                                ?",
        "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
    ]
    return level, move
def level5():
    move = 5
    level = [
        "#############################",
        "#                           #",
        "#                           #",
        "#1                          #",
        "#2  # # S # MMM     # #  #  #",
        "# #                      ?  #",
        "##                       ?  #",
        "#AAAAAAAAAAIAAAAAAAAAAAAA?  #",
        "??????????????????????????  #"
        "#                           #",
        "#                           #",
        "#                           #",
        "#   #####  #########        #",
        "#       ?  ?        #########",
        "#       ?  ?  #  # #        #",
        "####    ?  ?  #  # #        #",
        "#       ?  ?  #### #        #",
        "A   #A##?  ?  #  # #        #",
        "#       ?  ?  #  # #        #",
        "#E      ?  ?                #",
        "##S######  #################"
        "?                           ?",
        "?                           ?",
        "?                           ?",
        "?                           ?",
        "IIIIIIIIIIIIIIIIIIIIIIIIIIIII",
    ]
    return level, move
def level6():
    move = 0
    level = [
        "#############################",
        "#                           #",
        "#                           #",
        "#12   ?##  ######  #####    #",
        "#    ?                      #",
        "########LLLL####WWWWW########",
        "#      ?    ?  ?     ?      #",
        "#      ?    ?  ?     ?      #",
        "########    ####     ########",
        "#                           #",
        "#    #######AAAA#######     #",
        "#                           #",
        "#      ######D ########      #",
        "#     #   I?          #     #",
        "#    #                 #    #",
        "#   #  E   ?            #   #",
        "######### ##???##############",
        "?                           ?",
        "?                           ?",
        "?                           ?",
        "?                           ?",
        "AAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
    ]
    return level, move
def level7():
    move = 10
    level = [
        "?????????????????????????????",
        "?                           ?",
        "?                           ?"
        "?                           ?",
        "?                       12  ?",
        "???#########PPPP??########P??",
        "?           IIII            ?",
        "?                           ?",
        "?                           ?",
        "?                           ?",
        "?    ###DDDDDD########      ?",
        "?            I              ?",
        "?        E                  ?",
        "?        #  mmm             ?",
        "IIIIIIIIIIIIIIIIIIIIIIIIIIIII",
    ]
    return level, move 
def level8():
    move = 1
    level = [
        "#############################",
        "#                     r     #",
        "#                     r     #",
        "#                     r  ?p #",
        "####LLL#######bbbb###########",
        "#  ?   ?    I               #",
        "#  ?P #?    I               #",
        "#  ?????    ?                #",
        "#           ?               #",
        "#E                          #", 
        "###############AAAAAAAAAA####",
    ]
    return level, move
def level9():
    level = [
        "#############################",
        "#                           #",
        "#     #####                 #",
        "#                           #",
        "#                           #",
        "#                           #",
        "#                           #",
        "##########################  #",
        "##########################  #",
        "#                           #",
        "#                           #",
        "#                           #",
        "#                           #",
        "#                           #",
        "#E                          #",
        "#############################",
    ]
    return level
def level10():
    move = 0
    level = [
        "#############################",
        "#                           #",
        "#12                         #",
        "###SS#SS####SS###SS###SSSSSS#",
        "#  II II    II??    ? IIIIII#",
        "#??????????????      ???????#",
        "#                           #",
        "#                    ?      #",
        "#                    ?      #",
        "#SSSS#SS#SS#SS##SAAS######S##",
        "#IIII II II II  I  I?      ?#",
        "#????????????????????       #",
        "#  b          r             #",
        "#  b          r          ?  #",
        "#  b        p r   P      ?  #",
        "#S##########SS#########SS#AS#",
        "# ?##SSSSS##IISSSSSSSSSII # #",
        "#I?##S###D####S#####S###### #",
        "#SSSSSSISSSSSSS#####SSSSSS# #",
        "#S#######################S# #",
        "#EISSSSSSSSSSSSSSSSSSSSSSSS #",
        "#############################",
    ]
    return level, move
def level11():
    level = [
        "#############################",
        "#                           #",
        "#                           #",
        "#                           #",
        "#                           #",
        "#                           #",
        "#                           #",
        "##########################  #",
        "##########################  #",
        "###                         #",
        "#                           #",
        "#                           #",
        "#                           #",
        "#                           #",
        "#E                          #",
        "#############################",
    ]
    return level
def level12():
    level = [
        "#############################",
        "#                           #",
        "#                           #",
        "#                           #",
        "#                           #",
        "#                           #",
        "#                           #",
        "##########################  #",
        "##########################  #",
        "##########################  #",
        "#                           #",
        "#                           #",
        "#                           #",
        "#                           #",
        "#E                          #",
        "#############################",
    ]
    return level
def level12_1():
    level = [
        "#############################",
        "#                           #",
        "#                           #",
        "#                           #",
        "#                           #",
        "#        ####################",
        "#                           #",
        "##########################  #",
        "##########################  #",
        "#                           #",
        "#                           #",
        "#                           #",
        "#                           #",
        "#                           #",
        "#E                          #",
        "#############################",
    ]
    return level