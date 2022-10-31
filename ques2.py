def test_prime(n):
    if(n==1):
        return "Not a prime number"

    elif(n==2):
        return "Prime number"
    
    else:
        for x in range(2,(n/2)+1):
            if(n%x==0):
                return "Not a prime number"
        return "Prime number"

print(test_prime(5))
                