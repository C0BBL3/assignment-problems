recommendedClothing :: (RealFloat a) => a -> String  
recommendedClothing degreesCelcius  
    | degreesFahrenheit < maximumCold = "It is recommend to wear a jacket."  
    | degreesFahrenheit < kindaCold = "It is recommend to wear a sweater."   
    | degreesFahrenheit < notCold = "It is recommend to wear a longsleeve shirt." 
    | otherwise = "It is recommend to wear a shortsleeve shirt."  
    where degreesFahrenheit = 9 / 5 * degreesCelcius + 32
          maximumCold = 50 
          kindaCold = 65
          notCold = 80 

main = print (recommendedClothing 10)