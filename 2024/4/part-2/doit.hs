{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Use camelCase" #-}
import Control.Applicative
-- import qualified Data.Vector as V
import Basis


diff_foos_bases :: [Int -> Int]


diff_foos_bases = [(+0), (+1) , (+ negate 1) ]

diff_foos :: [(Int -> Int, Int -> Int)]
diff_foos = (,) <$> diff_foos_bases <*> diff_foos_bases

apply_diff_foo_succ :: (a -> a, b -> b) -> (a, b) -> [(a, b)]
apply_diff_foo_succ (fa , fb ) (a,b) = (a,b):apply_diff_foo_succ  (fa, fb) (fa a, fb b)

start_point_to_lines :: (Int, Int) -> [[(Int, Int)]]
start_point_to_lines  start_point = map (($ start_point) . apply_diff_foo_succ) diff_foos


--input_matrix :: [[Char]]
--input_matrix = [ "XMAS" ,         [ 'X', 'M', 'A', 'S' ]     ]

m2 foo = map (map foo)
f2 foo = map (filter foo)


is_line_outside input_matrix_arg line = let

        xmax = length input_matrix_arg -1
        ymax = length (head input_matrix_arg) -1

        xes = map fst line
        ys = map snd line

        is_outside = or [any (<0) xes ,         any (>xmax) xes ,         any (<0) ys,         any (>ymax) ys        ]

    in is_outside

line_to_chars :: [[Char]] -> [(Int, Int)]  -> [Char]
line_to_chars input_matrix_arg line = let
        is_outside = is_line_outside input_matrix_arg line
        output False  = line_to_chars_inner input_matrix_arg line
        output _  = []
    in output is_outside
    -- in output

get_cross_from_start :: (Int, Int) -> [([(Int, Int)], [(Int, Int)])]
get_cross_from_start start = let

    add_tuples (a,b) (c,d) = ((a+c), (b+d) )

    down_cross_diffs = [(negate 1,1 ) , (0,0) , (1, negate 1) ]
    up_cross_diffs = [(negate 1, negate 1 ) , (0,0) , (1,1) ]

    up_cross = map (add_tuples start)  up_cross_diffs
    down_cross = map (add_tuples start)  down_cross_diffs


    variants = [reverse, id]

    outputs = do
        op1 <- variants
        op2 <- variants
        return (op1 down_cross, op2 up_cross)

    in outputs


line_to_chars_inner :: [[Char]] -> [(Int, Int)] -> [Char]
line_to_chars_inner input_matrix_arg line = do

    point  <- line

    let (x,y) = point

    let char = (input_matrix_arg !! x ) !! y
    -- let char ='X'
    return char


evaluate_cross :: p -> [([(Int, Int)], [(Int, Int)])] -> Bool
evaluate_cross input_matrix_arg cross = let
    cross_to_chars (l1,l2) =  (line_to_chars input_matrix l1, line_to_chars input_matrix l2)
    cross_chars = map cross_to_chars cross
    is_mas = any ( == ("MAS", "MAS")) cross_chars
    in is_mas




main = do
    let start = (0,0)  :: (Int, Int)
    let basis_x = [0..(length input_matrix) ]
    let basis_y = [0..(length $ head input_matrix) ]
    let start_points = (,) <$> basis_x <*> basis_y
    let lines_inf = concatMap start_point_to_lines start_points
    let lines = map (take 4) $ filter (\(f:s:tl) -> f/=s  ) lines_inf
    let dummy_line =   lines  !! 0
    let dummy_chars = line_to_chars_inner input_matrix (dummy_line )

    let char_lists_unfiltered = map (line_to_chars input_matrix) lines
    let char_lists = filter (=="XMAS") char_lists_unfiltered
    -- let char_lists =  char_lists_unfiltered
    print "Indices"
    print dummy_line
    print $ take 50 $ map (take 5)   lines
    print "DUMMY CHARS"
    print dummy_chars
    print "CHARS"
    print $ length  char_lists
    print $ "Cross from start"

    -- let list_of_crosses = 


    let evaluate = evaluate_cross input_matrix .  get_cross_from_start

    let cross = get_cross_from_start (1,1)  :: [([(Int, Int)], [(Int,Int)])]
                                            -- ([(Int, Int)], [(Int, Int)])


    let evaluations = map evaluate start_points

    -- let eval = evaluate_cross input_matrix cross

    print $ length $ filter id  evaluations
