namespace Andersc.AlgorithmInCs.Algorithms.Problems
{
    public class Maths
    {
        public static long Factorial(int n)
        {
            return n > 0 ? n * Factorial(n - 1) : 1;
        }
    }
}
