
def permute(data, i, length): 
    if (i==length): 
        print(''.join(data) )
    else: 
        for j in range(i,length): 
            #swap
            data[i], data[j] = data[j], data[i] 
            print(data)
            permute(data, i+1, length) 
            print(data)
            data[i], data[j] = data[j], data[i]  