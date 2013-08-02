using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Andersc.AlgorithmInCs.Common
{
    public static class ObjectExtension
    {
        public static bool IsNull(this object obj)
        {
            return obj == null;
        }

        public static bool IsNotNull(this object obj)
        {
            return obj != null;
        }

        public static bool In<T>(this T t, IEnumerable<T> c)
        {
            return c.Any(i => i.Equals(t));
        }

        public static bool InRange<T>(this IComparable<T> t, T min, T max)
        {
            return t.CompareTo(min) >= 0
                   && t.CompareTo(max) <= 0;
        }

        public static bool DoesNotHaveValue<T>(this T? nullable) where T : struct
        {
            return !nullable.HasValue;
        }
    }
}
