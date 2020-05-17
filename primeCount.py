def count_primes(num):
    count = 0
    for i in range(3,num+1) :
        prime_flag = 1
        for j in range(2,i) :
            if(i%j == 0) :
                prime_flag = 0
                break
        count += prime_flag
    return count

print(count_primes(100))