using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using NUnit.Framework;

namespace Andersc.AlgorithmInCs.Tests.FCL
{
    [TestFixture]
    public class TestNullable
    {
        [TestCase]
        public void TestAddToInt()
        {
            int? i = null;
            Assert.That(i+1, Is.Null);
        }
    }
}
