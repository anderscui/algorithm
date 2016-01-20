using System.Linq;

using NUnit.Framework;

namespace Andersc.AlgorithmInCs.Common.Tests
{
    [TestFixture]
    public class TestQueue
    {
        [Test]
        public void TestAlphabeticalNext()
        {
            Assert.That(Seq.NextInAlphabet(""), Is.EqualTo("a"));
            Assert.That(Seq.NextInAlphabet("a"), Is.EqualTo("b"));
            Assert.That(Seq.NextInAlphabet("z"), Is.EqualTo("aa"));
        }

        [Test]
        public void TestIndexOfString()
        {
            Assert.That(Seq.IndexOfString(""), Is.EqualTo(0));
            Assert.That(Seq.IndexOfString("a"), Is.EqualTo(0));
            Assert.That(Seq.IndexOfString("z"), Is.EqualTo(25));
        }
    }
}
