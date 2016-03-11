using System;
using System.Collections.Generic;
using System.Linq;
using System.Collections;

namespace Andersc.AlgorithmInCs.Common
{
    public static class EnumerableExtension
    {
        public static void ForEach<T>(this IEnumerable<T> enumerable, Action<T> action)
        {
            foreach (T item in enumerable)
            {
                action(item);
            }
        }

        public static bool IsEmpty<T>(this IEnumerable<T> enumerable)
        {
            return (enumerable.IsNull() || (!enumerable.Any()));
        }

        public static bool IsNotEmpty<T>(this IEnumerable<T> enumerable)
        {
            return (enumerable.IsNotNull() && (enumerable.Any()));
        }

        public static bool Contains<T>(this IEnumerable enumerable, T value, Func<T, T, bool> areEqual)
        {
            foreach (T item in enumerable)
            {
                if (areEqual(item, value))
                {
                    return true;
                }
            }

            return false;
        }

        public static TValue GetValueOrDefault<TKey, TValue>(this IDictionary<TKey, TValue> dict, TKey key, TValue defaultValue)
        {
            TValue value;
            return dict.TryGetValue(key, out value) ? value : defaultValue;
        }

        public static TValue GetValueOrDefault<TKey, TValue>(this IDictionary<TKey, TValue> dict, 
            TKey key, Func<TValue> defaultValueProvider)
        {
            TValue value;
            return dict.TryGetValue(key, out value) ? value : defaultValueProvider();
        }

        public static IEnumerable<int> CumulativeSum(this IEnumerable<int> numbers)
        {
            var sum = 0;
            foreach (var number in numbers)
            {
                sum += number;
                yield return sum;
            }
        }

        public static IEnumerable<T> Accumulate<T>(this IEnumerable<T> elements, Func<T, T, T> func)
        {
            var sum = default(T);
            foreach (var element in elements)
            {
                sum = func(sum, element);
                yield return sum;
            }
        }

        // TODO: Impl.
        //public static bool IsAscOrdered<T>(this IEnumerable<T> enumerable) where T : IComparable<T>
        //{
        //    if (enumerable.IsNull()) { throw new ArgumentNullException("enumerable"); }

        //    // Avoid unnecessary counting.
        //    int count = 0;
        //    foreach (T item in enumerable)
        //    {
        //        count++;
        //        if (count >= 2)
        //        {
        //            break;
        //        }
        //    }

        //    if (count <= 1)
        //    {
        //        return true;
        //    }

        //    IEnumerator<T> enumerator = enumerable.GetEnumerator();
        //    T a, b;
        //    while (enumerator.MoveNext())
        //    {
        //        a = enumerator.Current;
        //        if (enumerator.MoveNext())
        //        {
        //            b = enumerator.Current;
        //        }
        //        else
        //        {
        //            return true;
        //        }
        //    }

        //    return true;
        //}

        //public static bool IsDescOrdered<T>(this T[] array) where T : IComparable<T>
        //{
        //    if (array.IsNull()) { throw new ArgumentNullException("array"); }

        //    if (array.Length <= 1)
        //    {
        //        return true;
        //    }

        //    for (int i = 1; i < array.Length; i++)
        //    {
        //        if (array[i - 1].CompareTo(array[i]) < 0)
        //        {
        //            return false;
        //        }
        //    }

        //    return true;
        //}
    }
}
