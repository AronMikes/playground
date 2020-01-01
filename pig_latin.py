say = input("")
lsay = say.split()
	
for word in lsay:
    print(word[1:] + word[0] + 'ay', end =" " ) 
