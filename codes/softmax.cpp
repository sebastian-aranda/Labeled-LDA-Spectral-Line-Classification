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
boost::char_separator<char> sep(" ");
tokenizer::iterator tok_iter;

int main(int argc, char** argv) {
   if (argc !=2) return -1;
   string foo = argv[1];
   string line, token, species, value_st;
   ifstream myfile (foo);
   if (myfile.is_open()) {
      while (getline(myfile,line)) {
	double max = 0.0;
	string max_id = "0";
	tokenizer tokens(line, sep);
	tok_iter = tokens.begin();
	while (tok_iter != tokens.end()) {
	   token = *tok_iter;
	   std::size_t found = token.find_first_of(":");
	   string id = token.substr(0,found);
	   int len = token.length();
	   string num_st = token.substr(found+1,len);
	   double num = std::stod(num_st);
	   if (num > max) {
	      max = num;
	      max_id = id;
	   }
	   ++tok_iter;
        }
	cout << "[" << max_id << "]" << endl;
      }
   }
   return 0;
}
