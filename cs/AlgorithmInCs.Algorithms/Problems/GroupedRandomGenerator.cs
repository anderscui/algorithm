using System;
using System.Linq;
using Andersc.AlgorithmInCs.Common;

namespace Andersc.AlgorithmInCs.Algorithms.Problems
{
    public class GroupedRandomGenerator
    {
        private int[] ranges;
        private int uppperBound;
        private Random random;

        public GroupedRandomGenerator(int n)
        {
            var prop = new int[n];
            for (var i = 0; i < n; i++)
            {
                prop[i] = 1;
            }

            Init(prop);
        }

        public GroupedRandomGenerator(int[] proportions)
        {
            Init(proportions);
        }

        private void Init(int[] proportions)
        {
            CheckProportions(proportions);
            
            if (proportions.Average() < 5)
            {
                for (var i = 0; i < proportions.Length; i++)
                {
                    proportions[i] *= 10;
                }
            }

            ranges = proportions.CumulativeSum().ToArray();
            uppperBound = ranges[ranges.Length - 1];
            random = new Random();
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

        private int Next()
        {
            return random.Next(1, uppperBound+1);
        }

        public int NextGroupIndex()
        {
            var next = Next();
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
