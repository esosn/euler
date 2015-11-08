module euler92

open System.Collections
open System

let squareDigits x =
    x.ToString().ToCharArray() |>
    Array.sumBy (fun i -> (int (i.ToString())) * (int (i.ToString())))

let known = Generic.Dictionary<int, int>()

let rec checkNumbers cur = 
    match known.ContainsKey cur with
    | true when known.[cur] = 89 -> 1
    | true -> 0
    | _ ->
        let next = squareDigits cur
        match next with
        | 89 ->
            known.Add(cur, 89)
            1
        | 1 ->
            known.Add(cur, 1)
            0
        | _ ->
            match checkNumbers next with
            | 1 -> 
                known.Add(cur, 89)
                1
            | _ -> 
                known.Add(cur, 1)
                0

let run =
    [44;32;13;10;1] |> List.iter (fun x -> known.Add(x, 1)) 
    [85;89;145;42;20;4;16;37;58] |> List.iter (fun x -> known.Add(x, 89)) 
    [2..9999999] |> List.sumBy (fun x -> checkNumbers x) |> printfn "%A"