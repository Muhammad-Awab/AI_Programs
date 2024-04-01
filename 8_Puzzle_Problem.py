import queue

my_queue = queue.Queue()

def display(ans):
     
        print(ans[0] , ' ' , ans[1] , ' ' , ans[2])
        print(ans[3] , ' ' , ans[4] , ' ' , ans[5])
        print(ans[6] , ' ' , ans[7] , ' ' , ans[8])
        print('')

initial_state = [1, 2, 3,
                 ' ', 4, 6,
                 7, 5, 8]



def swap(currstate, index1, index2):
    temp = currstate[index1]
    currstate[index1] = currstate[index2]
    currstate[index2] = temp

def producer(currstate, check):
    if check != 1:
        if currstate == [1, 2, 3,
               4, 5, 6,
               ' ', 7, 8]:
            check = 1
            return
        elif currstate[0] == ' ':
            ans1 = currstate.copy()
            swap(ans1, 0, 1)
            my_queue.put(ans1)
            ans1 = currstate.copy()
            swap(ans1, 0, 3)
            my_queue.put(ans1)
        elif currstate[1] == ' ':
            ans1 = currstate.copy()
            swap(ans1, 1, 0)
            my_queue.put(ans1)
            ans1 = currstate.copy()
            swap(ans1, 1, 4)
            my_queue.put(ans1)
            ans1 = currstate.copy()
            swap(ans1, 1, 2)
            my_queue.put(ans1)
        elif currstate[2] == ' ':
            ans1 = currstate.copy()
            swap(ans1, 2, 1)
            my_queue.put(ans1)
            ans1 = currstate.copy()
            swap(ans1, 2, 5)
            my_queue.put(ans1)
        elif currstate[3] == ' ':
            ans1 = currstate.copy()
            swap(ans1, 3, 0)
            my_queue.put(ans1)
            ans1 = currstate.copy()
            swap(ans1, 3, 4)
            my_queue.put(ans1)
            ans1 = currstate.copy()
            swap(ans1, 3, 6)
            my_queue.put(ans1)
        elif currstate[4] == ' ':
            ans1 = currstate.copy()
            swap(ans1, 4, 1)
            my_queue.put(ans1)
            ans1 = currstate.copy()
            swap(ans1, 4, 3)
            my_queue.put(ans1)
            ans1 = currstate.copy()
            swap(ans1, 4, 5)
            my_queue.put(ans1)
            ans1 = currstate.copy()
            swap(ans1, 4, 7)
            my_queue.put(ans1)
        elif currstate[5] == ' ':
            ans1 = currstate.copy()
            swap(ans1, 5, 2)
            my_queue.put(ans1)
            ans1 = currstate.copy()
            swap(ans1, 5, 4)
            my_queue.put(ans1)
            ans1 = currstate.copy()
            swap(ans1, 5, 8)
            my_queue.put(ans1)
        elif currstate[6] == ' ':
            ans1 = currstate.copy()
            swap(ans1, 6, 3)
            my_queue.put(ans1)
            ans1 = currstate.copy()
            swap(ans1, 6, 7)
            my_queue.put(ans1)
        elif currstate[7] == ' ':
            ans1 = currstate.copy()
            swap(ans1, 7, 4)
            my_queue.put(ans1)
            ans1 = currstate.copy()
            swap(ans1, 7, 6)
            my_queue.put(ans1)
            ans1 = currstate.copy()
            swap(ans1, 7, 8)
            my_queue.put(ans1)
        elif currstate[8] == ' ':
            ans1 = currstate.copy()
            swap(ans1, 8, 5)
            my_queue.put(ans1)
            ans1 = currstate.copy()
            swap(ans1, 8, 7)
            my_queue.put(ans1)


my_queue.put(initial_state)

while not my_queue.empty():
    ans = my_queue.get()
    display(ans)
    producer(ans, 0)
    
    

print("Goal state reached!!")