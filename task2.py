
# # import numpy as np

# # def syndrome_decode(codeword, n, k, G):
# #     a = np.transpose(np.concatenate((np.transpose(G[:, k:]), np.identity(n - k)) ,axis=1))
# #     print("Transpose:")
# #     print(a)

# #     S = np.array(np.mod(np.dot(codeword, a),2)),
# #     print("Syndrome:")
# #     print(S[0])
    
     
# #     for row,i in zip(a,range(n)):
# #         if np.array_equal(S[0],row):
# #             codeword[i] ^= 1
# #             return(codeword,'  Detected and Corrected',i)
            
# #     return(codeword,'  No correction',-1)

# # arr = [[1, 0, 0, 0, 1, 1, 1], [0, 1, 0, 0, 1, 1, 0], [0, 0, 1, 0, 1, 0, 1],[0, 0, 0, 1, 0, 1, 1]]
# # n = 7
# # k = 4
# # G = np.array(arr)
# # print("Generator is as follows:")
# # print(G)
# # m = np.array([1, 0, 1, 0])


# # codeword = np.mod(np.dot(m, G), 2)
# # # print('original codeword is as follows:')
# # print(codeword)

# # codeword[1] = [1,0][codeword[1]]
# # print('received codeword is as follows:')
# # print(codeword)

# # decoded  = syndrome_decode(codeword, n, k, G)
# # print('Decoded word: ' , decoded[0],decoded[1])

# # if decoded[2] != -1 :
# #     print('index',decoded[2],'of codeword needed correction')
# # else:
# #     print("")

# # print("The corrected message at reciever's end is ",decoded[0][:k])
# def getGCD(a,b):
#     if b == 0:
#         return a
#     return getGCD(b,a%b)
# n = int(input())
# arr = []
# diff = []
# for _ in range(n):
#     arr.append(int(input()))
#     try:
#         diff.append(abs(arr[-1]-arr[-2]))
#     except:
#         pass
# diff.sort()
# gcd = diff[0]
# for i in range(1,len(diff)):
#     gcd = getGCD(gcd,arr[i])
# print(gcd)
# for i in range(2,gcd+1):
#     if i%gcd == 0:
#         print(i,end = ' ')

# n,k = map(int,input().split())
# mp = {}
# for i in range(k):
#     t = list(map(int,input().split()))
#     for a in t[1:]:
#         mp[a] = i+1
# for i in range(int(input())):
#     x1,x2 = map(int,input().split())
#     print(abs(mp[x1]-mp[x2]))
def fun(mat):
    X = 0 
    O = 0
    for i in range(3):
        if len(set(mat[i])) == 1 and mat[i][0]!='.':
            if mat[i][0] == "X":
                X+=1
            else:
                O+=1
    if X>1 or O>1:
        return "Wait, what?"
    X1 = 0
    O1 = 0
    for i in range(3):
        if len(set([mat[j][i] for j in range(3)])) == 1  and mat[0][i]!='.':
            if mat[0][i] == "X":
                X1+=1
            else:
                O1+=1
    if X1>1 or O1>1:
        return "Wait, what?"
    X+=X1
    O+=O1
    if len(set([mat[0][2],mat[1,1],mat[2,0]])) == 1 and mat[0][2] !=".":
        if mat[0][2] == "X":
            X+=1
        else:
            O+=1
    if len(set([mat[0][0],mat[1,1],mat[2,2]])) == 1 and mat[0][0] !=".":
        if mat[0][0] == "X":
            X+=1
        else:
            O+=1
    if (X>0 and O>0):
        return "Wait, what?"
    if X>0:
        return "X won."
    if O>1:
        return "O won."
    x,o = 0,0
    for i in range(3):
        for j in range(3):
            if mat[i][j] == "X":
                x+=1
            elif mat[i][j] == "O":
                o+=1
    if abs(x-0)>1:
        return "Wait, what?"
    if x+o == 9:
        return "It is a draw."
    if x<o or x == o:
        return  "X's turn."
    else:
        return "O's turn."

mat = []
for i in range(3):
    mat.append(list(input()))
print(fun(mat))

    