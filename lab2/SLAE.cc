#include "SLAE.hh"

#include <assert.h>

#include <algorithm>
#include <fstream>
#include <iomanip>
#include <sstream>

SLAE::SLAE(const table& matrix, const std::vector<double>& answers) {
  this->size = matrix.size();
  assert(size == matrix[0].size());
  matr = matrix;
  this->answers = answers;
}

SLAE::SLAE(std::ifstream& is) {
  table t;
  while (is) {
    std::string line;
    getline(is, line);
    std::istringstream iss(line);
    std::vector<double> vec;
    double elem;
    while (iss) {
      iss >> elem;
      vec.push_back(elem);
    }
    t.push_back(vec);
  }
  int size = t.size();
  std::vector<double> ans;
  for (int i = 0; i < t.size(); i++) {
    ans.push_back(t[i][t[i].size() - 1]);
    t[i].pop_back();
    t[i].pop_back();
  }
  t.pop_back();
  t.shrink_to_fit();
  ans.pop_back();
  ans.shrink_to_fit();
  std::cout << std::endl;
  *this = SLAE(t, ans);
}

Solution SLAE::Solve() const {
  return Gaussian(matr, answers);
}

Solution Gaussian(table t, std::vector<double> answers) {
  table inv(t.size());
  for (size_t i = 0; i < inv.size(); i++) {
    inv[i] = std::vector<double>(t.size());
    inv[i][i] = 1;
  }

  for (int i = 0; i < t.size(); i++) {
    for (int j = 0; j < t.size(); ++j) {
      if (j == i) {
        continue;
      }

      inv[j] = inv[j] - inv[i] * t[j][i] / t[i][i];
      answers[j] = answers[j] - answers[i] / t[i][i] * t[j][i];
      t[j] = t[j] - t[i] / t[i][i] * t[j][i];
    }
    for (int i = 0; i < t.size(); i++) {
      for (int j = 0; j < t.size(); j++) {
        std::cout << std::left << std::setw(12) << t[i][j] << " ";
      }
      std::cout << "| " << answers[i] << std::endl;
    }
    std::cout << std::endl;
  }

  double det = 1;
  for (int i = 0; i < t.size(); i++) {
    det *= t[i][i];
    inv[i] = inv[i] / t[i][i];
  }
  std::cout << "inverse matrix: " << std::endl;
  for (int i = 0; i < t.size(); i++) {
    for (int j = 0; j < t.size(); j++) {
      std::cout << std::setw(12) << inv[i][j] << " ";
    }
    std::cout << std::endl;
  }
  std::cout << "determinant = " << det << std::endl;
  std::vector<double> solutions(t.size());
  std::cout << "solution of system: " << std::endl;
  for (size_t i = 0; i < t.size(); i++) {
    solutions[i] = answers[i] / t[i][i];
    std::cout << "\t" << solutions[i] << std::endl;
  }
  return std::tie(solutions, inv, det);
}

std::vector<double> operator+(const std::vector<double>& v1, const std::vector<double>& v2) {
  std::vector<double> result(v1.size());
  for (size_t i = 0; i < result.size(); i++) {
    result[i] = v1[i] + v2[i];
  }
  return result;
}

std::vector<double> operator-(const std::vector<double>& v1, const std::vector<double>& v2) {
  std::vector<double> result(v1.size());
  for (size_t i = 0; i < result.size(); i++) {
    result[i] = v1[i] - v2[i];
  }
  return result;
}

std::vector<double> operator/(const std::vector<double>& v, double num) {
  std::vector<double> result(v.size());
  for (size_t i = 0; i < result.size(); i++) {
    result[i] = v[i] / num;
  }
  return result;
}

table operator*(const table& v1, const table& v2) {
  table result(v1.size());
  for (size_t i = 0; i < result.size(); i++) {
    result[i] = std::vector<double>(v2.size());
  }

  for (int i = 0; i < result.size(); i++) {
    for (int j = 0; j < result[i].size(); j++) {
      for (int k = 0; k < v2.size(); k++) {
        result[i][j] += v1[i][k] * v2[k][j];
      }
    }
  }
  return result;
}

std::vector<double> operator*(const std::vector<double>& v, double num) {
  std::vector<double> result(v.size());
  for (size_t i = 0; i < result.size(); i++) {
    result[i] = v[i] * num;
  }
  return result;
}

std::ostream& operator<<(std::ostream& os, SLAE sl) {
  bool first = true;

  os << "size: " << sl.size << std::endl;
  for (size_t i = 0; i < sl.size; i++) {
    if (!first) {
      os << std::endl;
    }
    first = false;
    for (size_t j = 0; j < sl.size; j++) {
      os << sl.matr[i][j] << "\t";
    }
    os << "| " << sl.answers[i];
  }
  return os;
}
