#include <vector>
#include <string>

class Polynom
{
private:
    std::vector<double> coefficients; //starting from x^0 to x^(size - 1)
public:
    template <typename InputIt>
    Polynom(InputIt begin, InputIt end);
    ~Polynom();
    std::string ToString();
};