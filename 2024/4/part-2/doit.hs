{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Use camelCase" #-}


-- This program finds counds the occurences of the word "MAS" Written in an
-- X-shape in a 2D list of characters, regardless of their ordering
--
-- i.e., if we assume "." are irrelevant characters
--
--     M.M
--     .A.
--     S.S
--
-- or
--     S.S
--     .A.
--     M.M



import Control.Applicative
-- Import the file containing the proper problem input
import Basis

-- Test if any point of the line is outside of the input matrix
is_line_outside input_matrix_arg line = let
        xmax = length input_matrix_arg -1
        ymax = length (head input_matrix_arg) -1

        xes = map fst line
        ys = map snd line

        -- All border tests on the x-es and the ys
        any_x_outside = or  $ [(<0) , (>xmax) ] <*> xes
        any_y_outside = or  $ [(<0) , (>ymax) ] <*> ys

        is_outside = any_x_outside || any_y_outside
    in is_outside


-- Get all combinations of how to draw a diagonal cross over a start-pont.
--
-- i.e
-- 0,1,2 and 2,1,0
-- or
-- 0,1,2 and 0,1,2
get_crosses_from_start_point :: (Int, Int) -> [([(Int, Int)], [(Int, Int)])]
get_crosses_from_start_point start = let
    add_tuple_elements (a,b) (c,d) = ((a+c), (b+d) )
    add_to_start_point = add_tuple_elements  start

    -- Create the two basic lines out from the start-point
    down_cross_diffs = [(negate 1,1 ) , (0,0) , (1, negate 1) ]
    up_cross_diffs = [(negate 1, negate 1 ) , (0,0) , (1,1) ]
    up_cross = map add_to_start_point  up_cross_diffs
    down_cross = map add_to_start_point  down_cross_diffs

    -- Get all variations of either reversing or not reversing the lines
    variants = [reverse, id]
    list_of_line_pairs = do
        op1 <- variants
        op2 <- variants
        return (op1 down_cross, op2 up_cross)

    in list_of_line_pairs

-- Will ignore indecies that are outside of the matrix
line_to_chars :: [[Char]] -> [(Int, Int)]  -> [Char]
line_to_chars input_matrix_arg line = let
        is_outside = is_line_outside input_matrix_arg line
        -- No output if the line is outside of the character matrix
        output False  = line_to_chars_inner input_matrix_arg line
        output _  = []
    in output is_outside

-- No bundary checking
line_to_chars_inner :: [[Char]] -> [(Int, Int)] -> [Char]
line_to_chars_inner input_matrix_arg line = do
    point  <- line
    let (x,y) = point
    -- NOTE: This is extremely slow, due to Haskell's indexing. Consider using
    -- the Vector package to get O(1) indexing instead of O(n)
    let char = (input_matrix_arg !! x ) !! y
    return char


-- Test if a any of all the possible versions of a cross contains the words MAS and MAS
-- Both lines in the cross contain a direction, so it will
-- evaluate false if it is given SAM instead of MAS
--
-- This is not optimized for exiting early if one of the lines is not MAS or SAM
-- The entire structure could also have been changed to only look at each direction once per edge
evaluate_crosses :: p -> [([(Int, Int)], [(Int, Int)])] -> Bool
evaluate_crosses input_matrix_arg crosses = let
    line_to_chars_partial =  line_to_chars input_matrix
    cross_to_chars (l1,l2) =  (line_to_chars_partial l1, line_to_chars_partial l2)
    cross_chars = map cross_to_chars crosses
    is_mas = any ( == ("MAS", "MAS")) cross_chars
    in is_mas




main = do
    -- Generate all the different possible start-points
    let basis_x = [0..(length input_matrix) ]
    let basis_y = [0..(length $ head input_matrix) ]

    -- This is just a cartesian product
    -- If the solution had been too slow, this could have been optimized by:
    -- - Filtering out any start-point that does not match an "A"
    -- - Not evaluatign along the borders, since we know how big the corss is
    let start_points = (,) <$> basis_x <*> basis_y


    -- Combine making a cross with evaluating if it contains "MAS" and "MAS"
    let evaluate = evaluate_crosses input_matrix .  get_crosses_from_start_point
    let evaluations = filter evaluate start_points

    -- Only pass the valid start points
    let valid_crosses = evaluations

    print  "N crosses with MAS and MAS in them"
    -- Count the number of valid crosses
    print $ length valid_crosses
