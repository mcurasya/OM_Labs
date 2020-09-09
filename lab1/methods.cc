#include "methods.hpp"
#include <iostream>
#include <cstdint>
#include <cmath>
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
        while (std::abs(end - begin) >= 2 * eps)
        {
            ++iterations;
            double middle = end + begin;
            middle /= 2;
            double midValue = p->GetValue(middle);
            std::cout << "iteration " << iterations << ": point " << middle << " with value " << midValue << "\n\tb = " << end << " a = " << begin << std::endl;
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
        std::cout << "Chords method" << std::endl;
        uint64_t iterations = 0;
        double begin, end;
        std::tie(begin, end) = s;
        double beginValue = p->GetValue(begin), endValue = p->GetValue(end);
        double center;
        do
        {
            center = (begin * endValue - end * beginValue) / (endValue - beginValue);
            double centValue = p->GetValue(center);
            std::cout << "iteration " << ++iterations << ": point " << center << " with value " << centValue << "\n\tb = " << end << " a = " << begin << std::endl;
            if (beginValue * centValue < 0)
            {
                endValue = centValue;
                end = center;
            }
            else
            {
                beginValue = centValue;
                begin = center;
            }
        } while (std::abs(p->GetValue(center)) >= eps);

        std::cout << "Chords method solved in " << iterations << " iterations" << std::endl;
        return center;
    }

    double Newton::operator()(Polynom *p, Section s, double eps)
    {
        uint64_t iterations = 0;
        std::cout << "Newtons method" << std::endl;
        double point;
        if (p->GetValue(s.first) * p->GetSecondDerivativeValue(s.first) > 0)
        {
            point = s.first;
        }
        else
        {
            point = s.second;
        }
        std::cout << "Starting value"
                  << ". Current point: " << point << " with value " << p->GetValue(point) << std::endl;
        while (std::abs(p->GetValue(point)) >= eps)
        {
            point -= p->GetValue(point) / p->GetDerivativeValue(point);
            std::cout << "Iteration " << ++iterations << ". Current point: " << point << " with value " << p->GetValue(point) << std::endl;
        }
        std::cout << "Newton method finished in " << iterations << " iterations" << std::endl;
        return point;
    }
} // namespace SolutionMethods