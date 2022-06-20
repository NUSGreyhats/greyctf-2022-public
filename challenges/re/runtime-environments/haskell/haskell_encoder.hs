import Data.Int
import Data.Char (ord, chr)
import Data.Bits
import Data.Time
import Data.Time.Clock.POSIX 
import qualified Data.ByteString.Char8 as BC
import qualified Data.ByteString as B

random :: Integral a => a -> Int32
random a =
    let t  = fromIntegral a :: Int32
        t1 = t `xor` (shiftL t 13)
        t2 = t1 `xor` (shiftR t1 17)
        t3 = t2 `xor` (shiftL t2 5)
    in
        t3

randomL :: Integral a => a -> [Int32]
randomL seed = 
    let r = random seed
    in r:randomL r


otp :: (Integral a1, Integral a2) => [a1] -> [a2] -> [Int32]
otp a b = zipWith xor (map fromIntegral a) (map fromIntegral b)

epoch :: UTCTime -> Int
epoch = floor .nominalDiffTimeToSeconds . utcTimeToPOSIXSeconds 


main :: IO()
main = 
  do
    input <- fmap B.unpack B.getLine
    time <- getCurrentTime
    pad <- return $ map (fromIntegral . (\x -> (.&.) x 0xff)) $ randomL $ epoch time
    t <- return $ otp input pad
    B.putStr $ BC.pack $ map (chr . fromIntegral) t

