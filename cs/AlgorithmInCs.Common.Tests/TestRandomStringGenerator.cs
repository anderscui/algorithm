
using System.Collections.Generic;
using System.Linq;

using NUnit.Framework;

namespace Andersc.AlgorithmInCs.Common.Tests
{
    [TestFixture]
    public class TestRandomStringGenerator
    {
        [Test]
        public void TestAlphabeticalNext()
        {
            var gen = new RandomStringGenerator(2, false);
            Assert.That(gen.StringOfIndex(0), Is.EqualTo("A"));
            Assert.That(gen.StringOfIndex(1), Is.EqualTo("B"));
            Assert.That(gen.StringOfIndex(27), Is.EqualTo("BB"));
            Assert.That(gen.StringOfIndex(26), Is.EqualTo("BA"));
        }

        private static readonly string Letters = "abcdefghijklmnopqrstuvwxyz";
        private static string StringOfIndex(long id)
        {
            if (id < 0) { return string.Empty; }

            int CharsCount = Letters.Length;
            var nums = new List<char>();

            var n = id;
            do
            {
                nums.Add(Letters[(int) (n % CharsCount)]);
                n = n / CharsCount;
            } while (n > 0);

            nums.Reverse();
            return string.Join(string.Empty, nums);
        }

        [Test]
        public void TestStringOfIndex()
        {
            Assert.That(StringOfIndex(0), Is.EqualTo("a"));
            Assert.That(StringOfIndex(1), Is.EqualTo("b"));
            Assert.That(StringOfIndex(25), Is.EqualTo("z"));
            Assert.That(StringOfIndex(26), Is.EqualTo("ba"));
            Assert.That(StringOfIndex(27), Is.EqualTo("bb"));
            Assert.That(StringOfIndex(27), Is.EqualTo("bb"));
        }
    }
}
