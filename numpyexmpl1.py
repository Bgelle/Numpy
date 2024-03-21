import numpy as np
print(np.__version__)
arr = np.array([1, 2, 3, 4, 5])
print(arr)
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

arr = np.array([1, 2, 3, 4])

print(arr[0])
arr = np.array([1, 2, 3, 4])

print(arr[1])
arr = np.array([1, 2, 3, 4])

print(arr[2] + arr[3])

arr = np.array([[1,2,3,4,5],
                [6,7,8,9,10]])

print(arr[0])
print(arr[1])
print(arr[0,0],arr[0,1],arr[0,2],arr[0,3],arr[0,4])
print(arr[1,0],arr[1,1],arr[1,2],arr[1,3],arr[1,4])
print(arr[0,0]+arr[1,0])

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(np.sum(arr))
print(np.mean(arr, axis=1))

l1=[1,2,3]
print(l1)


arr = np.array(l1)
print(arr)


