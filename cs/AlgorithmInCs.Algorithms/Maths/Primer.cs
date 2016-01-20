using System;
using System.Collections.Generic;
using System.Linq;

namespace Andersc.AlgorithmInCs.Algorithms.Maths
{
    public static class Primer
    {
        public static int[] PrimesLessThan1000 = 
        { 
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
            31,   37,   41,   43,   47,   53,   59,   61,   67,   71, 
            73,   79,   83,   89,   97,  101,  103,  107,  109,  113, 
            127,  131,  137,  139,  149,  151,  157,  163,  167,  173, 
            179,  181,  191,  193,  197,  199,  211,  223,  227,  229, 
            233,  239,  241,  251,  257,  263,  269,  271,  277,  281, 
            283,  293,  307,  311,  313,  317,  331,  337,  347,  349, 
            353,  359,  367,  373,  379,  383,  389,  397,  401,  409, 
            419,  421,  431,  433,  439,  443,  449,  457,  461,  463, 
            467,  479,  487,  491,  499,  503,  509,  521,  523,  541, 
            547,  557,  563,  569,  571,  577,  587,  593,  599,  601, 
            607,  613,  617,  619,  631,  641,  643,  647,  653,  659, 
            661,  673,  677,  683,  691,  701,  709,  719,  727,  733, 
            739,  743,  751,  757,  761,  769,  773,  787,  797,  809, 
            811,  821,  823,  827,  829,  839,  853,  857,  859,  863, 
            877,  881,  883,  887,  907,  911,  919,  929,  937,  941, 
            947,  953,  967,  971,  977,  983,  991,  997 
        };

        public static bool IsPrime(int n)
        {
            if (n <= 0) { throw new ArgumentOutOfRangeException("n"); }

            if (n == 1) { return false; }
            if (n == 2 || n == 3) { return true; }

            if (n % 2 == 0) { return false; }

            int upper = (int)Math.Ceiling(Math.Sqrt(n));
            for (int i = 3; i <= upper; i += 2)
            {
                if (n % i == 0)
                {
                    return false;
                }
            }

            return true;
        }

        public static bool IsPrime(long n)
        {
            if (n <= 0) { throw new ArgumentOutOfRangeException("n"); }

            if (n == 1 || n % 2 == 0) { return false; }
            if (n == 2 || n == 3) { return true; }

            int upper = (int)Math.Ceiling(Math.Sqrt(n));
            for (int i = 3; i <= upper; i += 2)
            {
                if (n % i == 0)
                {
                    return false;
                }
            }

            return true;
        }

        public static List<int> GetPrimesBelow(int n)
        {
            if (n <= 0) { throw new ArgumentOutOfRangeException("n"); }

            List<int> result = new List<int>();
            if (n == 1) { return result; }

            result.Add(2);
            if (n == 2) { return result; }

            for (int i = 3; i <= n; i += 2)
            {
                if (IsPrime(i))
                {
                    result.Add(i);
                }
            }

            return result;
        }

        /// <summary>
        /// Assumes that 0, 1 and -1 don't have prime factors;
        /// and n has the same factors to -n.
        /// </summary>
        /// <param name="n"></param>
        /// <returns></returns>
        public static List<int> GetPrimeFactors(int n)
        {
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

        public static List<int> GetPrimeFactors2(int n)
        {
            var factors = new List<int>();

            var counter = 0;
            for (var i = 2; i <= n / i; i++)
            {
                counter++;
                while (n % i == 0)
                {
                    factors.Add(i);
                    n /= i;

                    counter++;
                }
            }
            if (n > 1)
            {
                factors.Add(n);
            }

            Console.WriteLine(counter);
            return factors;
        }

        public static List<int> GetPrimeFactors3(int n)
        {
            var factors = new List<int>();

            var counter = 1;
            while (n % 2 == 0)
            {
                factors.Add(2);
                n = n >> 1;

                counter++;
            }

            for (var i = 3; i <= n / i; i += 2)
            {
                counter++;
                while (n % i == 0)
                {
                    factors.Add(i);
                    n /= i;

                    counter++;
                }
            }

            if (n > 1)
            {
                factors.Add(n);
            }

            Console.WriteLine(counter);
            return factors;
        }
    }
}
