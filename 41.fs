// Learn more about F# at http://fsharp.org
// See the 'F# Tutorial' project for more help.
open System.Collections
open System

/// Segmented sieve of Eratosthenes
/// returns ordered list of primes < n
/// not optimized - needs wheel factorization, bit packing
let sieve (n:uint64) =
    let maxSeg = 1024*1024
    let segSize = 
        match n >= (maxSeg |> uint64) with
        | true -> maxSeg
        | false -> (n |> int)
    let segCount = 
        (match n % (maxSeg |> uint64) = 0UL with
        | true -> n / (maxSeg |> uint64)
        | false -> 1UL + n / (maxSeg |> uint64))
        |> int
    let candidates = [| for i in 0..segCount-1 do yield new BitArray(segSize, true) |]
    let max = (sqrt (n |> float)) |> int
    // 0 and 1 are not prime
    candidates.[0].Set(0, false)
    candidates.[0].Set(1, false)
    // each segment represents some chunk of values between 0 and n
    let getOffset startVal i = 
        match startVal <> 0 && startVal % i = 0 with
        | true -> 0
        | false -> startVal / i * i + i - startVal
    // sieve out prime multiples
    for i in 2..max+1 do
        let segNo = i / segSize
        let startVal = segNo * segSize
        let offset = getOffset startVal i
        if candidates.[segNo].Get(offset) then
            // don't accidentally unset the found prime
            [offset+i..i..segSize-1] |>
                List.iter (fun k -> candidates.[segNo].Set(k, false))
            // mark off remaining segments
            [segNo+1..segCount-1] |> List.iter (fun j ->
                let startVal = j * segSize
                let offset = getOffset startVal i
                [offset..i..segSize-1] |>
                    List.iter (fun k -> candidates.[j].Set(k, false)))
    // return the list of primes
    [for i in 0..segCount-1 do
        for j in 0..segSize-1 do 
            let value = i*segSize+j
            if candidates.[i].Get j && (value |> uint64) <= n then 
                yield value]
                
/// Determines whether a given integer contains exactly one of each
/// digit from 1 to n, where n is the number of digits in the number
let is1nPanDigital x =
    let rec checkChar (arr:char[]) (i:int) (found:Set<char>) =
        if i >= Array.length arr then
            found.MaximumElement = ((arr.Length.ToString()) |> char)
        else
            let c = arr.[i]
            match c='0' || found.Contains(c) with
            | true -> false
            | false -> checkChar arr (i+1) (found.Add(c))
    checkChar (x.ToString().ToCharArray()) 0 Set.empty<char>

[<EntryPoint>]
let main argv =
    sieve (10000000 |> uint64) |> List.rev |>
    List.find (fun x -> is1nPanDigital x) |> printfn "%d" |> ignore
    // pause the console to read the result
    Console.ReadKey(true) |> ignore
    0 // return an integer exit code
