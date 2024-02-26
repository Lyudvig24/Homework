
def findMinNum(arr):

    minNum = int(arr[0])

    for i in range(len(arr)):
        val = int(arr[i])
        if minNum > val and val > 0:
            minNum = int(arr[i])
        
          
    return minNum

numArr = [
    ['8', '11', '-9', '0', '2', '66', '-20'],
    ['8', '1', '-9', '0', '5', '66', '-20'],
    ['8', '11', '-9', '0', '5', '66', '-20'],
   
]

for i in range(len(numArr)):
    print(findMinNum(numArr[i]))
