using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Collections.Specialized;
using System.Linq;
using System.Text;

using NUnit.Framework;

namespace Andersc.AlgorithmInCs.Tests.FCL
{
    [TestFixture]
    public class TestObservableCollection
    {
        class Person
        {
            public string Name { get; set; }
            public int Age { get; set; }
        }

        [Test]
        public void TestBasics()
        {
            var people = new ObservableCollection<Person>()
            {
                new Person() {Name = "Anders", Age = 30},
                new Person() {Name = "Madfrog", Age = 33},
            };

            people.CollectionChanged += PeopleOnCollectionChanged;

            //
            people.Add(new Person() { Name = "Moon", Age = 31});

            //
            people.RemoveAt(2);
        }

        private void PeopleOnCollectionChanged(object sender, NotifyCollectionChangedEventArgs args)
        {
            Console.WriteLine("Action: " + args.Action);

            if (args.Action == NotifyCollectionChangedAction.Remove)
            {
                Console.WriteLine("Removed items: ");
                foreach (Person item in args.OldItems)
                {
                    Console.WriteLine(item.Name);
                }
            }

            if (args.Action == NotifyCollectionChangedAction.Add)
            {
                Console.WriteLine("Added items");
                foreach (Person item in args.NewItems)
                {
                    Console.WriteLine(item.Name);
                }
            }
        }
    }
}
