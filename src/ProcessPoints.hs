smallestDistances :: (RealFloat a) => [(a, a, a)] -> [a]
smallestDistances xyz = [norm | (x, y, z) <- xyz, let norm = sqrt (x ^ 2 + y ^ 2 + z ^ 2), norm <= 10.0]

main = print (smallestDistances [(5, 5, 5), (3, 4, 5), (8, 5, 8), (9, 1, 4), (11, 0, 0), (12, 13, 14)])