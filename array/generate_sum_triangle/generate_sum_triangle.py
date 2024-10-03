def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """

    res = [[1]]
    for i in range(numRows - 1):
        temp = [0] + res[-1] + [0]
        p1 = 0
        p2 = 1
        temp2 = []
        while p2 < len(temp):
            temp2.append(temp[p1] + temp[p2])
            p1 += 1
            p2 += 1
        res.append(temp2)
    print(res)
    return res
# numRows = 5
# generate(numRows)

def getRow(rowIndex):
    if rowIndex < 0 or rowIndex > 33:
        return None
    res = [1]
    for i in range(0, rowIndex):
        temp = [0] + res + [0]
        res = []
        p1 = 0
        p2 = 1
        while p2 < len(temp):
            res.append(temp[p1] + temp[p2])
            p1 += 1
            p2 += 1
    return res

getRow(3)