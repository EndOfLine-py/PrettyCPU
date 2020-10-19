#!/usr/bin/python

# https://github.com/Endlassy/PrettyCPU/
# Pls no stealerino

import os
import time
import subprocess
import sys
import argparse

class number:
    one = """
  ██  
  ██  
  ██  
  ██  
  ██  
"""
    two = """
██████
    ██
██████
██    
██████
"""

    three = """
██████
    ██
██████
    ██
██████
"""

    four = """
██  ██
██  ██
██████
    ██
    ██
"""

    five = """
██████
██    
██████
    ██
██████
"""

    six = """
██████
██    
██████
██  ██
██████
"""

    seven = """
██████
    ██
    ██
    ██
    ██
"""

    eight = """
██████
██  ██
██████
██  ██
██████
"""

    nine = """
██████
██  ██
██████
    ██
██████
"""

    zero = """
██████
██  ██
██  ██
██  ██
██████
"""

    dot = """
   
   
   
   
██ 
"""

    celcius = """
   ██████  ██████
   ██  ██  ██    
   ██████  ██    
           ██    
           ██████
"""


class fg: 
    red='\033[31m'
    green='\033[32m'
    orange='\033[33m'
    blue='\033[34m'
    purple='\033[35m'
    cyan='\033[36m'

def translate(num : int):
    if num == 0:
        return ''
    if num == 1:
        return '\033[31m'
    if num == 2:
        return '\033[32m'
    if num == 3:
        return '\033[33m'
    if num == 4:
        return '\033[34m'
    if num == 5:
        return '\033[35m'
    if num == 6:
        return '\033[36m'
    if num == 7:
        return '\033[37m'
    if num > 7 :
        print("--color [1,2,3,4,5,6,7]")
        exit()



global show_celcius
show_celcius = False





def main(color: str, celcius: bool):
    os.system("clear")
    print("\x1b[?25l") # hidden
    os.system("clear")
    while True:
        try:
            proc1 = subprocess.Popen(['sensors'], stdout=subprocess.PIPE)
            proc2 = subprocess.Popen(['grep', 'Tdie'], stdin=proc1.stdout,stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            proc1.stdout.close()
            out, err = proc2.communicate()

            if celcius == True:
                result = out.decode('utf-8').split("+")[1].replace('°','')
            else:
                result = out.decode('utf-8').split("+")[1].replace('°C','')

            # print(result)

            line1 = []
            line2 = []
            line3 = []
            line4 = []
            line5 = []
            line6 = []

            if color != '':
                line1.append(color)
                line2.append(color)
                line3.append(color)
                line4.append(color)
                line5.append(color)
                line6.append(color)

            for chara in result:
                i = 1
                chara = chara.replace("1", number.one).replace("2", number.two).replace("3", number.three).replace("4", number.four).replace("5", number.five).replace("6", number.six).replace("7", number.seven).replace("8", number.eight).replace("9", number.nine).replace("0", number.zero).replace(".", number.dot).replace("C", number.celcius)
                for lines in str(chara).splitlines():
                    if i == 1:
                        line1.append(lines)
                        i += 1
                    elif i == 2:
                        line2.append(lines)
                        i += 1
                    elif i == 3:
                        line3.append(lines)
                        i += 1
                    elif i == 4:
                        line4.append(lines)
                        i += 1
                    elif i == 5:
                        line5.append(lines)
                        i += 1
                    elif i == 6:
                        line6.append(lines)
                        i += 1
                    elif i > 6:
                        break

            line1.append("\033[0m")
            line2.append("\033[0m")
            line3.append("\033[0m")
            line4.append("\033[0m")
            line5.append("\033[0m")
            line6.append("\033[0m")

            print("  ".join(line1))
            print("  ".join(line2))
            print("  ".join(line3))
            print("  ".join(line4))
            print("  ".join(line5))
            print("  ".join(line6))

            time.sleep(1)
            os.system("clear")
        except KeyboardInterrupt:
            print("\x1b[?25h") # shown
            os.system("clear")
            exit()



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Displays your CPU Temp in a 'TTY-Clock' Style")
    parser.add_argument('--celcius', help="Displays '°C' after Temp",action="store_true")
    parser.add_argument('--color', help="Colors [1,2,3,4,5,6,7]" ,type=int, default=0)
    args = parser.parse_args()

    if args.celcius:
        show_celcius = True

    a = translate(num=args.color)

    main(color=a, celcius=show_celcius)
