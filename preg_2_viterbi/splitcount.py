import sys
def main():
	f=open('gene_rare.count','r')
	f2=open('trigram','w')
	f3=open('bigram','w')
	f4=open('unigram','w')
	for line in f:
		p=line.split()
		if(p[1]=='3-GRAM'):	
			f2.write(line)
		if(p[1]=='2-GRAM'):
			f3.write(line)
		if(p[1]=='WORDTAG'):
			f4.write(line)
	
	
if __name__=='__main__':
	main()
