'''
Write a program to print all the Armstrong numbers from 0 to N. 
'''

def Arm(N):
    A=str(N)
    D=len(A)
    S=0
    for I in A:
        X=int(I)
        S=S+(X**D)
    if S==N:
        return 1
    return 0

def ListArm(UB):
    i = 0
    I = 1
    while i<UB:
        if Arm(I)==1:
            print(I)
            i = i + 1
        I = I + 1
 
End=int(input("Enter the number of Armstrong numbers you want: "))
ListArm(End)
