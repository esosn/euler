module main

[<EntryPoint>]
let main argv =
    let timer = System.Diagnostics.Stopwatch.StartNew()
    // euler##.run
    euler100.run
    printfn "%f ms" timer.Elapsed.TotalMilliseconds
    // pause the console to read the result
    printfn "Press any key to exit" |> ignore
    System.Console.ReadKey(true) |> ignore
    0