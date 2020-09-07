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
    return std::make_tuple(_Solve(b, s, eps),
                           _Solve(n, s, eps),
                           _Solve(c, s, eps));
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

std::vector<Solutions> Polynom::SolveAll(std::vector<Section> sections, double eps)
{
    std::vector<Solutions> sols;
    for (auto section : sections)
    {
        sols.push_back(Solve(section, eps));
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

template <class Functor>
double Polynom::_Solve(Functor solutionMethod, Section s, double eps)
{
    return solutionMethod(this, s, eps);
}
