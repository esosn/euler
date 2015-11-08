module euler41

open functions

let run =
    functions.sieve (10000000 |> uint64) |> List.rev |>
    List.find (fun x -> functions.is1nPanDigital x) |> printfn "%d" |> ignore
