#pragma once
#include "polynom.hpp"
namespace SolutionMethods
{
    class Bisections
    {
    public:
        double operator()(Polynom *p, Section s, double eps);
    };

    class Chords
    {
    public:
        double operator()(Polynom *p, Section s, double eps);
    };

    class Newton
    {
    public:
        double operator()(Polynom *p, Section s, double eps);
    };
} // namespace SolutionMethods