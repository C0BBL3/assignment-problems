classifyNumber x = if x < 0 then "negative" else "nonnegative"
main = putStrLn (classifyNumber 5)