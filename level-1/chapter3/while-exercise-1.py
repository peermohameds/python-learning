'''
          _____       
        __|___|_  
     ___|___|___|__
    |____|____|____|

Height of the wall is 3 
total bricks : 6
Your task is to write a program which reads the number of blocks 
the builders have, and outputs the height of the pyramid 
that can be built using these blocks.

Note: the height is measured by the number of fully completed layers.
if the builders don't have a sufficient number of blocks and 
cannot complete the next layer, they finish their work immediately.
Test Data:
Blocks = 6 ; height = 3
Blocks = 20 ; height = 5
Blocks = 1000 ; height = 44
Blocks = 2 ; height = 1

'''
blocks = int(input('Enter no of blocks: '))

total = 0
height = 0

while total <= blocks:
    remaining = blocks - total
    if remaining >= height + 1 :
        height += 1
        total = total + height
    else:
        break

print('Height is :', height)
