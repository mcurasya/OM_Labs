#pragma once
#include <tuple>
#include <vector>
#include <string>
#include <utility>
#include <iostream>

using Section = std::pair<double, double>;
using Solutions = std::tuple<double, double, double>;

class Polynom
{
private:
    std::vector<double> coefficients; //starting from x^0 to x^(size - 1)
    std::vector<double> derivativeCoeffs;
    template<class Functor>
    double _Solve(Functor solutionMethod, Section s, double eps);
public:
    Polynom(const std::vector<double>& v);
    ~Polynom();
    std::vector<double> getCoefficients() const;
    Solutions Solve(Section s, double eps);
    double GetValue(double x);
    double GetDerivativeValue(double x);
    std::vector<Solutions> SolveAll(std::vector<Section> sections, double eps);
};

std::ostream &operator<<(std::ostream &os, const Polynom &p);