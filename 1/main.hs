import System.Environment


getFuelCost mass = (mass `div` 3) - 2
getFuelCostRecursive mass
    | getFuelCost mass <= 0 = 0
    | otherwise = getFuelCost mass + getFuelCostRecursive (getFuelCost mass)


main = do
    d <- readFile "input.txt"
    let masses = toInt (lines d)
    let partOne = show (sum (map getFuelCost masses))
    let partTwo = show (sum (map getFuelCostRecursive masses))
    putStrLn $ "Part 1: " ++ partOne
    putStrLn $ "Part 2: " ++ partTwo


toInt :: [String] -> [Int]
toInt = map read
