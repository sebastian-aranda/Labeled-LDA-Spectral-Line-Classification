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
   if (argc !=3) return -1;
   string foo_1 = argv[1];
   string foo_2 = argv[2];
   string line_1, line_2;
   ifstream myfile_1 (foo_1);
   ifstream myfile_2 (foo_2);
   int cases = 0;
   int matches = 0;
   if (myfile_1.is_open() && myfile_2.is_open()) {
     while (getline(myfile_1, line_1) && getline(myfile_2, line_2)) {
	if (line_1 == line_2) matches++;
	cases++;
     }
     double acc = 100*(double)matches/(double)cases;
     cout << std::setprecision(8) << acc << endl;
   }
   return 0;
}
