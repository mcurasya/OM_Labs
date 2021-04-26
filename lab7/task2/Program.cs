using System;

namespace task2
{
    class Program
    {
        static double func(double x, double y)
        {
            if (y < Math.Sqrt(x) && y > -x * x)
            {
                return 9 * x * x * y * y + 48 * x * x * y * y * x * y;
            }
            return 0;
        }
        static double xi(double i, double h)
        {
            return i * h;
        }
        static double yi(double j, double k)
        {
            return -1 + j * k;
        }
        static double CubicSimpson(int n, int m)
        {
            double sum = 0;
            double h = 1.0 / (2 * n);

            double k = 2.0 / (2 * m);
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < m; j++)
                {
                    sum += func(xi(2 * i, h), yi(2 * j, k)) + func(xi(2 * i + 2, h), yi(2 * j, k)) + func(xi(2 * i, h), yi(2 * j + 2, k)) + func(xi(2 * i + 2, h), yi(2 * j + 2, k));
                    sum += 4 * (func(xi(2 * i + 1, h), yi(2 * j, k)) + func(xi(2 * i + 2, h), yi(2 * j + 1, k)) + func(xi(2 * i + 1, h), yi(2 * j + 2, k)) + func(xi(2 * i, h), yi(2 * j + 1, k)));
                    sum += 16 * func(xi(2 * i + 1, h), yi(2 * j + 1, k));
                    // Console.WriteLine($"xi = {xi(2 * i, h)}, yi = {yi(2 * j, k)} func = {func(xi(2 * i, h), yi(2 * j, k))}");
                }
            }
            return sum * h * k / 9;
        }
        static void Main(string[] args)
        {
            for (int i = 1; i < 1000; i++)
            {
                for (int j = 1; j < 200; j++)
                {
                    double res = CubicSimpson(i, j);
                    Console.WriteLine($"for n = {i} and m = {j} integral = {res}");
                    if (Math.Abs(res - 2) / 2 < 0.02)
                    {
                        Console.WriteLine($"optimal valuse for n and m are {i} and {j} respectively");
                        goto end;
                    }
                }
            }
        end:
            return;
        }
    }
}
