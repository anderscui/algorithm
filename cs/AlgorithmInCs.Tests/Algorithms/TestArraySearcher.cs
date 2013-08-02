using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using NUnit.Framework;

using Andersc.AlgorithmInCs.Algorithms;
using Andersc.AlgorithmInCs.Common;
using Andersc.AlgorithmInCs.Common.Extensions;

namespace Andersc.AlgorithmInCs.Tests.Algorithms
{
    [TestFixture]
    public class TestArraySearcher
    {
        private int[] GetTestData()
        {
            return new [] { 9, 19, 14, 5, 17, 10, 1, 15, 4, 7 };
        }
        
        [TestCase]
        public void TestQuickFind()
        {
            var data = GetTestData();
            var index = ArraySearcher.Sequential(data, 10, 0, data.Length - 1);
            Assert.That(index, Is.EqualTo(5));

            index = ArraySearcher.Sequential(data, 12, 0, data.Length - 1);
            Assert.That(index, Is.LessThan(0));
        }
    }
}
