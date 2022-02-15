from xml.dom.minidom import Element


def binary_search(start,end,int_list,target):
    if start<=end:
        mid = (start+end) // 2

        if int_list[mid] == target:
            return mid +1
        elif target < int_list[mid]:
            return binary_search(start,mid-1,int_list,target)
        elif target > int_list[mid]:
            return binary_search(mid+1,end,int_list,target)

    else:
        return -1

length = int(input("Insira o tamanho da lista: "))
int_list = []

for i in range(length):
    element = int(input("Insira o elemento: "))
    int_list.append(element)

int_list=sorted(int_list)
print(int_list)

target = int(input("Insira o elemento alvo: "))
position = binary_search(0,length-1,int_list,target)
if position == -1:
    print('Elemento não está na lista')
else:
    print("Elemento está na posição: "+ str(position))


length = int(input("Insira o tamanho da lista: "))
int_list = []

for i in range(length):
    element = int(input("Insira o elemento: "))
    int_list.append(element)
    
    int_list=sorted(int_list)
    print(int_list)

    target = int(input("Insira o elemento alvo: "))

start = 0 
end = length-1
position = -1

while(start<=end):
    mid = (start+end) // 2
    if int_list[mid] == target:
        position = mid
        break

    elif target < int_list[mid]:
        end = mid-1
    
    elif target > int_list[mid]:
        start = mid+1
    if position == -1:
        print('Elemento não está na lista')
    else:
        print("Elemento está na posição: "+ str(position+1))
