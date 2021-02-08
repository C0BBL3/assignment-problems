fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci (n-1) + fibonacci (n-2)

kthPartialSum  k = sum [fibonacci(x) | x <- [0..k] ]
metaSum n = sum [kthPartialSum(fibonacci(k)) | k <- [0..n] ]

main = print (metaSum 6)