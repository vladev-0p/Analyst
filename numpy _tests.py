import numpy as np
'''Basic arrays'''

a = np.array([1,2,3,4])

b= np.array([1.7,2.5,3,4,6,7])

print(a[0],a[1]) # 1 2

print(a[1:4])  #[2 3 4]

print(a[::-1]) #[4 3 2 1]


'''Arrray types '''

print(a.dtype) #int64
print(b.dtype) #float64
c = np.array([1,2,3,4],dtype=float)
print(c.dtype) #float64 appointing data type

'''Matrix '''


Matrix = np.array([
    [1,2,3,7],  #0
    [4,5,6,9],  #1
    [7,8,9,11],  #2
])

print(Matrix.shape) #(3, 3)
print(Matrix.size) #9
print(Matrix.ndim) #2

                   # [4 5]
                    #  [7 8]]


print(Matrix[1:3, [0,1]]) # first 2 rows and 1 , 2 elem in them
print(Matrix[:,-1])

f = np.arange(5) # creating array  with  elements from 0 to 4
f += 20
f+ 20 #This code wont change main f but result will be [20
print(f)