using System;
using System.Linq;
using Andersc.AlgorithmInCs.Common;

namespace Andersc.AlgorithmInCs.Algorithms.Problems
{
    public class GroupedDigitsGenerator
    {
        private int[] ranges;
        private int bucketSize;
        private int seed;

        public GroupedDigitsGenerator(int n, int seed, int digits = 2)
        {
            var prop = new int[n];
            for (var i = 0; i < n; i++)
            {
                prop[i] = 1;
            }

            Init(prop, seed, digits);
        }

        public GroupedDigitsGenerator(int[] proportions, int seed, int digits = 2)
        {
            Init(proportions, seed, digits);
        }

        private void Init(int[] proportions, int seed, int digits)
        {
            CheckProportions(proportions);
            
            if (proportions.Average() < 5)
            {
                for (var i = 0; i < proportions.Length; i++)
                {
                    proportions[i] *= 10;
                }
            }

            bucketSize = (int)Math.Pow(10, digits);
            ranges = proportions.CumulativeSum().ToArray();
            for (var i = 0; i < ranges.Length; i++)
            {
                ranges[i] = ranges[i] * bucketSize / ranges[ranges.Length - 1];
            }

            this.seed = seed;
        }

        private void CheckProportions(int[] proportions)
        {
            if (proportions.IsEmpty() || proportions.Length < 2)
            {
                throw new ArgumentException("proportions should contain at least 2 elements.", "proportions");
            }

            if (proportions.Any(p => p <= 0))
            {
                throw new ArgumentException("proportions should contain positive numbers only.", "proportions");
            }
        }

        public int NextGroupIndex()
        {
            var next = seed % bucketSize + 1;
            return Index(next);
        }

        private int Index(int number)
        {
            var i = 0;
            while (number > ranges[i])
            {
                i++;
            }
            return i;
        }
    }
}
