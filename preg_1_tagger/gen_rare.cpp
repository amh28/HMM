#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <sstream>

using namespace std;

typedef string S;
typedef stringstream SS;

void replace(S file_in, S file_out, S word)
{
	ifstream iff(file_in);
	ifstream count("gene.counts");
	ofstream off(file_out);
	
	map<S,int> no_frec;
	bool flag=1;
	
	//MAP WORDS
	while(!count.eof() && flag)
	{
		S line;	getline(count, line);
		SS ss(line);
		
		S part;		ss>>part;
		int frec = stoi(part);
		S word;    ss>>word;
		if(word=="WORDTAG")	{
			ss>>part; ss>>part;
			no_frec[part]+=frec;				
		}
			else flag=0;
	}
	
	while(!iff.eof())
	{
		S line;	getline(iff, line);
		if(line.size()!=0)
		{
			SS ss(line);
			S part;
			ss>>part; 
			if(no_frec[part]<5)
			{
				ss>>part;
				off<<"_RARE_"<<" "<<part<<endl;
			}
			else
			{
				off<<part<<" "; ss>>part; off<<part<<endl;
			}
		}
		else off<<endl;
	}
	
}


int main()
{
	replace("gene.train", "gene_rare.train", "_RARE_");
	
}





