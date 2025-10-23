CSI = '\x1b['
RESET = f'{CSI}0m'
RED = f'{CSI}41m'    
GREEN = f'{CSI}42m'
END = '\u001b[0m'

part1 = f'{GREEN}{" " * 4}{RESET}{''}{" " * 3}{RESET}'
print(part1*3) #чтобы изменить кол-во узоров, нужно просто поменять в скобках число 3
part1 = f'{GREEN}{" " * 1}{RESET}{''}{" " * 2}{RESET}{GREEN}{" " * 1}{RESET}{''}{" " * 3}{RESET}'
print(part1*3)
part1 = f'{GREEN}{" " * 1}{RESET}{''}{" " * 1}{RESET}{GREEN}{" " * 2}{RESET}{''}{" " * 3}{RESET}'
print(part1*3)
part1 = f'{GREEN}{" " * 1}{RESET}{''}{" " * 1}{RESET}{GREEN}{" " * 1}{RESET}{''}{" " * 4}{RESET}'
print(part1*3)
part1 = f'{GREEN}{" " * 1}{RESET}{''}{" " * 1}{RESET}{GREEN}{" " * 5}{RESET}'
print(part1*3)