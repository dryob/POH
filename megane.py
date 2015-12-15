
list_legth = []
list_N =[]
list_M =[]

N = int(raw_input())
for x in range(N):
    x = raw_input().split(' ')
    x = map(int, x)
    list_N.append(x)

M = int(raw_input())
for x in range(M):
    x = raw_input().split(' ')
    x = map(int, x)
    list_M.append(x)

for x in range(M,N+1):
    list_legth.append(x)
    
def megane(list_N,list_M):
    correct_counter = 0
    x_counter = 0
    y_counter = 0
    My_counter = 0
    global Ans_listX 
    global Ans_listY
    Ans_listX = []
    Ans_listY = []
    while correct_counter != M:
        while list_N[y_counter][list_legth[x_counter]-M:list_legth[x_counter]] == list_M[My_counter] :
            Ans_listX.append(x_counter)
            Ans_listY.append(y_counter)
            y_counter += 1
            My_counter += 1
            correct_counter +=1
            if correct_counter == M:
                return Ans_listY[0], Ans_listX[0]
                break
        else:
            x_counter += 1
            My_counter = 0
            correct_counter = 0
            Ans_listX = []
            Ans_listY = []
            if correct_counter == M:
                break
            if x_counter > N-M:
                x_counter =0
                y_counter += 1
megane = megane(list_N,list_M)
print megane[0],megane[0]
