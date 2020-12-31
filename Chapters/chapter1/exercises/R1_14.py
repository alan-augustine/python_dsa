def pair_with_odd_product(data):
    l = len(data)
    for i in range(l-1): # last iteration - i is second-last ement, j is last element
        # distinct pairs
        for j in range(i+1, l):
            #print(i,j)
            # if both numbers are odd, product will be odd
            if data[i]%2!= 0 and data[j]%2!=0:
                print(data[i],data[j])



a = [0,1,2,3,4,5,6,7,8]
pair_with_odd_product(a)
        
