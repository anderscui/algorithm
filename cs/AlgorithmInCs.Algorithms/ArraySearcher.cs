﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Andersc.AlgorithmInCs.Algorithms
{
    /// <summary>
    /// From b1, ch02
    /// Demonstrates basic impls of searching elements in an array.
    /// Given N objects(to search in), M other objects(to be searched), commonly M is much larger than N.
    /// </summary>
    public class ArraySearcher
    {
        private static readonly int NotFound = -1;

        /// <summary>
        /// O(N)
        /// </summary>
        public static int Sequential(int[] a, int v, int left, int right)
        {
            for (int i = left; i <= right; i++)
            {
                if (a[i] == v)
                {
                    return i;
                }
            }
            return NotFound;
        }

        /// <summary>
        /// O(lgN)
        /// While we need the "a" is sorted in some way, the sorting cost is O(NlgN),
        /// if M is much larger than N, this cost is negligible.
        /// </summary>
        public static int Binary(int[] a, int v, int left, int right)
        {
            for (int i = left; i <= right; i++)
            {
                if (a[i] == v)
                {
                    return i;
                }
            }
            return NotFound;
        }
    }
}
