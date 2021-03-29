from math import *
import numpy as np

# Adjacency Matrix

A = np.array([[0,1,0,0,1],[1,0,1,0,1],[0,1,0,0,1],[0,0,0,0,1],[1,1,1,1,0]])
Test_Matrix1 = np.array([[0,1,0,0,1],[1,0,1,0,1],[0,1,0,0,1],[0,0,0,0,1],[1,1,1,1,0]])
Test_Matrix2 = np.array([[0,1.2,0,0,6.5],[1,0,1,0,1],[0,2.1,0,0,1],[0,0,0,0,-1],[1,1,-3.4,1,0]])
Test_Matrix3 = np.array([[1,2,3],[2,4,6],[-1,0,1]])
Test_Matrix4 = np.array([[2,-3,5],[6,0,4],[1,5,-7]])
Test_Matrix5 = np.array([[8,15],[7,-3]])
Test_Matrix6 = np.array([[1,2,1,2,3],[2,3,1,0,1],[2,2,1,0,0],[1,1,1,1,1],[0,-2,0,2,-2]])

def Size_of_Array(arr):
    x = list(arr)
    y = 0
    for element in x:
        y += element**2
    y = sqrt(y)
    return y 

def Size_of_List(List):
    summation = 0
    for element in List:
        summation += element**2
    ans = sqrt(summation)
    return ans

def Error_Calculation(former,latter):
    if former :        
        return float((latter - former)/former)
    else :
        return float((latter - former)/latter)

def Check_Whether_Matrix(A):

    a = A.size
    n= A.shape

    if len(n) == 2:
        n1,n2 = n 
    else : 
        print("This is not a matrix!")
        return False 
    if not a == n1 * n2 :
        print("This is not a matrix!")
        return False
    return True 

def Tupled_All_Element(A):

    if not Check_Whether_Matrix(A):
        return False

    Data = []
    n1,n2 = A.shape
    for i in range(n1):
        for j in range(n2):
            x = (i+1,j+1,A[i][j])
            Data.append(x)
    return Data

def Determinant(A):

    if not Check_Whether_Matrix(A):
        return False

    n,m = A.shape
    if not n == m:
        return False

    # Line Up [1,2,3] , [1,3,2] ... [3,1,2], [3,2,1]
    # put_inside : False = it was already involved, True = it was not found, so I put it inside.
    def put_inside(Line,List,count):
        info = (Line[:], count)
        if List.count(info)==1:
            return False
        elif List.count(info) > 1:
            while not List.count(Line) ==1:
                List.remove(info)
            return False
        else :
            List.append(info)
            return True    

    def switch_order(Line,a,b):
        n1 = Line[a]
        n2 = Line[b]
        Line[a]=n2
        Line[b]=n1
        return Line

    def Levi_Civita(Spare,Line, List):
        
        if len(Line) == 2 :
            put_inside(Line,List,-1)
            switch_order(Line,0,1)
            put_inside(Line,List,1)
            switch_order(Line,0,1)

            if Spare :
                Line.insert(0,Spare.pop(-1))
            else :
                return List
            return Levi_Civita(Spare,Line, List)

        elif not List :
            Spare.append(Line.pop(0))
            return Levi_Civita(Spare,Line, List)

        else:        
            if len(Line) %2:
                start_count = 1
            else:
                start_count= -1

            new_List = []
            for info in List:
                order,count = info
                add_count = start_count 
                for i in range(len(order)+1):
                    order_copy = order[:]
                    order_copy.insert(i,Line[0])
                    count_copy = add_count * count
                    info_copy = order_copy,count_copy
                    new_List.append(info_copy)
                    add_count = -add_count
                    
            if Spare :
                Line.insert(0,Spare.pop(-1))
            else :
                return new_List
            return Levi_Civita(Spare,Line, new_List)
                    
    Line = []
    Spare = []
    List = []
    for i in range(n):
        Line.append(i)
    Line.sort(reverse=True)
    List = Levi_Civita(Spare,Line, List)

    det = float(0)
    for info in List:
        order, count = info
        cal = float(1) 
        for i in order:
            cal *=  float(A[order.index(i)][i])
        det += cal*count
                
    return det 
        
def DOC(A):

    # AX = Y
    # Check the dimensions
    if not Check_Whether_Matrix(A):
        return False

    # X is a vector having all elements as 1 
    n1,n2 = A.shape
    X = np.ones((n2,1), dtype = int)
    Y = A@X
    return Y

def EC_manual(A,λ):

    # λC = AC
    # Check the dimensions
    if not Check_Whether_Matrix(A):
        return False

    n,m = A.shape
    if not n == m:
        return False

    B = A - np.eye(n)*λ
    det = Determinant(B)

    return det 

def EC_Auto_Value(A):

    # λC = AC
    # Check the dimensions
    if not Check_Whether_Matrix(A):
        return False

    n,m = A.shape
    if not n == m:
        return False

    # switch 0 : Until 2nd Strategy 
    # switch 1 : 3rd Strategy
    # switch 2 : 4th Strategy
    # switch 3 : 5th Strategy 
    switch = 0 

    PP_List = []
    dif_PP_List = []
    Ans_List = []
    Memory = 0
    # First strategy : lowering the size of matrix
    det = Determinant(A)
    k = abs(det)**(1/n)
    if not k:
        B_List = DOC(A)[0]
        for num in B_List:
            k += num
    A = A/k
    
    def check_sign_change(List):
        New_List = []
        check = []
        count = 0
        for value,solution in List:
            if value >0:
                sign = True
            elif value <0:
                sign = False
            else:
                sign = None
            check.append(sign)
            if len(check)>1 and check[-1] != check[-2]:
                count += 1
                New_List.append((value,solution))
                New_List.append(List[List.index((value,solution))-1])
        return New_List, count 

    #Second strategy : Plotting all points and guess the range of the solutions
    for i in range(21):
        λ =  i-10
        Data1 = (EC_manual(A,λ), λ)
        PP_List.append(Data1)
        if Memory:
            Data2 = (EC_manual(A,λ)-Memory,λ)
            dif_PP_List.append(Data2)
        Memory = EC_manual(A,λ)
    
    Dif_List, dif_change_count =  check_sign_change(dif_PP_List)
    PP_List, sign_change_count = check_sign_change(PP_List)
    if dif_change_count < n-1 :
        switch = 1

    def Timid_Grid(PP_List,A):
        New_PP_List = []
        while PP_List :
            New_case = []
            Mini_PP_List = []
            sign_change_count = 0 
            det_1, λ_1 = PP_List.pop(0)
            det_2, λ_2 = PP_List.pop(0)
            interval = float(λ_2-λ_1)
            for i in range(11):
                new_λ = float(interval*i/10 + λ_1)
                new_det = EC_manual(A,new_λ)
                New_case.append((new_det,new_λ))
            Mini_PP_List,sign_change_count = check_sign_change(New_case)
            New_PP_List += Mini_PP_List
        return New_PP_List

    satisfaction = 1
    Memory2 = 0
    Memory3 = 0
    while abs(satisfaction) > 0.00001:
        satisfaction = 0 
        PP_List = Timid_Grid(PP_List,A)
        for i in range(len(PP_List)):
            if not i %2 :
               Memory2 = PP_List[i][1]     
            else:
                satisfaction += Error_Calculation(Memory2,PP_List[i][1])
        satisfaction = float(satisfaction / (len(PP_List)/2))

    Ans_List = []
    for i in range(len(PP_List)):
        if i%2:
            adjusted_λ =  k* PP_List[i][1]
            Ans_List.append(adjusted_λ)
            
    return Ans_List 

def Convertable(A):

    # Only fucntion operates to convert det = 0 into the else.

    def All_the_Same(List):
        if List.count(List[0]) == len(List):
            return True
        else:
            return False

    #How to deal with repeated equation 
    B = []
    C = []
    done = True 
    while done:
        n,m = A.shape
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                else : 
                    prop = (A[j]/Size_of_Array(A[j])-A[i]/Size_of_Array(A[i]))
                    if All_the_Same(list(prop)):
                        A = np.delete(A,j,0)
                        B.append(j)
                        for k in range(n-1):
                            value = -A[k][j]
                            C.append(value)
                        A = np.delete(A,j,1)
                        break
            break
        done = False
    if C:
        D = list(np.linalg.inv(A)@np.array(C))
        while B:
            D.insert(B.pop(),1)
        D = list(np.array(D)/Size_of_List(D))

    #Without repeated equation, it could be  at the determinant zero.
    else :
        while not C :
            n,m = A.shape
            A = np.delete(A,0,0)
            B.append(0)
            for i in range(n-1):
                value = -A[i][0]
                C.append(value)
            A = np.delete(A,0,1)
        D = list(np.linalg.inv(A)@np.array(C))
        while B:
            D.insert(B.pop(),1)
        D = list(np.array(D)/Size_of_List(D))
        
    return D

def EC_Auto_Vector(A):

    if not Check_Whether_Matrix(A):
        return False

    Eigenvalue_List = EC_Auto_Value(A)
    n,m = A.shape

    C_E_List = []
    for λ in Eigenvalue_List:
        B = A - λ*np.eye(n)
        C_E_List.append(Convertable(B))
        
    return C_E_List

def PC_Auto_Vector(A,α,β):

    if not Check_Whether_Matrix(A):
        return False
    
    # C_p  = np.inv(α*A@inv(D)-np.eye(n))@(-β*np.one(n))
 
    D = DOC(A)
    n,m = A.shape
    D = np.eye(n)*D

    C = np.linalg.inv(α*A@np.linalg.inv(D)-np.eye(n))@(-β*np.ones(n))

    return C 

def Push_Layer(i,j,k):
    # k is deleted layer number of nxn matrix
    # i,j is a coordinate of remnant, (n-1)x(n-1) matrix
    
    if i >= k:
        i = i+1
    if j >= k:
        j = j+1

    # All coordinates correspond into the nxn matrix again
    return (i,j)

def Shortest_Path_Exemption(Map,Exemption_List):
    M = Map
    Ex_List = Exemption_List # As a list of locations number
    Ex_List.sort()

    # Renew the original Matrix by slicing the selected rows and columns
    discount = 0
    for target in Ex_List:
        target -= discount
        M = np.delete(np.delete(M,target,0),target,1)
        discount += 1

    # Stacking 
    Memory = []
    n,m = M.shape
    Base = np.ones((n,n))
    A = np.eye(n)
    for i in range(n):
        A = A@M
        Memory.append(A)

    check = 0 
    # Put the checked shortest path number in the base 
    for i in range(n):
        for j in range(n):
            for k in range(n):
                check = Memory[k][i][j]
                if check :
                    Base[i][j] += k
                    break
                
    return Base, Memory 

#print(Shortest_Path_Exemption(A,[0]))

def Shortest_Path(Map):
    
    M = Map
    # Stacking 
    Memory = []
    n,m = M.shape
    # For example, M^(k+1) is saved in the Memory[k]. Each number of steps to get arrivals should be k+1. 
    Base = np.ones((n,n))   
    A = np.eye(n)
    # No unit matrix gets involved in the Memory list. 
    for i in range(n):
        A = A@M
        Memory.append(A)    

    check = 0 
    # Put the checked shortest path number in the base 
    for i in range(n):
        for j in range(n):
            for k in range(n):
                check = Memory[k][i][j]
                if check :
                    Base[i][j] += k
                    break
                
    return Base, Memory

def BC_Auto(A):
    
    n,m = A.shape
    C_b = []

    for k in range(n):
        A1 = np.delete(np.delete(Shortest_Path(A)[0],k,0),k,1)
        A2 = np.zeros((n-1,n-1))
        Record1 = Shortest_Path(A)[1]
        Record2 = Shortest_Path_Exemption(A,[k])[1]
        for i in range(n-1):
            for j in range(n-1):
                bookmark = A1[i][j]
                (i2,j2) = Push_Layer(i,j,k)
                check1 = Record1[int(bookmark-1)][i2][j2]
                check2 = Record2[int(bookmark-1)][i][j]
                if check1:
                    A2[i][j] = (check1 - check2)/check1
                else :
                    A2[i][j] = 0
                if i == j:
                    A2[i][j] = 0
        total = np.sum(A2)
        C_b.append(total)        

    total_value = 0
    for i in range(n):
        C_b[i] /= Size_of_List(C_b)

    #A2 becomes a matrix of probabilty to pass 

    return C_b
    
def CC_Auto(A):

    C_c = []
    Short_Path_Matrix = Shortest_Path(A)[0]
    n,m = A.shape

    for i in range(n):
        vector = np.zeros(n)
        vector[i] = 1 
        new_vector = np.delete(Short_Path_Matrix@vector,i,0)
        C_c.append((n-1)/np.sum(new_vector))
  
    return C_c

def CH_Auto(A):

    C_h = []
    Short_Path_Matrix = Shortest_Path(A)[0]
    n,m = A.shape    
    for i in range(n):
        vector = np.zeros(n)
        vector[i] = 1
        new_vector = Short_Path_Matrix@vector
        new_vector[i] = 0 
        new_vector = np.ones(n) / new_vector
        for  j in range(n):
            if new_vector[j] == inf:
                new_vector[j] = 0 
        C_h.append(np.sum(new_vector)/(n-1))
    return C_h

print(CH_Auto(A))



    

    



