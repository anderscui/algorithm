using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using NUnit.Framework;

namespace Andersc.AlgorithmInCs.Tests.FCL
{
    [TestFixture]
    public class TestLinqToObjects
    {
        [TestCase]
        [ExpectedException(typeof(ArgumentNullException))]
        public void TestAnyForEmptyCollectionException()
        {
            int[] arr = null;
            Assert.That(arr.Any(), Is.False);
        }

        [TestCase]
        public void TestAnyMethodForEmptyCollection()
        {
            var arr = new int[0];
            Assert.That(arr.Any(), Is.False);
        }

        [Test]
        public void TestAggregate()
        {
            var arr = new[] {1, 2, 3, 4, 5};
            Console.WriteLine(arr.Aggregate(0, (x, y) => x + y));
        }
    }
}
