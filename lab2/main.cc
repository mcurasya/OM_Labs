#include <fstream>
#include <iomanip>
#include <iostream>

#include "SLAE.hh"
int main() {
  std::ifstream fin("text.txt");
  SLAE sl(fin);
  Solution s = sl.Solve();
  std::cout << std::get<1>(s) * sl.matr << std::endl;
  std::vector<double> X = std::get<0>(s);
  std::vector<double> r(X.size());
  std::vector<double> Ax(X.size());

  std::cout << "NEVYAZKA VECTOR" << std::endl;
  for (int i = 0; i < r.size(); i++) {
    for (size_t j = 0; j < r.size(); j++) {
      Ax[i] += sl.matr[i][j] * X[j];
    }
    r[i] = sl.answers[i] - Ax[i];
    std::cout << "\t" << r[i] << std::endl;
  }
  return 0;
}