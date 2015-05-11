using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Andersc.AlgorithmInCs.Algorithms.Problems
{
    /// <summary>
    /// +, -, *, /, ^, !, (, ), EOL
    /// </summary>
    public enum Operator
    {
        ADD, SUB, MUL, DIV, POW, FAC, L_P, R_P, EOE
    }

    public class ExpressionEvaluator
    {
        private static readonly int N_OPTR = 9;

        private char[][] pri = 
        {
           /*              |-------------------- 当 前 运 算 符 --------------------| */
           /*                      +      -      *      /      ^      !      (      )     \0 */
           /* --  + */   new [] { '>',   '>',   '<',   '<',   '<',   '<',   '<',   '>',   '>'},
           /* |   - */   new [] { '>',   '>',   '<',   '<',   '<',   '<',   '<',   '>',   '>'},
           /* 栈  * */   new [] { '>',   '>',   '>',   '>',   '<',   '<',   '<',   '>',   '>'},
           /* 顶  / */   new [] { '>',   '>',   '>',   '>',   '<',   '<',   '<',   '>',   '>'},
           /* 运  ^ */   new [] { '>',   '>',   '>',   '>',   '>',   '<',   '<',   '>',   '>'},
           /* 算  ! */   new [] { '>',   '>',   '>',   '>',   '>',   '>',   ' ',   '>',   '>'},
           /* 符  ( */   new [] { '<',   '<',   '<',   '<',   '<',   '<',   '<',   '=',   ' '},
           /* |   ) */   new [] { ' ',   ' ',   ' ',   ' ',   ' ',   ' ',   ' ',   ' ',   ' '}, // ')' will never appears in the stack.
           /* -- \0 */   new [] { '<',   '<',   '<',   '<',   '<',   '<',   '<',   ' ',   '='}
        };

        private double Calculate(double a, char op, double b)
        {
            switch (op)
            {
                case '+': return a + b;
                case '-': return a - b;
                case '*': return a * b;
                case '/': return a / b;
                case '^': return Math.Pow(a, b);
                default: throw new ArgumentException("Invalid argument value", "op");
            }
        }

        private double Calculate(char op, double b)
        {
            switch (op)
            {
                case '!': return Maths.Factorial((int)b);
                default: throw new ArgumentException("Invalid argument value", "op");
            }
        }

        // TODO: string end checking.
        public Tuple<double, int> ReadNumber(string s, int start)
        {
            var i = start;
            double res = 0;
            if (char.IsDigit(s, i))
            {
                while (i < s.Length && char.IsDigit(s, i))
                {
                    res = res * 10 + char.GetNumericValue(s[i++]);
                }
                // if has fraction part
                if (i < s.Length && '.' == s[i])
                {
                    i++;
                    double fraction = 1;
                    while (i < s.Length && char.IsDigit(s[i]))
                    {
                        fraction /= 10;
                        res += char.GetNumericValue(s[i++]) * fraction;
                    }
                }
            }
            return new Tuple<double, int>(res, i);
        }

        private Operator Optr2rank(char op)
        {
            switch (op)
            {
                case '+': return Operator.ADD; //加
                case '-': return Operator.SUB; //减
                case '*': return Operator.MUL; //乘
                case '/': return Operator.DIV; //除
                case '^': return Operator.POW; //乘方
                case '!': return Operator.FAC; //阶乘
                case '(': return Operator.L_P; //左括号
                case ')': return Operator.R_P; //右括号
                case '\0': return Operator.EOE; //起始符与终止符
                default: throw new ArgumentException("Invalid operater.", "op"); //未知运算符
            }
        }

        private char OrderBetween(char op1, char op2)
        {
            return pri[(int)Optr2rank(op1)][(int)Optr2rank(op2)];
        }

        public string RemoveSpace(string s)
        {
            return new string(s.Where(c => !char.IsWhiteSpace(c)).ToArray());
        }

        public double EvaluateRpn(StringBuilder expr, char separator = ' ')
        {
            return EvaluateRpn(expr.ToString(), separator);
        }

        public double EvaluateRpn(string expr, char separator = ' ')
        {
            var tokens = expr.Split(separator).Where(t => !string.IsNullOrWhiteSpace(t)).ToArray();

            var opnd = new Stack<double>();
            foreach (var token in tokens)
            {
                if (char.IsDigit(token[0]))
                {
                    opnd.Push(double.Parse(token));
                }
                else
                {
                    var op = token[0];
                    if (op == '!')
                    {
                        var popnd = opnd.Pop();
                        opnd.Push(Calculate(op, popnd));
                    }
                    else
                    {
                        var popnd2 = opnd.Pop();
                        var popnd1 = opnd.Pop();
                        opnd.Push(Calculate(popnd1, op, popnd2));
                    }
                }
            }
            if (opnd.Count != 1)
            {
                throw new Exception(string.Format("Invalid Expression: '{0}'", expr));
            }
            return opnd.Pop();
        }

        public double Evaluate(string s, StringBuilder rpn = null)
        {
            if (string.IsNullOrWhiteSpace(s))
            {
                throw new ArgumentOutOfRangeException("s", "s must not be null or whitespace.");
            }

            var opnd = new Stack<double>();
            var optr = new Stack<char>();
            //rpn = new StringBuilder();
            
            optr.Push('\0');
            s = RemoveSpace(s) + "\0";

            var extr = s;
            var cur = 0;
            while (optr.Count > 0)
            {
                if (char.IsDigit(s, cur))
                {
                    var num = ReadNumber(s, cur);
                    opnd.Push(num.Item1);
                    cur = num.Item2;

                    rpn.Append(opnd.Peek() + " ");
                }
                else
                {
                    switch (OrderBetween(optr.Peek(), s[cur]))
                    {
                        case '<':
                            optr.Push(s[cur]);
                            cur++;
                            break;
                        case '=': // ')' or EOE
                            optr.Pop();
                            cur++;
                            break;
                        case '>':
                            var op = optr.Pop();
                            rpn.Append(op + " ");
                            if (op == '!')
                            {
                                var popnd = opnd.Pop();
                                opnd.Push(Calculate(op, popnd));
                            }
                            else
                            {
                                var popnd2 = opnd.Pop();
                                var popnd1 = opnd.Pop();
                                opnd.Push(Calculate(popnd1, op, popnd2));
                            }
                            break;
                        default:
                            throw new InvalidOperationException("Invalid syntax.");
                    }
                }
            }
            return opnd.Pop();
        }
    }
}
