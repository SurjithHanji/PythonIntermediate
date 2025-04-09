points=[(1,2),(15,1),(5,-1)]

def sort_by(x):
    return x[1]

points2=sorted(points,key=lambda x:x[0]+x[1])



print(points2)
print(points)