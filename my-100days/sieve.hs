sieve remaining = nextItem : sieve (filter (\x -> x `mod` nextItem /= 0) remaining)
    where
        nextItem = head remaining

main = mapM print $ take 100000 $ sieve [2..]
