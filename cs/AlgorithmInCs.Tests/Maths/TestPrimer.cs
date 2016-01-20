using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Andersc.AlgorithmInCs.Algorithms.Maths;
using NUnit.Framework;

namespace Andersc.AlgorithmInCs.Tests.Maths
{
    [TestFixture]
    public class TestPrimer
    {
        [Test]
        public void TestGetPrimeFactorsWithFactorsLessThan()
        {
            var n = 2;
            var factors = Primer.GetPrimeFactors(n);
            Assert.That(factors.Count, Is.EqualTo(1));
            Assert.That(factors[0], Is.EqualTo(2));

            n = 6;
            factors = Primer.GetPrimeFactors(n);
            Assert.That(factors.Count, Is.EqualTo(2));
            Assert.That(factors[0], Is.EqualTo(2));
            Assert.That(factors[1], Is.EqualTo(3));

            n = 1003;
            factors = Primer.GetPrimeFactors(n);
            Assert.That(factors.Count, Is.EqualTo(2));
            CollectionAssert.AreEqual(new[] {17, 59}, factors);

            n = 5603114;
            factors = Primer.GetPrimeFactors(n);
            Assert.That(factors.Count, Is.EqualTo(4));
            CollectionAssert.AreEqual(new[] { 2, 11, 257, 991 }, factors);

            n = 10101128;
            factors = Primer.GetPrimeFactors(n);
            Assert.That(factors.Count, Is.EqualTo(7));
            CollectionAssert.AreEqual(new[] { 2, 2, 2, 17, 17, 17, 257 }, factors);
        }

        [Test]
        public void TestGetPrimeFactorsWithLargeFactors()
        {
            var n = 6114;
            var factors = Primer.GetPrimeFactors(n);
            Assert.That(factors.Count, Is.EqualTo(3));
            CollectionAssert.AreEqual(new[] { 2, 3, 1019 }, factors);

            n = 1326559543;
            factors = Primer.GetPrimeFactors(n);
            Assert.That(factors.Count, Is.EqualTo(3));
            CollectionAssert.AreEqual(new[] { 1009, 1009, 1303 }, factors);
        }

        [Test]
        public void TestGetPrimeFactors2WithLargeFactors()
        {
            var n = 6114;
            var factors = Primer.GetPrimeFactors2(n);
            Assert.That(factors.Count, Is.EqualTo(3));
            CollectionAssert.AreEqual(new[] { 2, 3, 1019 }, factors);

            n = 1326559543;
            factors = Primer.GetPrimeFactors2(n);
            Assert.That(factors.Count, Is.EqualTo(3));
            CollectionAssert.AreEqual(new[] { 1009, 1009, 1303 }, factors);
        }

        [Test]
        public void TestGetPrimeFactors3WithLargeFactors()
        {
            var n = 6114;
            var factors = Primer.GetPrimeFactors3(n);
            Assert.That(factors.Count, Is.EqualTo(3));
            CollectionAssert.AreEqual(new[] { 2, 3, 1019 }, factors);

            n = 1326559543;
            factors = Primer.GetPrimeFactors3(n);
            Assert.That(factors.Count, Is.EqualTo(3));
            CollectionAssert.AreEqual(new[] { 1009, 1009, 1303 }, factors);
        }

        [Test]
        public void TestGetPrimesBelow()
        {
            var n = 20;
            var factors = Primer.GetPrimesBelow(n);
            Assert.That(factors.Count, Is.EqualTo(8));
            CollectionAssert.AreEqual(new[] { 2, 3, 5, 7, 11, 13, 17, 19 }, factors);

            n = 2000;
            factors = Primer.GetPrimesBelow(n);
            foreach (var factor in factors)
            {
                Console.Write("{0} ", factor);
            }
        }
    }
}
