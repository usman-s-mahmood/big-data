
def isPrime(num):
    flag = True
    for i in range(1, int(num)):
        if (i % num == 0):
            print(i)
            flag = False # faulty algorithm, try again with better approach
    if flag:
        print(f'Number: {num} is prime')
    else:
        print(f'Number: {num} is not prime')
        
def main():
    num = int(input("Enter an integer for prime number check: "))
    isPrime(num)
    
if __name__ == '__main__':
    main()