module euler74

open functions
open System.Collections

let known = new Generic.Dictionary<int,int>()
known.Add(0, 2)
known.Add(1, 1)

let facDigits x =
    x.ToString().ToCharArray()
    |> Array.fold (fun total c -> total + (factorial(int (c.ToString())))) 0

let rec countTerms count (seen:Set<int>) x =
    match seen.Contains(x) with
    | true when (known.ContainsKey(x) <> true) -> 
        known.Add(x, count) |> ignore
        count
    | true -> count 
    | false when known.ContainsKey(x) -> (count + known.[x])
    | false -> 
        let next = countTerms (count + 1) (seen.Add(x)) (facDigits x)
        if known.ContainsKey(x) <> true then
            known.Add(x, next - count) |> ignore
        next

let run =
    [3..999999] |> List.fold (fun total x -> 
    (match countTerms 0 Set.empty<int> x with
    | 60 -> 1
    | _ -> 0) + total) 0 |> printfn "%A"