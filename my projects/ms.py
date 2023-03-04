# import random
# l = ["rock", "scissor", "paper"]
# '''
# rock vs paper -> paper wins
# rock vs scissor -> rock wins
# paper vs scissor -> scissor wins
#
# '''
#
# while True:
#     uchoice = int(input('''
# game start.....
# 1 yes
# 2 no | exit
#         '''))
#     if uchoice==1:
#         for a in range(1 , 6):
#             userInput= int(input('''
# 1 rock
# 2 scissor
# 3 paper
#             '''))
#             if userInput == 1:
#              uchoice ="rock"
#             elif userInput == 2:
#                 uchoice = "scissor"
#             elif userInput == 3:
#                 uchoice = "paper"
#             Cchoice=random.choice(l)
#             print(uchoice)
#             print(Cchoice)
#     else:
#         break
#
