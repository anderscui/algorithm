using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using Andersc.AlgorithmInCs.Algorithms.Problems;
using NUnit.Framework;

namespace Andersc.AlgorithmInCs.Tests.Problems
{
    [TestFixture]
    public class TestGroupedDigitsGenerator
    {
        [TestCase]
        public void TestNextIndexFor2Groups()
        {
            var next = new GroupedDigitsGenerator(2, 30).NextGroupIndex();
            Assert.That(next, Is.EqualTo(0));

            next = new GroupedDigitsGenerator(2, 80).NextGroupIndex();
            Assert.That(next, Is.EqualTo(1));

            next = new GroupedDigitsGenerator(2, 50).NextGroupIndex();
            Assert.That(next, Is.EqualTo(0));

            next = new GroupedDigitsGenerator(2, 51).NextGroupIndex();
            Assert.That(next, Is.EqualTo(1));
        }

        [TestCase]
        public void TestNextGroupIndexByProportions()
        {
            var next = new GroupedDigitsGenerator(new[] { 1, 2 }, 0).NextGroupIndex();
            Assert.That(next, Is.EqualTo(0));

            next = new GroupedDigitsGenerator(new[] { 1, 2 }, 33).NextGroupIndex();
            Assert.That(next, Is.EqualTo(1));

            next = new GroupedDigitsGenerator(new[] { 1, 2 }, 34).NextGroupIndex();
            Assert.That(next, Is.EqualTo(1));

            next = new GroupedDigitsGenerator(new[] { 1, 2 }, 99).NextGroupIndex();
            Assert.That(next, Is.EqualTo(1));

            next = new GroupedDigitsGenerator(new[] { 1, 2 }, 100).NextGroupIndex();
            Assert.That(next, Is.EqualTo(0));
        }

        [TestCase]
        public void TestNextGroupIndexByMoreProportions()
        {
            var seeds = new[] {0, 1500, 103048, 10049, 165, 366, 382, 50083, 1919199};
            var expected = new[] {0, 0, 0, 1, 1, 2, 2, 3, 3};

            var nexts = from seed in seeds
                        select new GroupedDigitsGenerator(new[] { 49, 17, 17, 17 }, seed).NextGroupIndex();
            CollectionAssert.AreEqual(expected, nexts);
        }
    }
}
