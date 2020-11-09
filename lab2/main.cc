#include <fstream>
#include <iomanip>
#include <iostream>

#include "SLAE.hh"
int main() {
  std::ifstream fin("text.txt");
  SLAE sl(fin);
  Solution s = sl.Solve();

  return 0;
}