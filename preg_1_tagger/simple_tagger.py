#!/usr/bin/python


#41072 - I-Gene, 345128 0
		
						
#READS gene.key
def read(file_in, counts):
	with open(file_in, "r") as ins:
		for line in ins:
			splitted = line.split()
			if len(splitted) != 0:
				print splitted[0]
			else:
				print ""
	
	
#RETURN MAP OF FRECUENCIES OF I_GENE AND O OF EACH WORD			
def create_map(counts):
	from collections import defaultdict
	map_frec = defaultdict(dict)
	frec_I_GENE = None
	frec_0 = None
	with open(counts, "r") as ins:
		
		#fill map
		for line in ins:
			splitted = line.split()
			if len(splitted) != 0:
				if splitted[1] == "WORDTAG":
					map_frec[splitted[3]][splitted[2]] = splitted[0]
				if splitted[1] == "1-GRAM":
					if splitted[2] == "I-GENE":
						frec_I_GENE = splitted[0]
					if splitted[2] == "O":
						frec_0 =splitted[0]
		
		#print map
		'''for word in map_frec:
			print word, '-->',
			print map_frec[word]'''
		
				
		'''
		if "volumes" in map_frec and 'I-GENE' in map_frec['volume']:
			print 'si esta'
		else:
			print map_frec["coupling"]["O"] '''
		
		
		
	return (frec_I_GENE, frec_0, map_frec)
	
#TAGS GENE.DEV
def tagger(gene_dev, output):
	frec_I_GENE, frec_0, map_frec = create_map("gene_rare.count")
	cont = 0
	OFSTREAM = open(output, 'w')				
	#READ GENE.DEV
	with open(gene_dev, "r") as ins:
		for line in ins:
			split = line.split()
			
			if len(split) != 0:
				
				word = split[0]
				cont = cont + 1
				frec_Word_IGENE = 0.0
				frec_Word_O = 0.0
				
				#IF WORD EXISTS IN MAP ASSIGN FRECUENCIES
				if(word in map_frec):
				
					if word in map_frec and 'I-GENE' in map_frec[word]:
						frec_Word_IGENE = map_frec[word]['I-GENE']
						#print("Results: word: ",word, "frec I-GENE: ",frec_Word_IGENE)
					if word in map_frec and 'O' in map_frec[word]:
						frec_Word_O = map_frec[word]['O']
						#print("Results: word: ",word, "frec O: ",frec_Word_O)
					
				#IF WORD DOESNT EXIST ASSIGN FRECUENCY OF _RARE_
				else:
						frec_Word_IGENE = map_frec["_RARE_"]['I-GENE']
						frec_Word_0 = map_frec["_RARE_"]['O']
				
				
				
				frec_Word_IGENE = int(frec_Word_IGENE)/ ( int(frec_I_GENE) * 1.0 )
				frec_Word_O = int(frec_Word_O)/ ( int(frec_0) * 1.0 )
				
				
				#ASSIGN TAG
				if frec_Word_IGENE > frec_Word_O:
					tag = "I-GENE"
				else:
					tag = "O"
									
				#WRITE THE OUTPUT
				if cont  == 1:
					OFSTREAM.write(word + " " + tag)
				else:
					OFSTREAM.write('\n'+word + " " + tag)
				
			
			else:
				OFSTREAM.write('\n')
	OFSTREAM.write('\n')
	
			
			
#read("gene.key", "gene_rare.count")
tagger("gene.dev","gene_dev.p1.out")



















