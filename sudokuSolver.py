n = [[3,4,1,0],[0,2,0,0],[0,0,2,0],[0,1,4,3]]
o = [[1,0,3,0],[0,0,2,1],[0,1,0,2],[2,4,0,0]]
m = [[8,0,2,7,0,0,4,0,0],[0,1,0,0,0,9,0,0,5],[0,4,0,0,8,0,2,0,0],[0,0,0,0,5,0,9,2,0],[0,0,0,8,0,7,0,0,6],[7,0,9,0,6,0,0,5,0],[0,0,3,0,0,5,7,0,9],[6,0,0,0,1,0,3,0,0],[4,0,0,2,0,0,0,0,8]]   
n = [[0,7,1,0,9,0,8,0,0],[0,0,0,3,0,6,0,0,0],[4,9,0,0,0,0,7,0,5],[0,1,0,9,0,0,0,0,0],[9,0,2,0,0,0,6,0,3],[0,0,0,0,0,8,0,2,0],[8,0,5,0,0,0,0,7,6],[0,0,0,6,0,7,0,0,0],[0,0,7,0,4,0,3,5,0]]
p = [[5,3,0,0,7,0,0,0,0],[6,0,0,1,9,5,0,0,0],[0,9,8,0,0,0,0,6,0],[8,0,0,0,6,0,0,0,3],[4,0,0,8,0,3,0,0,1],[7,0,0,0,2,0,0,0,6],[0,6,0,0,0,0,2,8,0],[0,0,0,4,1,9,0,0,5],[0,0,0,0,8,0,0,7,9]]
o = [[0,0,0,0,0,8,0,0,0],[3,0,0,0,0,0,8,6,0],[0,0,8,7,0,0,2,0,1],[5,8,0,2,4,1,0,7,6],[1,7,6,8,3,9,5,4,2],[0,4,0,0,7,0,0,0,8],[9,0,4,0,0,2,6,0,0],[0,2,0,0,0,0,0,0,5],[0,0,0,9,0,0,0,2,0]]

def blank(m):
    for i in range(0,9):
        for j in range(0,9):
            if(not m[i][j]):
                return(i,j)

def isBlank(m):
    flag = False
    for i in range(0,9):
        for j in range(0,9):
            if(not m[i][j]):
                flag = True
    return flag
def box(m,i,j):
    flag = True
    for r in range(i-i%3,i-i%3+3):
        for c in range(j-j%3,j-j%3+3):
            if(m[i][j]==m[r][c]):
                flag = False
                break
            if(not flag):
                break
        if(not flag):
            break
    return(flag)
        
def check(m):
    flag = True
    for i in range(0,9):
        for j in range(0,9):
            if(m[i][j]):
                for k in range(0,9):
                    if not(k==j) and not(k==i):
                        if(m[i][k]==m[i][j] or m[k][j]==m[i][j] or (box(m,i,j))):
                            #print(box(m,i,j))
                            flag = False
                            break
                if(not flag):
                    break
        if(not flag):
            break
    return(flag)

def fill(m):
    if(isBlank(m)):
        r,c = blank(m)
        print(r)
        print(c)
        print(m)
        flag  = False
        for k in range(1,10):
            m[r][c] = k
            #print(k)
            #print(m)
            if(check(m)):
                if(fill(m)):
                    return True
            else:
                m[r][c]=0
        if(k==10):
            return False
    else:
        return True
if __name__ == "__main__":
    print(m)
    if(fill(m)):
        print(m)
    else:
        print("No solution exist")    
