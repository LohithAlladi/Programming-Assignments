# You can add any additional function and class you want to implement in this file
def comp1(a,b):
    return a<b
    
def comp2(a,b):
    A= a.remaining_size + a.arrival_time
    B= b.remaining_size + b.arrival_time
    if A==B:
        return a.id<b.id
    return A<B
    
def comp3(a,b):
    return a.load<b.load
    
    