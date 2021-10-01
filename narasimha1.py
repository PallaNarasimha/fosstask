import random
list=["rock","paper","scissor"]
score1=0
score2=0
x=1
while(x<=10):
	c=random.choice(list)
	n=input("rock,paper,scissor")
	if(c=="paper" and n=="scissor"):
		score2=score2+1
	elif(c=="paper" and n=="rock"):
		score1=score1+1
	elif(c=="scissor" and n=="paper"):
		score1=score1+1
	elif(c=="scissor" and n=="rock"):
		score2=score2+1
	elif(c=="rock" and n=="scissor"):
		score1=score1+1
	elif(c=="rock" and n=="paper"):
		score2=score2+1
	x=x+1
print(score1)
print(score2)
if(score1>score2):
	print("computer won")
elif(score2>score1):
	print("you won")
else:
	print("match is draw")
	
