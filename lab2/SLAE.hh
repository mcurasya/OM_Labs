#pragma once
#include <iostream>
#include <tuple>
#include <utility>
#include <vector>
using table = std::vector<std::vector<double>>;
using Solution = std::tuple<std::vector<double>, table, double>;
class SLAE {
 private:
  size_t size;

 public:
  table matr;
  std::vector<double> answers;
  explicit SLAE(const table& matrix, const std::vector<double>& answers);
  Solution Solve() const;
  SLAE(std::ifstream& is);
  friend std::ostream& operator<<(std::ostream& os, SLAE sl);
};

Solution Gaussian(table t, std::vector<double> answers);
std::vector<double> operator+(const std::vector<double>& v1, const std::vector<double>& v2);
std::vector<double> operator-(const std::vector<double>& v1, const std::vector<double>& v2);
std::vector<double> operator/(const std::vector<double>& v, double num);
std::vector<double> operator*(const std::vector<double>& v, double num);
table operator*(const table& v1, const table& v2);
std::ostream& operator<<(std::ostream& os, const table& t); 