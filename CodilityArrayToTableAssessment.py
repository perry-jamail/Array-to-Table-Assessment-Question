import math


def solution(A, K):
    largestNumber = 0
    for i in range(len(A)):
        if A[i] > largestNumber:
            largestNumber = A[i]
            
    border = '+'
    for i in str(largestNumber):
        border += '-'
    endBorder = '+'
    
    def makeBorder(K):
        count = 0
        fullBorder = ''
        while count < K:
            if count == K - 1:
                fullBorder += border
                fullBorder += endBorder
                count += 1
            else:
                fullBorder += border
                count += 1
        return fullBorder
    
    def makeNumberRow(A, K):
        row = '|'
        if K > len(A):
            count = 0
            while count < len(A):
                largestNumberDifference = len(str(largestNumber)) - len(str(A[count]))
                for space in range(largestNumberDifference):
                    row += ' '
                row += str(A[count])
                row += '|'
                count += 1
            while count < K:
                for space in range(len(str(largestNumber))):
                    row += ' '
                row += '|'
                count += 1
        else:
            count = 0
            while count < len(A):
                largestNumberDifference = len(str(largestNumber)) - len(str(A[count]))
                for space in range(largestNumberDifference):
                    row += ' '
                row += str(A[count])
                row += '|'
                count += 1
        return row
    
    def getListSection(A, startIndex, K):
        returnList = []
        kCount = 0
        for i in range(len(A)):
            if i >= startIndex and kCount < K:
                returnList.append(A[i])
                kCount += 1
        return returnList
    
    num = float(len(A)/K)
    numOfBorders = math.ceil(num)
    startIndex = 0
    for i in range(numOfBorders):
        print(makeBorder(K))
        print(makeNumberRow(getListSection(A, startIndex, K), K))
        startIndex += K
    print(makeBorder(K))
        
        
solution([1,45,8,36,812,46,33,9,25,5,3,24567], 5)