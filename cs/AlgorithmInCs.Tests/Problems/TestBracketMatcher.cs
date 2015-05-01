using System;
using System.Collections.Generic;
using Andersc.AlgorithmInCs.Algorithms.Problems;
using NUnit.Framework;

namespace Andersc.AlgorithmInCs.Tests.Problems
{
    [TestFixture]
    public class TestBracketMatcher
    {
        [TestCase]
        public void TestNormalSymbol()
        {
            var matcher = new BracketMatcher();

            var expr = "1 + (a + b) * (3 + c)";
            Assert.That(matcher.Solve(expr), Is.True);

            expr = "{1 + [a + (a + (b))] * (3 + c)}";
            Assert.That(matcher.Solve(expr), Is.True);

            expr = "{1 + [a + (a + b]] * (3 + c)}";
            Assert.That(matcher.Solve(expr), Is.False);
        }

        [TestCase]
        public void TestEmptySymbol()
        {
            var matcher = new BracketMatcher();

            var expr = "1 + 2 * 3";
            Assert.That(matcher.Solve(expr), Is.True);
        }
    }
}
