using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Andersc.AlgorithmInCs.Algorithms;
using Andersc.AlgorithmInCs.Common.Extensions;
using NUnit.Framework;

namespace Andersc.AlgorithmInCs.Tests.Algorithms
{
    [TestFixture]
    public class TestConnectivity
    {
        private List<Tuple<int, int>> GetTestData()
        {
            /*  3 4
                4 9
                8 0
                2 3
                5 6
                5 9
                7 3
                4 8
                6 1
            */

            return new List<Tuple<int, int>>()
            {
                new Tuple<int, int>(3, 4),
                new Tuple<int, int>(4, 9),
                new Tuple<int, int>(8, 0),
                new Tuple<int, int>(2, 3),
                new Tuple<int, int>(5, 6),
                new Tuple<int, int>(2, 9),
                new Tuple<int, int>(5, 9),
                new Tuple<int, int>(7, 3),
                new Tuple<int, int>(4, 8),
                new Tuple<int, int>(5, 6),
                new Tuple<int, int>(0, 2),
                new Tuple<int, int>(6, 1),
            };
        }
        
        [TestCase]
        public void TestQuickFind() 
        {
            var result = Connectivity.QuickFind(GetTestData());
            result.Print();
        }

        [TestCase]
        public void TestQuickUnion()
        {
            var result = Connectivity.QuickUnion(GetTestData());
            result.Print("QuickUnion: ");
        }

        [TestCase]
        public void TestWeightedQuickUnion()
        {
            var result = Connectivity.WeightedQuickUnion(GetTestData());
            result.Print("WeightedQuickUnion: ");
        }
    }
}
