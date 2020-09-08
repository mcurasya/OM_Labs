#include "polynom.hpp"
#include <iostream>
#include <utility>
int main(int argc, const char** argv) {
    std::vector<double> v{-14, -2, 1, -3, 1};
    Polynom p(v);
    std::cout << p << std::endl << std::endl;
    auto solutions = p.SolveAll({std::make_pair(-2., 0.), std::make_pair(0., 4.)}, 0.00001);

    return 0;
}