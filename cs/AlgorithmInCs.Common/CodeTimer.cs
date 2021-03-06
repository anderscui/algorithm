﻿using System;
using System.Diagnostics;
using System.Threading;
using System.Runtime.InteropServices;

namespace Andersc.AlgorithmInCs.Common
{
    /// <summary>
    /// Evaluates execution time of a block of code.
    /// Got it from: http://www.cnblogs.com/JeffreyZhao/archive/2009/03/10/codetimer.html
    /// You can check the results from command line window (console app) or output window(debugging info or unit test)
    /// </summary>
    public static class CodeTimer
    {
        // This API function only supports Vista/Sever 2008 or above.
        //[DllImport("kernel32.dll")]
        //[return: MarshalAs(UnmanagedType.Bool)]
        //static extern bool QueryThreadCycleTime(IntPtr threadHandle, ref ulong cycleTime);

        [DllImport("kernel32.dll", SetLastError = true)]
        static extern bool GetThreadTimes(IntPtr hThread, out long lpCreationTime,
           out long lpExitTime, out long lpKernelTime, out long lpUserTime);

        [DllImport("kernel32.dll")]
        static extern IntPtr GetCurrentThread();

        static CodeTimer()
        {
            // Set priority of current process to "high" to reduce the effect of OS.
            Process.GetCurrentProcess().PriorityClass = ProcessPriorityClass.High;
            Thread.CurrentThread.Priority = ThreadPriority.Highest;
        }

        public static void Time(string name, int iteration, Action action)
        {
            if (string.IsNullOrEmpty(name)) { return; }

            ConsoleColor currentForeColor = Console.ForegroundColor;
            Console.ForegroundColor = ConsoleColor.Yellow;
            Console.WriteLine(name);

            GC.Collect(GC.MaxGeneration, GCCollectionMode.Forced);
            int[] gcCounts = new int[GC.MaxGeneration + 1];
            for (int i = 0; i <= GC.MaxGeneration; i++)
            {
                gcCounts[i] = GC.CollectionCount(i);
            }

            Stopwatch watch = new Stopwatch();
            watch.Start();
            long ticksStart = GetCurrentThreadTimes();
            for (int i = 0; i < iteration; i++)
            {
                action();
            }
            long ticks = GetCurrentThreadTimes() - ticksStart;
            watch.Stop();

            Console.ForegroundColor = currentForeColor;

            Console.WriteLine("\tTime Elapsed:\t\t" + watch.ElapsedMilliseconds.ToString("N0") + "ms");
            Console.WriteLine("\tTime Elapsed (one time):" + (watch.ElapsedMilliseconds / iteration).ToString("N0") + "ms");

            Console.WriteLine("\tCPU time:\t\t" + (ticks * 100).ToString("N0") + "ns");
            Console.WriteLine("\tCPU time (one time):\t" + (ticks * 100 / iteration).ToString("N0") + "ns");

            for (int i = 0; i <= GC.MaxGeneration; i++)
            {
                int count = GC.CollectionCount(i) - gcCounts[i];
                Console.WriteLine("\tGen " + i + ": \t\t" + count);
            }

            Console.WriteLine();
        }

        private static long GetCurrentThreadTimes()
        {
            long creationTime;
            long kernelTime, userTime;
            GetThreadTimes(GetCurrentThread(), out creationTime, out creationTime,
                out kernelTime, out userTime);
            return kernelTime + userTime;
        }
    }
}
