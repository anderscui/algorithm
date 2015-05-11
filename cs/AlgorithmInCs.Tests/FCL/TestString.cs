using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using NUnit.Framework;

namespace Andersc.AlgorithmInCs.Tests.FCL
{
    [TestFixture]
    public class TestString
    {
        [Test]
        public void TestStringBuilderAppendChar()
        {
            var sb = new StringBuilder("hello");
            Console.WriteLine(sb);
            sb.Append('\0');
            Console.WriteLine(sb);
            Console.WriteLine('\0'.ToString());

            var s = "hello0";
            s = s + "\0";
            Console.WriteLine(s.Length);
            Console.WriteLine((int)s[5]);
            Console.WriteLine((int)s[6]);
        }

        [Test]
        public void TestSplitWithSpace()
        {
            var s = "a b c";
            Assert.That(s.Split(' ').Length, Is.EqualTo(3));

            s = "a b c d ";
            var parts = s.Split(' ');
            Assert.That(parts.Length, Is.EqualTo(5));
            Assert.That(parts[3], Is.EqualTo("d"));
            Assert.That(parts[4], Is.EqualTo(""));

            s = "a b c  d ";
            parts = s.Split(' ');
            Assert.That(parts.Length, Is.EqualTo(6));
            Assert.That(parts[3], Is.EqualTo(""));
            Assert.That(parts[4], Is.EqualTo("d"));
            Assert.That(parts[5], Is.EqualTo(""));

            s = "a b  c ";
            parts = s.Split(' ').Where(p => !string.IsNullOrWhiteSpace(p)).ToArray();
            Assert.That(parts.Length, Is.EqualTo(3));
            Assert.That(parts[0], Is.EqualTo("a"));
            Assert.That(parts[1], Is.EqualTo("b"));
            Assert.That(parts[2], Is.EqualTo("c"));
        }
    }
}
