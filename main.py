
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
    LinearDict = LinearProbeHashMap()
    QuadDict = QuadProbeHashMap()
    DoubleDict = DoubleProbeHashMap()
    #DoubleDict[4] = 'hello'
    #DoubleDict[195] = 'there'

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

    for i in LinearDict._table:
        try:
            print("key: ",i._key,"Value: ",i._value)
        except AttributeError:
            print('None')


    data.sort()
    LinearDictAsc = LinearProbeHashMap()
    QuadDictAsc = QuadProbeHashMap()
    DoubleDictAsc = DoubleProbeHashMap()

    #file.write("*** Ascending Order Start *** \n")
    #for i in data:
#
    #    linearPreCol = LinearDictAsc._collisions
    #    LinearDictAsc[i] = i*2
    #    file.write(f"{i} : {i*2}, collisions: {LinearDictAsc._collisions - linearPreCol} \n")
#
    #    QuadPreCol = QuadDictAsc._collisions
    #    QuadDictAsc[i] = i*2
    #    file.write(f"{i} : {i*2}, collisions: {QuadDictAsc._collisions - QuadPreCol} \n")
#
    #    DoublePreCol = DoubleDictAsc._collisions
    #    DoubleDictAsc[i] = i*2
    #    file.write(f"{i} : {i*2}, collisions: {DoubleDictAsc._collisions - DoublePreCol} \n")
    #    file.write('\n')
#
    #file.write(f'Linear collisions : {LinearDictAsc._collisions}\n')
    #file.write(f'Quadratic collisions : {QuadDictAsc._collisions}\n')
    #file.write(f' Doulbe collisions : {DoubleDictAsc._collisions}\n')
    #file.write("*** Ascending Order Stop *** \n",)


    #for i in range(191):
    #    DoubleDict[i] = i*2


    #print('collisions : ',QuadDict._collisions)
    #print('collisions : ',LinearDict._collisions)
    #print('collisions : ',DoubleDict._collisions)
if __name__ == "__main__":
    main() 