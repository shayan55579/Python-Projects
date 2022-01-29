dicArivell = {}
dicCpuBurst = {}


def openFile():
    with open("input.txt") as f:
        file = f.read().splitlines()
        print("Main File is:", file)
        global q
        q = int(file[1])
        global dl
        dl = int(file[0])
        total_p_no = len(file) - 2
        for i in range(2, total_p_no + 2):
            a = file[i].split(':')  # first frayanad
            a1 = a[1].split(',')  # all numbers
            a2 = a1[0]
            dicArivell[a[0]] = int(a2)
            dicCpuBurst[a[0]] = [int(i) for i in a1[1:]]

def addition(n):
    return n - q
openFile()
procese = [v for v in dicArivell.keys()]
print("Processs: ", procese)

print("burst:", [v for v in dicCpuBurst.values()])

dicArivell = {k: int(v) for k, v in dicArivell.items()}  # convert both keys and values to int
list_Arivall = [v for v in dicArivell.values()]
print("List", list_Arivall)
sorted_dic_Arivell = dict(sorted(dicArivell.items(), key=lambda item: item[1]))
print("Sorted Arival:", sorted_dic_Arivell)

print('Cpu burst Time: ', dicCpuBurst)
for i in sorted_dic_Arivell.keys():
    for j in range(0, len(procese)):
        if i == procese[j]:
            #dicCpuBurst[i] = map(addition, dicCpuBurst.values()[j])
            print("Felan Doroste")


print(dicCpuBurst)