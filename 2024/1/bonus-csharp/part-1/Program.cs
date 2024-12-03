// See https://aka.ms/new-console-template for more information
using StreamReader reader = new("input.txt");
string text = reader.ReadToEnd();



Console.WriteLine($"Hello, World! and more mmm {text}");
