
from LinearProbingHash import LinearProbeHashMap
from QuadProbingHash import QuadProbeHashMap
from DoubleHash import DoubleProbeHashMap

def parse_text_file(name):
    temp_data = []
    f = open(name,'r')
    lines = f.readlines()
    data = lines[0:]
    for i in data:
        temp_data.append(i.strip().split())
    temp_data = [inner for outer in temp_data for inner in outer]
    temp_data = [int(e) for e in temp_data]
    f.close()
    print(temp_data)
    return temp_data

def main():
    data = parse_text_file('in150.txt')

    file = open("out150.txt",'w+')
    LinearDict = LinearProbeHashMap(cap =191,p=181)
    QuadDict = QuadProbeHashMap(cap =191,p=181)
    DoubleDict = DoubleProbeHashMap(cap =191,p=181)


    file.write("*** Random Order Start *** \n")
    for i in data:

        linearPreCol = LinearDict._collisions
        LinearDict[i] = i*2
        file.write(f"{i} : {i*2}, collisions: {LinearDict._collisions - linearPreCol} \n")

        QuadPreCol = QuadDict._collisions
        QuadDict[i] = i*2
        file.write(f"{i} : {i*2}, collisions: {QuadDict._collisions - QuadPreCol} \n")

        DoublePreCol = DoubleDict._collisions
        DoubleDict[i] = i*2
        file.write(f"{i} : {i*2}, collisions: {DoubleDict._collisions - DoublePreCol} \n")
        file.write('\n')

    file.write(f'Linear collisions : {LinearDict._collisions}\n')
    file.write(f'Quadratic collisions : {QuadDict._collisions}\n')
    file.write(f' Doulbe collisions : {DoubleDict._collisions}\n')
    file.write("*** Random Order Stop *** \n",)

 
if __name__ == "__main__":
    main() 