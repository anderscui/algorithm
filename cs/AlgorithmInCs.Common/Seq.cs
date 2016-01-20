using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Andersc.AlgorithmInCs.Common
{
    public class Seq
    {
        private static readonly string Letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        private static readonly string DigitAndLetters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";

        public static long IndexOfString(string str)
        {
            if (str.IsNullOrEmpty())
            {
                return 0;
            }

            long sum = str[0] - Letters[0];
            for (var i = 0; i < str.Length - 1; i++)
            {
                sum = sum * 26 + (str[i + 1] - Letters[0]);
            }

            return sum;
        }

        public static string NextInAlphabet(string input)
        {
            if (input.IsNullOrEmpty())
            {
                return "a";
            }
            return input;
        }

        public static string NextByOrdinality(string input)
        {
            return input;
        }
    }
}
