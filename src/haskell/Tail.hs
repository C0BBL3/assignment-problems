reverseList :: [a] -> [a]
reverseList [] = []
reverseList (x : xs) = reverseList xs ++ [x]

splice :: (Num i, Ord i) => i -> [a] -> [a]
splice n _
  | n <= 0 = []
splice _ [] = []
splice n (x : xs) = x : splice (n -1) xs

tail :: (Num a, Ord a) => a -> [a] -> [a]
tail n x = reverseList (splice n (reverseList x))

main = print (tail 4 [8, 3, -1, 2, -5, 7])