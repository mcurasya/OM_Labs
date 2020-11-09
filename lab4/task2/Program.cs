using System;

namespace task2
{
  struct Point
  {
    public double X;
    public double Y;
    public Point(double x, double y)
    {
      X = x;
      Y = y;
    }
    public static Point operator -(Point p1, Point p2)
    {
      return new Point(p1.X - p2.X, p1.Y - p2.Y);
    }
    public double Norm() => Math.Sqrt(X * X + Y * Y);
  }

  class Program
  {
    static double function_for_x(Point p)
    {
      return Math.Sqrt(Math.Tan(p.X * p.Y + 0.571));
    }

    static double function_for_y(Point p)
    {
      return Math.Sqrt(0.56 * p.X * p.X - 1);
    }
    static void Main(string[] args)
    {
      Console.Write("Enter epsilon");
      double eps = int.Parse(Console.ReadLine());
      Point p1 = new Point(1.5, 0.5);
      Point p2 = new Point(2, -1);
      Point new_point = p1;
      do
      {
        p1 = new_point;
        new_point.X = function_for_x(p1);
        new_point.Y = function_for_y(p1);
        Console.WriteLine()
      } while ();
    }
  }
}
