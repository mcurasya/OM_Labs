using System;

namespace task1
{
  class Program
  {
    static double Sqr(double x)
    {
      return x * x;
    }
    static double Norm(double x, double new_x, double y, double new_y)
    {
      return Math.Sqrt(Sqr(new_x - x) + Sqr(new_y - y));
    }
    static void Main(string[] args)
    {
      Console.WriteLine("enter epsilon");
      double eps = Convert.ToDouble(Console.ReadLine());

      double alpha = 0.571;
      double beta = -0.682;
      double b = -1.587;
      double c = 0.835;
      double d = 0.868;
      double x = 0;
      double y = 0;
      double new_x = 0;
      double new_y = 0;
      do
      {
        x = new_x;
        y = new_y;
        Console.WriteLine($"new x = {Math.Round(new_x, 5)};\tnew y = {Math.Round(new_y, 5)};");
        new_x = d - Math.Cos(y + beta);
        new_y = c / b - Math.Sin(x + alpha) / b;
      } while (Norm(x, new_x, y, new_y) > eps);
      Console.WriteLine($"final x = {Math.Round(new_x, 5)};\tfinal y = {Math.Round(new_y, 5)};");
    }
  }
}
