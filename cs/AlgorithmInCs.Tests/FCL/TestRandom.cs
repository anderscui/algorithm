using System;
using System.Collections.Generic;
using System.Linq;
using NUnit.Framework;

namespace Andersc.AlgorithmInCs.Tests.FCL
{
    [TestFixture]
    public class TestRandom
    {
        [TestCase]
        public void TestRandomRange()
        {
            var r = new Random();
            var min = 1;
            var max = 3;
            var numbers = new List<int>();
            for (int i = 0; i < 100; i++)
            {
                numbers.Add(r.Next(min, max));
            }

            Assert.That(numbers.All(n => n < max));
            Assert.That(numbers.All(n => n >= min));
            Console.WriteLine(numbers.Count(n => n == 1));
        }
    }
}
