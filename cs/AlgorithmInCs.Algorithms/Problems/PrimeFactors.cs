using System;
using System.Collections.Generic;

namespace Andersc.AlgorithmInCs.Algorithms.Problems
{
    public class PrimeFactors
    {
        /// <summary>
        /// Gets the prime factors of the specified number.
        /// Assumes that 0, 1 and -1 don't have prime factors;
        /// and n has the same factors to -n.
        /// </summary>
        /// <param name="n">the number.</param>
        /// <returns>A List of int which contains the prime factors.</returns>
        public static List<int> Generate(int n)
        {
            if (Math.Abs(n) < 2) { return new List<int>(); }

            if (n < 0) { n = -n; }

            var factors = new List<int>();
            while (n % 2 == 0)
            {
                factors.Add(2);
                n = n >> 1;
            }

            for (var i = 3; i <= n / i; i += 2)
            {
                while (n % i == 0)
                {
                    factors.Add(i);
                    n /= i;
                }
            }

            if (n > 1)
            {
                factors.Add(n);
            }

            return factors;
        }
    }
}