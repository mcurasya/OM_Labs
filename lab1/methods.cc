#include "methods.hpp"
#include <iostream>
#include <cstdint>
namespace SolutionMethods
{
    double Bisections::operator()(Polynom *p, Section s, double eps)
    {
        std::cout << "Bisections method\n";
        uint64_t iterations = 0;
        double begin = s.first;
        double end = s.second;
        double beginValue = p->GetValue(begin);
        double endValue = p->GetValue(end);
        while (end - begin >= 2 * eps)
        {
            ++iterations;
            double middle = end + begin;
            middle /= 2;
            double midValue = p->GetValue(middle);
            std::cout << "iteration " << iterations << ": point " << middle << " with value " << midValue << std::endl;
            if (midValue * beginValue < 0)
            {
                end = middle;
                endValue = midValue;
            }
            else
            {
                begin = middle;
                beginValue = midValue;
            }
        }
        std::cout << "Bisections method solved in " << iterations << " iterations" << std::endl;
        return (end + begin) / 2;
    }

    double Chords::operator()(Polynom *p, Section s, double eps)
    {
        return 0;
    }

    double Newton::operator()(Polynom *p, Section s, double eps)
    {
        return 0;
    }
} // namespace SolutionMethods