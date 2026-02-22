open System
open System.IO

// tHIS EXAMPLE WAS ABLE TO READ A STRING AND CONCAT SOMETHING TO THE RESULTS

// main  [] 

let filename = "input.txt"


let lines   = File.ReadLines filename 

lines 
|> Seq.map ((+) "AAA "  )
|> Seq.iter (printfn "aaa %s")

"HELLO"
|> Seq.mapi (fun ind  arg -> arg )


// EXAMPLES 
// you can get head and tail of a list
let h :: tl = [1..10] ;; 

// printing lists 
printf "%i" h
printf "%A" tl

// Or using the more generic function
// for loops also exist 
// you can even pattern match in a function 
for el@(7 | 8) in tl do 
Console.WriteLine 7 ; 
done  

// Stolen code 
// open System
// open System.IO

// [<EntryPoint>]
// let main argv =
//     if argv.Length <> 1 then
//         eprintfn "Usage: dotnet run <filename>"
//         1
//     else
//         let filePath = argv.[0]

//         if not (File.Exists filePath) then
//             eprintfn "File not found: %s" filePath
//             1
//         else
//             File.ReadLines(filePath)
//             |> Seq.mapi (fun i line -> sprintf "%d: %s" (i + 1) line)
//             |> Seq.iter (printfn "%s")
//             0
