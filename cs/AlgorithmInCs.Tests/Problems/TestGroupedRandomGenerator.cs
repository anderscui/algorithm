using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using Andersc.AlgorithmInCs.Algorithms.Problems;
using NUnit.Framework;

namespace Andersc.AlgorithmInCs.Tests.Problems
{
    [TestFixture]
    public class TestGroupedRandomGenerator
    {
        [TestCase]
        public void TestNextIndexFor2Groups()
        {
            var numbers = new List<int>();
            for (var i = 0; i < 100; i++)
            {
                var next = new GroupedRandomGenerator(2).NextGroupIndex();
                numbers.Add(next);
                Thread.Sleep(37);
            }

            foreach (var g in numbers.GroupBy(n => n, n => 1))
            {
                Console.WriteLine("{0}: {1}", g.Key, g.Count());
            }
        }

        [TestCase]
        public void TestNextIndex()
        {
            var numbers = new List<int>();
            for (var i = 0; i < 100; i++)
            {
                var next = new GroupedRandomGenerator(3).NextGroupIndex();
                numbers.Add(next);
                //Console.WriteLine(next);

                Thread.Sleep(37);
            }

            foreach (var g in numbers.GroupBy(n => n, n => 1))
            {
                Console.WriteLine("{0}: {1}", g.Key, g.Count());
            }
        }

        [TestCase]
        public void TestNextGroupIndexByProportions()
        {
            var numbers = new List<int>();
            for (var i = 0; i < 100; i++)
            {
                var next = new GroupedRandomGenerator(new[] { 33, 33, 33 }).NextGroupIndex();
                numbers.Add(next);
                //Console.WriteLine(next);

                Thread.Sleep(37);
            }

            foreach (var g in numbers.GroupBy(n => n, n => 1))
            {
                Console.WriteLine("{0}: {1}", g.Key, g.Count());
            }
        }

        [TestCase]
        public void TestNextGroupIndexByMoreProportions()
        {
            var numbers = new List<int>();
            for (var i = 0; i < 100; i++)
            {
                var next = new GroupedRandomGenerator(new[] { 49, 17, 17, 17 }).NextGroupIndex();
                numbers.Add(next);
                //Console.WriteLine(next);

                Thread.Sleep(37);
            }

            foreach (var g in numbers.GroupBy(n => n, n => 1))
            {
                Console.WriteLine("{0}: {1}", g.Key, g.Count());
            }
        }
    }
}
