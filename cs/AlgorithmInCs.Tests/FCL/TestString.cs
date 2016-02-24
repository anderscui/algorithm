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

        [Test]
        public void TestCharOrdinality()
        {
            var c = "ab"[0];
            Console.WriteLine((int)c);
            Console.WriteLine('c');
        }

        [Test]
        public void TestHex()
        {
            var s = "74 68 65"; // the
            //s = "68 61 70 70 69 65 73 74 74 68 69 6E 67"; // happiest.thing
            s = "65 76 65 72 69 73 2 6D 65 65 74"; // ever.is.2.meet
            s = "61 70 65 72 66 65 63 74 6D 61 74 63 68"; // a.perfect.match
            s = "6C 69 6B 65 75"; // like.u
            s = "6E 6D 69 6C 6C 69 6F 6E 73 6F 66 70 65 6F 70 6C 65"; // n.millions.of.people
            s = "65 69 74 68 65 72 65 61 72 6C 69 65 72 6E 6F 72"; // either.earlier.nor
            s = "61 62 69 74 6C 61 74 65"; // a.bit.late
            var parts = s.Split(' ');
            foreach (var c in parts)
            {
                var val = Convert.ToInt32(c, 16);
                var cval = char.ConvertFromUtf32(val);
                Console.Write(cval);
            }
            Console.WriteLine();

            //var parts = s.Split(' ').Select(p => char.Parse("\\x" + p)).ToArray();
            //Console.WriteLine(new string(parts));
        }
    }
}
