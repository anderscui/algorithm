using System;
using System.Collections.Generic;

namespace Andersc.AlgorithmInCs.Common.Extensions
{
    public static class ArrayExtension
    {
        private static readonly int NotFound = -1;

        public static bool HasElements(this Array array)
        {
            return (array != null && array.Length != 0);
        }

        public static void Swap<T>(this T[] array, int index1, int index2)
        {
            if (index1 == index2) { return; }

            var temp = array[index1];
            array[index1] = array[index2];
            array[index2] = temp;
        }

        public static int IndexOf<T>(this T[] array, T value)
        {
            if (array.IsNull()) { throw new ArgumentNullException("array"); }

            EqualityComparer<T> comparer = EqualityComparer<T>.Default;
            for (int i = 0; i < array.Length; i++)
            {
                if (comparer.Equals(array[i], value))
                {
                    return i;
                }
            }

            return NotFound;
        }

        public static bool Contains<T>(this T[] array, T value) where T : IComparable<T>
        {
            return (IndexOf(array, value) >= 0);
        }

        public static int BinarySearch<T>(this T[] array, T key) where T : IComparable<T>
        {
            if (!HasElements(array)) { return -1; }

            return BinarySearch(array, key, 0, array.Length - 1);
        }

        private static int BinarySearch<T>(this T[] array, T key, int lowerBound, int upperBound)
            where T : IComparable<T>
        {
            int currentIndex = (lowerBound + upperBound) / 2;

            if (array[currentIndex].CompareTo(key) == 0)
            {
                return currentIndex;
            }

            if (lowerBound > upperBound)
            {
                return NotFound;
            }

            if (array[currentIndex].CompareTo(key) < 0)
            {
                return BinarySearch(array, key, currentIndex + 1, upperBound);
            }
            else
            {
                return BinarySearch(array, key, lowerBound, currentIndex - 1);
            }
        }

        public static void Resize<T>(this T[] array, int newSize)
        {
            Array.Resize(ref array, newSize);
        }

        public static void Init<T>(this T[] array, T initValue)
        {
            if (array.IsNull()) { return; }

            for (int i = 0; i < array.Length; i++)
            {
                array[i] = initValue;
            }
        }

        public static bool IsAscOrdered<T>(this T[] array) where T : IComparable<T>
        {
            if (array.IsNull()) { throw new ArgumentNullException("array"); }

            if (array.Length <= 1)
            {
                return true;
            }

            for (int i = 1; i < array.Length; i++)
            {
                if (array[i - 1].CompareTo(array[i]) > 0)
                {
                    return false;
                }
            }

            return true;
        }

        public static bool IsDescOrdered<T>(this T[] array) where T : IComparable<T>
        {
            if (array.IsNull()) { throw new ArgumentNullException("array"); }

            if (array.Length <= 1)
            {
                return true;
            }

            for (int i = 1; i < array.Length; i++)
            {
                if (array[i - 1].CompareTo(array[i]) < 0)
                {
                    return false;
                }
            }

            return true;
        }

        public static void ForEach<T>(this T[] array, Action<T> action)
        {
            Array.ForEach(array, action);
        }

        public static void Clear(Array array, int startIndex, int length)
        {
            Array.Clear(array, startIndex, length);
        }

        // TODO: refactor this, use a delegate like Action<T>?
        public static void Print<T>(this T[] array, string title = "Elements: ", string separator = "  ")
        {
            Console.WriteLine("************");

            Console.WriteLine(title);
            foreach (T elem in array)
            {
                Console.Write("{0}{1}", elem, separator);
            }

            Console.WriteLine();
            Console.WriteLine("************");
            Console.WriteLine();
        }
    }
}
