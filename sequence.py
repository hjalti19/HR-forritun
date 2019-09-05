#finnur næsta gildi í eftirfarandi runu: n +1 = (n)+(n-1)+(n-2)
#ath! n-1 = talan sem kom einu skerfi á undan í rununni.
num = int(input("Enter sequence lenght: "))
current_number = 1
num_prev = 0
num_prev2 = 0          
for i in range(1, num+1):
    num_next =  current_number + num_prev + num_prev2
    print(num_next)
    num_prev2 = num_prev
    num_prev = current_number
    current_number = num_next
    
          
          
          
          

