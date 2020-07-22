def f1(student):
    return [i for i in student if not isinstance (i,float)] 
print(f1([10,20,20.5,30]))    