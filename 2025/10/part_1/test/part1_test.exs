defmodule Part1Test do
  use ExUnit.Case
  doctest Part1

  test "Parses input" do
    file_name = "resources/short.txt"
    # contents = Part1.parse_input("resources/part_1_input.txt")
    contents = Part1.parse_input(file_name)

    depths = contents |> Enum.map(&Part1.bfs_candidates(&1.fuse_box, &1.connections))
    assert depths == [2, 3, 2]
  end
end
