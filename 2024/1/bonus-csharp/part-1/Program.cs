// This program solves the first task of the first advent of code

// See https://aka.ms/new-console-template for more information
using System.Numerics;

using StreamReader reader = new("input.txt");
string text = reader.ReadToEnd();

var lines = text.Split("\n");

var v1 = new List<int>();
var v2 = new List<int>();

foreach (var line in lines)
{

    var words = line.Split(" ");
    Int32 o;
    var parsed_ints = words.Where(x => { return Int32.TryParse(x, out o); })

    .Select(x => { return Int32.Parse(x); })
    ;
    // foreach (var parsed_int in parsed_ints ){

    //     Console.WriteLine($"parsed int: {parsed_int}"); 
    // }
    List<int> parsed_ints_list = parsed_ints.ToList();
    Console.WriteLine($"-----");
    parsed_ints_list.ForEach(x => { Console.WriteLine($"{x}"); });
    Console.WriteLine($"-----");
    v1.Add(parsed_ints_list[0]);
    v2.Add(parsed_ints_list[1]);
}

var tot = 0;

Console.WriteLine($"{tot} {v1.Count}");
v1.Sort();
v2.Sort();



for (int i = 0; i < v1.Count; ++i)
{
    tot += Int32.Abs(
    v1[i] - v2[i]);
}

Console.WriteLine($"{tot} {v1.Count}");
