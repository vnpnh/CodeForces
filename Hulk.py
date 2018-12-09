n = int(input())

hate = "I hate it"
love = " I love it "


output = ""
if n == 1:
    output+=hate
else:
    for i in range(1,n+1):
        if i%2 == 1 and i!=n:
            output+=hate.replace("it","that")
        if i%2 == 0 and i!=n:
            output+=love.replace("it","that")
        if i%2 == 1 and i==n:
            output+=hate
        if i%2 == 0 and i==n:
            output+=love
           

print(output.lstrip())
    
