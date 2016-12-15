#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <sstream>

using namespace std;

typedef string S;
typedef stringstream SS;

S get_class(S word);

void replace(S file_in, S file_out)
{
	ifstream iff(file_in);
	ifstream count("gene.counts");
	ofstream off(file_out);
	
	map<S,int> no_frec;
	bool flag=1;
	
	
	cout<<"holi"<<endl;
	//MAP WORDS
	while(!count.eof() && flag)
	{
		S line;	getline(count, line);
		SS ss(line);
			cout<<"holi"<<endl;
		S part;		ss>>part;
		int frec = stoi(part);
		S word;    ss>>word;
		if(word=="WORDTAG")	{
			ss>>part; ss>>part;
			no_frec[part]+=frec;				
		}
			else flag=0;
	}
	cout<<"holi"<<endl;
	
	while(!iff.eof())
	{
		S line;	getline(iff, line);
		if(line.size()!=0)
		{
			SS ss(line);
			S word,part; 
			ss>>word; 
			if(no_frec[word]<5)
			{	
				S w_class = get_class(word);
				off<<word<<" "<<w_class<<endl;
			}
			else
			{
				off<<word<<" "; ss>>part; off<<part<<endl;
			}
		}
		else off<<endl;
	}
	
}

S get_class(S word)
{
	size_t word_s = word.size();
	bool all_cap=1, last_cap = 0;
	for(size_t i=0; i<word_s; i++)
	{
		if(isdigit(word[i])) return "NUMERIC";
		if(!isupper(word[i])) all_cap = 0; 
		if(i==word_s-1)
		{
			if(isupper(word[i]))
			{
				if(all_cap==0) return "LASTCAP";
				else if(all_cap==1) return "ALLCAPS";
			}
		}
	}
	
	return "RARE";
	
	
}

int main()
{
	replace("gene.train", "gene_rare_classes.train");
	
}





