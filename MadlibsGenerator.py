with open("story.txt", "r") as f:
    cast = f.read()

l = set()
start = -1  

for i, c in enumerate(cast):
    if c == "<":
        start = i
    
    if c == ">" and start != -1: 
        l.add(cast[start:i+1])  
        start = -1

reply = {}

for w in l:
    a = input("enter a text to replace for " + w + " : ")
    reply[w] = a

for w in l:
    cast = cast.replace(w, reply[w]) 

print(cast)
