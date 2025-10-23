CSI = '\x1b['
RED = '\u001b[31m'
GREEN = '\u001b[32m'
RESET = f'{CSI}0m'

print("  Y")
print("   ↑")
for y in range(18, -1, -2):  
    x = (y - 3) / 2 
    
    if x >= 0:  
        print(f"{y:2d} |" + " " * int(x) + f"{GREEN}/{RESET}")
    else:
        print(f"{y:2d} |")
print("   +" + "-" * 20 + "→ X")
print("    0 2 4 6 8 10")
