defmodule Part1Test do
  use ExUnit.Case
  doctest Part1

  test "Parses input" do
    file_name = "resources/short.txt"
    # contents = Part1.parse_input("resources/part_1_input.txt")
    contents = Part1.parse_input("resources/short.txt")
    dbg()

    # contents = problems |> Enum.map(&Part1.from_input_line_to_dict/1)



    depths = contents |> Enum.map(&Part1.bfs_candidates(&1.fuse_box, &1.connections))

    # contents = problems |> Enum.map(&Part1.from_input_line_to_dict/1)
    dbg(depths)

  end
end
