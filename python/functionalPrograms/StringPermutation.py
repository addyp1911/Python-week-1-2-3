
def permute(data, i, length): 
    if i==length: 
        print(''.join(data) )
    else: 
        for j in range(i,length): 
            #swap
            data[i], data[j] = data[j], data[i] 
            print(data)
            permute(data, i+1, length) 
            data[i], data[j] = data[j], data[i]  


string = input("enter the string you want to permute= ")
n = len(string) 
data = list(string) 
permute(data, 0, n)