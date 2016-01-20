using Andersc.AlgorithmInCs.Algorithms.Problems;
using NUnit.Framework;

namespace Andersc.AlgorithmInCs.Tests.Maths
{
    [TestFixture]
    public class TestPrimeFactors
    {
        [Test]
        public void TestGenerateWithUniqueFactors()
        {
            var n = 2;
            var factors = PrimeFactors.Generate(n);
            Assert.That(factors.Count, Is.EqualTo(1));
            CollectionAssert.AreEqual(new[] { 2 }, factors);

            n = 6;
            factors = PrimeFactors.Generate(n);
            Assert.That(factors.Count, Is.EqualTo(2));
            CollectionAssert.AreEqual(new[] { 2, 3 }, factors);

            n = 1003;
            factors = PrimeFactors.Generate(n);
            Assert.That(factors.Count, Is.EqualTo(2));
            CollectionAssert.AreEqual(new[] {17, 59}, factors);
        }

        [Test]
        public void TestGenerateWithDuplicateFactors()
        {
            var n = 10101128;
            var factors = PrimeFactors.Generate(n);
            Assert.That(factors.Count, Is.EqualTo(7));
            CollectionAssert.AreEqual(new[] { 2, 2, 2, 17, 17, 17, 257 }, factors);

            n = 1326559543;
            factors = PrimeFactors.Generate(n);
            Assert.That(factors.Count, Is.EqualTo(3));
            CollectionAssert.AreEqual(new[] { 1009, 1009, 1303 }, factors);
        }

        [Test]
        public void TestGenerateWithoutAnyFactors()
        {
            var n = 0;
            var factors = PrimeFactors.Generate(n);
            CollectionAssert.IsEmpty(factors);

            n = 1;
            factors = PrimeFactors.Generate(n);
            CollectionAssert.IsEmpty(factors);

            n = -1;
            factors = PrimeFactors.Generate(n);
            CollectionAssert.IsEmpty(factors);

            n = 10;
            factors = PrimeFactors.Generate(n);
            CollectionAssert.IsNotEmpty(factors);
        }

        [Test]
        public void TestGenerateForNegativeNumbers()
        {
            CollectionAssert.AreEqual(PrimeFactors.Generate(-2), PrimeFactors.Generate(2));
            CollectionAssert.AreEqual(PrimeFactors.Generate(-1003), PrimeFactors.Generate(1003));
            CollectionAssert.AreEqual(PrimeFactors.Generate(-10101128), PrimeFactors.Generate(10101128));
        }
    }
}
