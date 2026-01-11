# now this is a sample file inside python practice folder

# 1. open temrminal do it ctrl + j and go to command prompt
# 2. write git add .
# 3. write git commit -m "second commit"
# 4 write git push origin main
# your code is uploaded now 
# to check go to your repository through chrome,
# or write git remote -v , it willl show you a link , clik 
# on it to directly go to chrome webiste, (internet is needed)
# dont forget to save before uploadnig 


# samlpe code
num1 = int (input())
num2 = int (input())
sum = num1 + num2
print(sum)

# reverse a number
n = int(input())
rev = 0
temp = abs(n)
while temp > 0:
	rev = rev * 10 + temp % 10
	temp //= 10
if n < 0:
	rev = -rev
print(rev)

