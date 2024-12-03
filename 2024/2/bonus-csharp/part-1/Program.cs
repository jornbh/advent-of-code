// See https://aka.ms/new-console-template for more information
using System.Xml.Serialization;

using static MyBar; 
using System.Runtime.InteropServices;

int[] a = { 1, 2, 3 };
int[] b = { 1, 2, 3 };
int[][] c = { a, b };


Console.WriteLine($"{a}");

foreach (var elc in c)
{
    foreach (var el in elc)
    {

        var one = MyBar.Return1(); 
        Console.WriteLine(el);
        Console.WriteLine(one);
    }
}
Console.WriteLine("Hello, World!");
