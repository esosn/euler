module euler63

open System
open System.Collections
open System.Numerics

let isPowerful total i j =
    match (BigInteger.Pow(i, j).ToString().Length) = j with
    | false -> 0
    | true -> 1
    
/// count all a such that a = b**len(a)
/// b will always be 1..9 as len(10**x) = x+1
/// 9**22 only has 21 digits, so that's the ceiling
/// just check all base/power combinations
let run = 
    [2..9] |> List.sumBy (fun i ->
        (List.fold (fun (total) (y:int) -> total + (isPowerful total (Numerics.BigInteger i) y)) 
            0 [2..21])) |> (+) 9 // 1..9 ** 1 all match
            |> printfn "%A"