using System;
using System.Text.RegularExpressions;

namespace Andersc.AlgorithmInCs.Common
{
    public static class StringExtension
    {
        public static bool IsNullOrEmpty(this string s)
        {
            return string.IsNullOrEmpty(s);
        }

        public static bool IsBlank(this string s)
        {
            return (s.IsNullOrEmpty() || s.Trim().Length == 0);
        }

        public static bool IsNotNullOrEmpty(this string s)
        {
            return !string.IsNullOrEmpty(s);
        }

        public static bool IsNotBlank(this string s)
        {
            return !s.IsBlank();
        }

        public static bool IsMatch(this string s, string pattern)
        {
            if (s == null) { return false; }

            return Regex.IsMatch(s, pattern);
        }

        public static string Match(this string s, string pattern)
        {
            if (s == null) return "";

            return Regex.Match(s, pattern).Value;
        }

        public static bool IsInt32(this string s)
        {
            int i;
            return int.TryParse(s, out i);
        }

        public static bool Contains(this string s, string toCheck, StringComparison comp)
        {
            return s.IndexOf(toCheck, comp) >= 0;
        }

        public static string FormatWith(this string format, params object[] args)
        {
            return string.Format(format, args);
        }

        public static int ToInt32(this string s)
        {
            return int.Parse(s);
        }

        public static string ToCamel(this string s)
        {
            if (s.IsNullOrEmpty()) return s;

            return s[0].ToString().ToLower() + s.Substring(1);
        }

        public static string ToPascal(this string s)
        {
            if (s.IsNullOrEmpty()) return s;

            return s[0].ToString().ToUpper() + s.Substring(1);
        }

        public static bool IsPalindromic(this string str)
        {
            if (str.IsNull()) { throw new ArgumentNullException("str"); }

            if (str.Length <= 1) { return true; }

            char[] chars = str.ToCharArray();
            return IsPalindromic(chars, 0, chars.Length - 1);
        }

        private static bool IsPalindromic(char[] chars, int start, int end)
        {
            if (start >= end)
            {
                return true;
            }

            return (chars[start] == chars[end]) && IsPalindromic(chars, start + 1, end - 1);
        }
    }
}
