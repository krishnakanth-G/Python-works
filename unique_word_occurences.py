string = "one two three one one two three"
words = string.split()
unique = []
for word in words:
    if word not in unique:
        unique.append(word)

for i in range(0,len(unique)):
    counts = string.count(unique[i])
    print("('",unique[i],"',",counts,")",end =" ")
