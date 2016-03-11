using System.Linq;

using NUnit.Framework;

namespace Andersc.AlgorithmInCs.Common.Tests
{
    [TestFixture]
    public class TestEnumerableExtension
    {
        [Test]
        public void TestCumulativeSum()
        {
            var arr = new[] { 1, 2, 3, 4, 5 };
            var sums = arr.CumulativeSum().ToList();

            Assert.That(sums.Count, Is.EqualTo(arr.Length));
            CollectionAssert.AreEqual(new[] { 1, 3, 6, 10, 15 }, sums);
        }

        [Test]
        public void TestAccumulate()
        {
            var arr = new[] { 1, 2, 3, 4, 5 };
            var sums = arr.Accumulate((x, y) => x + y).ToList();

            Assert.That(sums.Count, Is.EqualTo(arr.Length));
            CollectionAssert.AreEqual(new[] { 1, 3, 6, 10, 15 }, sums);
        }
    }
}
