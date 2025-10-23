CSI = '\x1b['
RESET = f'{CSI}0m'
RED = f'{CSI}41m'    
GREEN = f'{CSI}42m'  
HEIGHT = 6

for i in range(1,HEIGHT):
    if i == 2 or  i == 4:
        left_green = f'{GREEN}{" " * 6}{RESET}'
        center = f'{RED}{" " * 5}{RESET}'
        right_green = f'{GREEN}{" " * 9}{RESET}'
        line = left_green + center + right_green
        print(line)
    elif i == 3:
        left_green = f'{GREEN}{" " * 5}{RESET}'
        center = f'{RED}{" " * 7}{RESET}'
        right_green = f'{GREEN}{" " * 8}{RESET}'
        line = left_green + center + right_green
        print(line)

    elif i == 1 or i == 5:
        line = f'{GREEN}{" " * 8}{RESET}{RED}{" " * 1}{RESET}{GREEN}{" " * 11}{RESET}'
        print(line)




    