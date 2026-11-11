defmodule Part1Test do
  use ExUnit.Case
  doctest Part1

  test "Parses input" do
    file_name = "resources/short.txt"
    contents = Part1.parse_input("resources/part_1_input.txt")

    dbg()

    depths =
      for problem <- contents do
        Part1.bfs_candidates(problem.fuse_box, problem.connections)
      end
      dbg()
  end
end
