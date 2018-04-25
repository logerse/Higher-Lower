from random import randrange as rnd
name=raiting=''
base=[]
lastname=name=lastraiting=''
points=0
LastInd=-1
def startProg():
    mainfile=open('reit')
    for line in mainfile: #create list with text lines (Name Raiting)
        base.append(line.strip())

def create():
	global lastraiting,raiting,lastname,name,Ind_2
	Ind_1=rnd(len(base))
	Ind_2=rnd(len(base))
	while Ind_2==Ind_1:
		Ind_2=rnd(len(base))
	#lastname:
	lastname=base[Ind_1].split(' ')[0]; lastraiting=base[Ind_1].split(' ')[1]
	#name:
	name=base[Ind_2].split(' ')[0]; raiting=base[Ind_2].split(' ')[1]

def checkans(ans):
	global raiting,lastraiting
	#true_ans
	print(lastraiting,'|',raiting)
	if lastraiting>raiting:
		true_ans=1
	else:
		true_ans=2
	#check user_ans
	print(ans,'|',true_ans)
	if ans==true_ans:
		return True
	else:
		return False
def refresh():
	global raiting,name,lastraiting,lastname,Ind_2
	lastname=name; lastraiting=raiting
	name=raiting=''
	Ind=Ind_2
	Ind_2=rnd(len(base))
	while Ind==Ind_2:
		Ind_2=rnd(len(base))
	name=base[Ind_2].split(' ')[0]
	raiting=base[Ind_2].split(' ')[1]
