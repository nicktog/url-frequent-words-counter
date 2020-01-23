import urllib

peat = list()
counts = dict()

fhand = urllib.urlopen('http://www.cracked.com')
for line in fhand:
   words = line.split()
   for word in words:
      counts[word] = counts.get(word,0) + 1
      
for k,v in counts.items():
    peat.append((v,k))
peat.sort(reverse=True)
for k,v in peat:
    if k > 1:
        print k,v
   
#print counts
