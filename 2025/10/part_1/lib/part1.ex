defmodule Part1 do
  @moduledoc """
  --- Day 10: Factory ---
  Just across the hall, you find a large factory. Fortunately, the Elves here have plenty of time to decorate. Unfortunately, it's because the factory machines are all offline, and none of the Elves can figure out the initialization procedure.

  The Elves do have the manual for the machines, but the section detailing the initialization procedure was eaten by a Shiba Inu. All that remains of the manual are some indicator light diagrams, button wiring schematics, and joltage requirements for each machine.

  For example:

  [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
  [...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
  [.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
  The manual describes one machine per line. Each line contains a single indicator light diagram in [square brackets], one or more button wiring schematics in (parentheses), and joltage requirements in {curly braces}.

  To start a machine, its indicator lights must match those shown in the diagram, where . means off and # means on. The machine has the number of indicator lights shown, but its indicator lights are all initially off.

  So, an indicator light diagram like [.##.] means that the machine has four indicator lights which are initially off and that the goal is to simultaneously configure the first light to be off, the second light to be on, the third to be on, and the fourth to be off.

  You can toggle the state of indicator lights by pushing any of the listed buttons. Each button lists which indicator lights it toggles, where 0 means the first light, 1 means the second light, and so on. When you push a button, each listed indicator light either turns on (if it was off) or turns off (if it was on). You have to push each button an integer number of times; there's no such thing as "0.5 presses" (nor can you push a button a negative number of times).

  So, a button wiring schematic like (0,3,4) means that each time you push that button, the first, fourth, and fifth indicator lights would all toggle between on and off. If the indicator lights were [#.....], pushing the button would change them to be [...##.] instead.

  Because none of the machines are running, the joltage requirements are irrelevant and can be safely ignored.

  You can push each button as many times as you like. However, to save on time, you will need to determine the fewest total presses required to correctly configure all indicator lights for all machines in your list.

  There are a few ways to correctly configure the first machine:

  [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
  You could press the first three buttons once each, a total of 3 button presses.
  You could press (1,3) once, (2,3) once, and (0,1) twice, a total of 4 button presses.
  You could press all of the buttons except (1,3) once each, a total of 5 button presses.
  However, the fewest button presses required is 2. One way to do this is by pressing the last two buttons ((0,2) and (0,1)) once each.

  The second machine can be configured with as few as 3 button presses:

  [...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
  One way to achieve this is by pressing the last three buttons ((0,4), (0,1,2), and (1,2,3,4)) once each.

  The third machine has a total of six indicator lights that need to be configured correctly:

  [.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
  The fewest presses required to correctly configure it is 2; one way to do this is by pressing buttons (0,3,4) and (0,1,2,4,5) once each.

  So, the fewest button presses required to correctly configure the indicator lights on all of the machines is 2 + 3 + 2 = 7.

  Analyze each machine's indicator light diagram and button wiring schematics. What is the fewest button presses required to correctly configure the indicator lights on all of the machines?

  """

  @doc """
  Hello world.

  ## Examples

      iex> Part1.hello()
      :world

  """
  def hello do
    :world
  end

  def parse_input(file_name) do
    {:ok, contents} = File.read(file_name)

    contents
    |> String.split("\r\n")
    |> Enum.filter(&(String.length(&1) > 0))
    |> Enum.map(&from_input_line_to_dict(&1))

    # |> dbg()
  end

  @spec from_input_line_to_dict(any()) :: %{connections: [bitstring()], fuse_box: bitstring()}
  def from_input_line_to_dict(input_line) do
    parts =
      input_line
      |> String.split(" ")

    # Drop last element

    # dbg()

    [fuse_box_str | connections_strings] =
      parts
      |> Enum.take(Enum.count(parts) - 1)

    fuse_box_str
    |> String.trim(" ")
    |> String.trim("[")
    |> String.trim("]")
    |> String.split(",")
    |> Enum.map(&(&1 == "#"))

    connections =
      connections_strings
      |> Enum.map(fn connection_string ->
        connection_string
        |> String.trim("(")
        |> String.trim(")")
        |> String.split(",")
        |> Enum.map(&String.to_integer(&1))
      end)

    fuse_box_list =
      fuse_box_str
      |> String.to_charlist()
      |> Enum.map(&(&1 == ?#))
      # Convert to ints
      |> Enum.map(&if &1, do: 1, else: 0)

    # Reversing will make this into a big endian list
    fuse_box_raw = for el <- Enum.reverse(fuse_box_list), into: <<>>, do: <<el::1>>

    # n_bits = Enum.count(for <<_bit::1 <- fuse_box_raw>>, into: [], do: [])
    n_bits = bit_size(fuse_box_raw) 

    remaining_bits = 64 - n_bits
    # fuse_box_padded = <<0::size(remaining_bits), fuse_box_raw::size(n_bits)>>
    rhs = fuse_box_raw
    lhs = <<0::size(remaining_bits)>>
    fuse_box_padded = <<rhs::bitstring, lhs::bitstring>>
    # fuse_box = fuse_box_raw
    fuse_box = fuse_box_padded
    n_bits_to_match = bit_size(fuse_box) 
    dbg()

    list_of_connection_masks =
      connections |> Enum.map(&connection_mask_list_to_bit_mask(&1, n_bits_to_match))

    %{fuse_box: fuse_box, connections: list_of_connection_masks}
  end

  def bfs_candidates(fuse_box, connections) do
    bfs_candidates_inner(fuse_box, connections, connections, 1)
  end

  def bfs_candidates_inner(fuse_box, connections, candidates, 1000) do
    dbg(fuse_box)
    dbg(connections)
    dbg(candidates)
    raise "Too deep"
    # Failed
  end

  def bfs_candidates_inner(fuse_box, connections, candidates, depth) do
    dbg()
    combinations = for el1 <- connections, el2 <- candidates, into: [], do: {el1, el2}

    updated_candidates =
      combinations
      |> dbg()
      |> Enum.map(fn {el1, el2} -> :crypto.exor(el1, el2) end)
      |> Enum.into(MapSet.new())

    {fuse_box, depth}
    |> dbg()

    if Enum.any?(updated_candidates, &(&1 == fuse_box)) do
      depth
    else
      bfs_candidates_inner(fuse_box, connections, updated_candidates, depth + 1)
    end

    Enum.flat_map(candidates, & &1)
  end

  @spec connection_mask_list_to_bit_mask(any(), integer()) :: bitstring()
  def connection_mask_list_to_bit_mask(connection_masks_list, n_bits) do
    position_to_bit = fn el ->
      bit =
        if Enum.any?(connection_masks_list, &(el == &1)) do
          1
        else
          0
        end

      <<bit::1>>
    end

    connections_mask_list = Enum.map(0..(n_bits-1), position_to_bit)
    # Is this now little endian? 
    # TOOD:  I need to look at how this fits with the other number!
    # 0,1,2,3,4,5, etc
    for el <- connections_mask_list, into: <<>>, do: el
  end

  def part_1() do
    problems = parse_input("resources/part_1_input.txt")

    contents = problems |> Enum.map(&from_input_line_to_dict/1)
    dbg()

    depths =
      for problem <- contents do
        bfs_candidates(problem.fuse_box, problem.connections)
      end
    dbg()
    # final_node, connections

    # Doing a BFS would lead us there
    # The largest fuse box is 10 nodes
    # That woulld be 150 * 10 * N combinations or so
    # Bitwise.bxor(current_list, flip_list)
    dbg()
  end
end
