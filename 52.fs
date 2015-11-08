module euler52

let rec checkAnagrams x i =
    match functions.areAnagrams x (i*x) with
    | false -> false
    | true when i = 6 -> true
    | true -> checkAnagrams x (i+1)

let run =
    Seq.initInfinite (fun x -> x + 1)
    |> Seq.find (fun x -> ([2..6] |> List.forall (checkAnagrams x)))
    |> printfn "%d"
    |> ignore