
def quicksort(arr,left,right):
  if left < right:
      #splitting our array
      partition_pos = partition(arr,left,right)
      quicksort(arr,left, partition_pos - 1)
      quicksort(arr,partition_pos+1,right)

def partition(arr,left,right):
    i = left
    j = right -1
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i],arr[j] = arr[j],arr[i]
        if arr[i] > pivot:
            arr[i],arr[right] = arr[right],arr[i]
    return i


def display(list):
    print('Unsorted:')
    print(list)
    quicksort(list,0,len(list)-1)
    print('sorted')
    print(list)

def rando(num):
    import random
    empty = []
    while len(empty) < num:
        number_generator = random.randint(0,100)
        empty.append(number_generator)
    if len(empty) >= num:
        print(display(empty))






#test
Knicks_roster = ['RJ Barrett','Alec Burks','Evan Fournier','Taj Gibson','Quentin Grimes','Rokas Jokubaitis','Kevin Knox II','Miles McBride','Nerlens Noel','Immanuel Quickley','Julius Randle','Mitchell Robinson','Derrick Rose','Aamir Simms','Jericho Sims','Obi Toppin','Luca Vildoza','Kemba Walker','MJ Walker']
#display(Knicks_roster)
rando(13)
