#include <string>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <set>
#include <cmath>
#include <fstream>
#include <list>
#include <vector>
#include <unordered_map>
#include <boost/tokenizer.hpp>
#include <boost/tokenizer.hpp>
#include <boost/numeric/ublas/matrix.hpp>
#include <boost/numeric/ublas/matrix_sparse.hpp>
#include <boost/numeric/ublas/io.hpp>

using namespace std;
using namespace boost::numeric::ublas;

typedef boost::tokenizer<boost::char_separator<char> > tokenizer;
typedef pair <string,string> Entry;
typedef std::list <Entry> Doc;
boost::char_separator<char> sep("\t");
tokenizer::iterator tok_iter;

int main(int argc, char** argv) {
   if (argc !=2) return -1;
   string foo = argv[1];
   std::size_t pos = foo.find(".");
   string foo_preffix = foo.substr(0,pos);
   string line, species, fint, tf_st;
   ifstream myfile (foo);
   std::unordered_multimap<string, Doc> corpus;
   if (myfile.is_open()) {
      while (getline(myfile,line)) {
	tokenizer tokens(line, sep);
	tok_iter = tokens.begin();
	if (tok_iter != tokens.end()) {
	   species = *tok_iter;
	   ++tok_iter;
	}
	if (tok_iter != tokens.end()) {
	   fint = *tok_iter;
	   ++tok_iter;
	}
	if (tok_iter != tokens.end()) {
	   tf_st = *tok_iter;
	}
	if (!species.empty() && !fint.empty() && !tf_st.empty()) {
	   Entry entry (fint,tf_st);
	   std::unordered_map<string, Doc>::const_iterator got = corpus.find(species);
	   if (got == corpus.end()) {
		Doc doc;
		doc.push_back(entry);
		std::pair<string, Doc> mypair (species, doc);
		corpus.insert (mypair);
	   }
	   else {
		Doc doc;
		doc = got->second;
		doc.push_back(entry);
		corpus.erase(species);
		std::pair<string, Doc> mypair (species, doc);
                corpus.insert (mypair);
	   }
	}
      }
      unsigned nspecies = corpus.bucket_count();
      int k = 0;
      ofstream outfile;
      outfile.open (foo_preffix+"_labelmap.sub");
      for (int i=0; i < nspecies; i++){
        if (corpus.bucket_size(i) >= 1){
           for (auto it=corpus.begin(i); it != corpus.end(i); it++) {
		species = it-> first;
		Doc doc = it->second;
		cout << "[" << k << "] ";
	 	outfile << k << " " << species << endl;
		for (std::list<Entry>::iterator doc_it=doc.begin(); doc_it !=doc.end(); ++doc_it) {
		   fint = doc_it->first;
		   tf_st = doc_it->second;
		   int tf = stoi(tf_st);
		   tf = (int)floor(log2(tf)) + 1;
		   while (tf > 0) {
		      cout << fint << " ";
		      tf--;
		   }
		}
		cout << endl;
		k++;
	   }
   	}
      }
   }
   return 0;
}
