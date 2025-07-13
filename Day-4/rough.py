def sum_of_n(sum,i,n):
    if i > n:
        print(sum)
        return(sum)
    sum_of_n(sum+i,i+1,n)

sum_of_n(0,1,10)