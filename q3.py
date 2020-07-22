def f1(student):
    #return[ i for i in student if i>0 else ]
    return[i if isinstance(i,int) else 0 for i in student]
print(f1([99,'no data',95,94,'no data']))     