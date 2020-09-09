#include "polynom.hpp"
#include <iostream>
#include <utility>
int main(int argc, const char** argv) {
    std::vector<double> v{-14, -2, 1, -3, 1};
    Polynom p(v);
    std::cout << p << std::endl << std::endl;
    auto solutions = p.SolveAll({std::make_pair(-1.7, -.5), std::make_pair(3., 4.)}, 0.00001);
    for(auto solution : solutions) { 
        std::cout << std::get<0>(solution) << "\t" << std::get<1>(solution) << "\t" << std::get<2>(solution) << "\n";
    }
    return 0;
}