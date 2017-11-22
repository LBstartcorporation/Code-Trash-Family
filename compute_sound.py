## compute_sound.py

import sys, json  #, numpy as np

#Read data from stdin
def read_in():
    lines = sys.stdin.readlines()
    #Since our input would only be having one line, parse our JSON data from that
    return json.loads(lines[0])

def main():
    #get our data as an array from read_in()
    lines = str(read_in()).split('[')[1].split(']')[0] + ', '

    file = open('testfile3.txt','a') 
    file.write(str(lines)) 

    print list(lines) #lines_sum

#start process
if __name__ == '__main__':
    main()