def palindrome(n):
    rem=p=0
    org_n=n
    while (n>0):
        rem=n%10
        p=p*10+rem
        n=n//10
    if org_n==p:
        print("No. is a palindrome.")
    else:
        print("No. is not a palindrome.")
    
nl=int(input ("Enter a number: "))
palindrome (nl)
