using System;
using System.Security.Cryptography;
using System.Text;
using NUnit.Framework;

using Andersc.AlgorithmInCs.Algorithms.Problems;

namespace Andersc.AlgorithmInCs.Tests.Problems
{
    [TestFixture]
    public class TestExpressionEvaluator
    {
        [Test]
        public void TestReadNumbers()
        {
            var ee = new ExpressionEvaluator();
            
            var s = "3+12*5";
            var start = 0;
            var res = ee.ReadNumber(s, start);
            Assert.That(res.Item1, Is.EqualTo(3));
            Assert.That(res.Item2, Is.EqualTo(1));

            start = 2;
            res = ee.ReadNumber(s, start);
            Assert.That(res.Item1, Is.EqualTo(12));
            Assert.That(res.Item2, Is.EqualTo(4));

            start = 1;
            res = ee.ReadNumber(s, start);
            Assert.That(res.Item1, Is.EqualTo(0));
            Assert.That(res.Item2, Is.EqualTo(1));

            start = 5;
            res = ee.ReadNumber(s, start);
            Assert.That(res.Item1, Is.EqualTo(5));
            Assert.That(res.Item2, Is.EqualTo(6));

            s = "2 * 3.14 * 3 + 2";
            start = 4;
            res = ee.ReadNumber(s, start);
            Assert.That(res.Item1, Is.EqualTo(3.14));
            Assert.That(res.Item2, Is.EqualTo(8));
        }

        [Test]
        public void TestEvaluate()
        {
            var ee = new ExpressionEvaluator();
            Console.WriteLine(ee.Evaluate("1"));
            Console.WriteLine(ee.Evaluate("1+2\0"));
            Console.WriteLine(ee.Evaluate("1+2*3"));
            Console.WriteLine(ee.Evaluate("(1+2)*3"));
            Console.WriteLine(ee.Evaluate("(1+2)*3 "));
        }

        [Test]
        public void TestRemoveSpace()
        {
            var ee = new ExpressionEvaluator();
            Assert.That(ee.RemoveSpace("(1+2)*3"), Is.EqualTo("(1+2)*3"));
            Assert.That(ee.RemoveSpace("(1+2)*3 "), Is.EqualTo("(1+2)*3"));
            Assert.That(ee.RemoveSpace("(1+2)*3 + 5"), Is.EqualTo("(1+2)*3+5"));
        }

        [Test]
        public void TestRpnConversion()
        {
            var ee = new ExpressionEvaluator();
            
            var rpn = new StringBuilder();
            ee.Evaluate("1", rpn);
            Console.WriteLine(rpn);

            rpn = new StringBuilder();
            ee.Evaluate("1+2*3", rpn);
            Console.WriteLine(rpn);

            rpn = new StringBuilder();
            ee.Evaluate("2+2*(3+2) + 9/ 3 ", rpn);
            Console.WriteLine(rpn);
        }

        [Test]
        public void TestRpnEval()
        {
            var ee = new ExpressionEvaluator();

            var rpn = "1";
            Assert.That(ee.EvaluateRpn(rpn), Is.EqualTo(1));

            rpn = "1 2 3 * +";
            Assert.That(ee.EvaluateRpn(rpn), Is.EqualTo(7));

            rpn = "2 2 3 2 + * + 9 3 / + ";
            Assert.That(ee.EvaluateRpn(rpn), Is.EqualTo(15));

            // this test case comes from: http://en.wikipedia.org/wiki/Reverse_Polish_notation
            rpn = "5 1 2 + 4 * + 3 -";
            Assert.That(ee.EvaluateRpn(rpn), Is.EqualTo(14));
        }
    }
}