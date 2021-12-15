
def bowls_recursive(n):
    if n == 1:
        return 1
    else:
        return bowls_recursive(n-1) + n

def bowls_loop(n):
    sum = 0
    for i in range(n + 1):
        sum = sum + i
    return sum

def bowls_sequence(n):
    #sum = n/2 * (2 + (n-1)*1)
    sum = n * (n+1)/2
    return int(sum)


print("Enter the rows  : ")  # Requesting user input
limit = input()
bowl = 0
print('Bowls: {}'.format(bowls_loop(int(limit))))
#print('Bowls: {}'.format(bowls_sequence(int(limit))))
#print('Bowls: {}'.format(bowls_recursive(int(limit))))