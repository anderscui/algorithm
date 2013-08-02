using System;

using NUnit.Framework;

using Andersc.AlgorithmInCs.Algorithms;

namespace Andersc.AlgorithmInCs.Tests.Algorithms
{
    [TestFixture]
    public class TestEvaluator
    {
        [Test]
        public void TestSamePrecedence()
        {
            string expression = "1+2+3";
            Evaluator eva = new Evaluator(expression);
            long result = eva.Evaluate();
            Assert.That(result, Is.EqualTo(6));

            expression = "1+2*3";
            eva = new Evaluator(expression);
            result = eva.Evaluate();
            Assert.That(result, Is.EqualTo(7));

            expression = "1+2*3-2^4";
            eva = new Evaluator(expression);
            result = eva.Evaluate();
            Assert.That(result, Is.EqualTo(-9));

            expression = "1+(2*3-2)^4";
            eva = new Evaluator(expression);
            result = eva.Evaluate();
            Assert.That(result, Is.EqualTo(257));
        }

        [Test]
        public void TestParenthesis()
        {
            string expression = "1+(2*3-2)^4";
            Evaluator eva = new Evaluator(expression);
            long result = eva.Evaluate();
            Assert.That(result, Is.EqualTo(257));

            expression = "1+(2*3-2^4)";
            eva = new Evaluator(expression);
            result = eva.Evaluate();
            Assert.That(result, Is.EqualTo(-9));
        }
    }
}
