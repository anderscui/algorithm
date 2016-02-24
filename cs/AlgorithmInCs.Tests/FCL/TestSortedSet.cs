using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using NUnit.Framework;

namespace Andersc.AlgorithmInCs.Tests.FCL
{
    [TestFixture]
    public class TestSortedSet
    {
        class Person
        {
            public string Name { get; set; }
            public int Age { get; set; }
        }

        class SortPersonByAge : IComparer<Person>
        {
            public int Compare(Person x, Person y)
            {
                return x.Age.CompareTo(y.Age);
            }
        }

        [Test]
        public void TestBasics()
        {
            var set = new SortedSet<Person>(new SortPersonByAge())
            {
                new Person() {Name = "Anders", Age = 30},
                new Person() {Name = "Madfrog", Age = 33},
                new Person() {Name = "Focus", Age = 27},
            };

            foreach (var person in set)
            {
                Console.WriteLine(person.Name);
            }
        }
    }
}
