MatrizAdya = [
                [1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1],
            ]
Certificado=[0,1,2,3,4,5,6,7,8,9,0]
def subM(
    matrix, 
    rowStartIdx, rowEndIdx,
    colStartIdx, colEndIdx):

    result = [
        x[ colStartIdx : colEndIdx ]
        for x in matrix[ rowStartIdx : rowEndIdx ]
    ]

    return result



subA = subM(MatrizAdya,
                    0, 1, 
                    0, 1)


subA