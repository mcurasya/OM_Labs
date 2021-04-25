using System;

namespace task1
{
    class Program
    {
        static double func(double x)
        {
            return Math.Pow(Math.Sin(3 * x) * Math.Cos(3 * x), 4);
        }

        static double RectIntegration()
        {
            double sum = 0;
            double h = 0.013068536780368406;
            for (double i = 0; i <= 2 * Math.PI; i += h)
            {
                sum += func(i) * h;
            }

            return sum;
        }

        static double TrapIntegration() {
            double h = 0.06514700159;
            double sum = func(0) + func(2 * Math.PI);
            for (double i = h; i < 2 * Math.PI; i += h)
            {
                sum += 2 * func(i);
            }
            return sum * h / 2;
        }

        static double SimpsonIntegration() {
            
        }
        static void Main(string[] args)
        {
            Console.WriteLine($"rectangle integration value = {RectIntegration()}");
            Console.WriteLine($"trapezoid integration value = {TrapIntegration()}");
        }
    }
}
