#include "polynom.hpp"
#include "methods.hpp"
#include <algorithm>
#include <sstream>
#include <cmath>
#include <iterator>
#include <cmath>

Polynom::Polynom(const std::vector<double> &v)
{
    coefficients = v;
    auto a = end(coefficients) - 1;
    for (; a >= begin(coefficients); --a)
    {
        if (*a != 0)
        {
            break;
        }
    }
    if (++a != end(coefficients))
    {
        coefficients.erase(a, end(coefficients));
    }

    for (int i = 1; i < coefficients.size(); ++i)
    {
        derivativeCoeffs.push_back(i * coefficients[i]);
    }
    for(int i = 1; i < derivativeCoeffs.size(); ++i){
        secondDerivativeCoeffs.push_back(i * derivativeCoeffs[i]);
    }
}

Polynom::~Polynom()
{
}

std::vector<double> Polynom::getCoefficients() const
{
    return coefficients;
}

Solutions Polynom::Solve(Section s, double eps)
{
    SolutionMethods::Bisections b;
    SolutionMethods::Chords c;
    SolutionMethods::Newton n;
    std::cout << std::endl;
    auto result1 = _Solve(b, s, eps);
    std::cout << std::endl;
    auto result2 = _Solve(c, s, eps);
    std::cout << std::endl;
    auto result3 = _Solve(n, s, eps);
    std::cout << std::endl;
    std::cout << std::endl;
    return std::make_tuple(result1, result2, result3);
}

double Polynom::GetValue(double x)
{
    double result = 0;
    for (int i = 0; i < coefficients.size(); ++i)
    {
        result += std::pow(x, i) * coefficients[i];
    }
    return result;
}

double Polynom::GetDerivativeValue(double x)
{
    double result = 0;
    for (int i = 0; i < derivativeCoeffs.size(); ++i)
    {
        result += std::pow(x, i) * derivativeCoeffs[i];
    }
    return result;
}

double Polynom::GetSecondDerivativeValue(double x)
{
    double result = 0;
    for (int i = 0; i < secondDerivativeCoeffs.size(); ++i)
    {
        result += std::pow(x, i) * secondDerivativeCoeffs[i];
    }
    return result;
}

std::vector<Solutions> Polynom::SolveAll(std::vector<Section> sections, double eps)
{
    std::vector<Solutions> sols;
    int i = 1;
    for (auto section : sections)
    {
        std::cout << "root " << i << std::endl;
        std::cout << "Section: " << section;
        sols.push_back(Solve(section, eps));
        ++i;
    }
    return sols;
}

std::ostream &operator<<(std::ostream &os, const Polynom &p)
{
    std::vector<double> coefficients = p.getCoefficients();
    os << coefficients[0];
    for (int i = 1; i < coefficients.size(); ++i)
    {
        os << " ";
        if (coefficients[i] < 0)
        {
            os << "-";
        }
        else
        {
            os << "+";
        }
        os << " ";
        if (std::abs(coefficients[i]) != 1)
        {
            os << std::abs(coefficients[i]);
        }
        os << "x";
        if (i != 1)
        {
            os << "^" << i;
        }
    }
    os << " = 0";
    return os;
}

std::ostream& operator<<(std::ostream &os, const Section &p) 
{
    os << "[" << p.first << ", " << p.second << "]";
    return os;
}

template <class Functor>
double Polynom::_Solve(Functor solutionMethod, Section s, double eps)
{
    return solutionMethod(this, s, eps);
}
