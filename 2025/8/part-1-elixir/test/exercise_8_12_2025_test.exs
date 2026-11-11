defmodule EX08Dec2025Test do
  use ExUnit.Case
  doctest EX08Dec2025

  test "Making new clusters makes simple boxes" do
    boxes = [
      {1, 3, 4},
      {2, 4, 5}
    ]

    clusters = EX08Dec2025.single_custers_from_boxes(boxes)
    expected_clusters = %{
      {1, 3, 4} => [{1, 3, 4}],
      {2, 4, 5} => [{2, 4, 5}]
    }

    assert clusters == expected_clusters,
           "Mapping clusters properly did not work the expected way"
  end

  test "Passes the simple short case where 10 are merged and the result is 40" do
    # {:ok, cont} = File.read("resources\\advent_of_code_2025\\08\\part_1.txt")
    {:ok, cont} = File.read("resources\\advent_of_code_2025\\08\\short.txt")
    assert :world == :world, "Positive test"

    result = EX08Dec2025.part_1_inner(cont, 10)
    assert result == 40, "Correct response for the simple case #{inspect(result)}"
  end

  test "Square distance works" do
    box_1 = [1, 1, 1]
    box_2 = [1, 1, 2]

    distance_squared = EX08Dec2025.square_distance(box_1, box_2)
    assert distance_squared == 1, "Square distance"
  end

  test "We find nearby clusters" do
    cluster_1 = [[1, 1, 1], [1, 1, -99991]]
    cluster_2 = [[1, 1, 2], [1, 1, 2]]

    distance_squared = EX08Dec2025.shortest_distance_between_clusters(cluster_1, cluster_2)
    assert distance_squared == 1, "Square distance"
  end

  # test "Merging clusters" do
  #   cluster_list_before = [
  #     [
  #       [1, 1, 1]
  #     ],
  #     [
  #       [1, 1, 2],
  #       [1, 1, 2]
  #     ],
  #     [[9999, 9999, 9999]]
  #   ]
  #
  #   cluster_list_after = EX08Dec2025.recursively_merge_clusters_n_times(1, cluster_list_before)
  #
  #   expected_after = [
  #     [
  #       [1, 1, 1],
  #       [1, 1, 2],
  #       [1, 1, 2]
  #     ],
  #     [
  #       [9999, 9999, 9999]
  #     ]
  #   ]
  #
  #   IO.inspect("Comparing clusters")
  #   IO.inspect(cluster_list_after)
  #
  #   IO.inspect(expected_after)
  #   assert cluster_list_after == expected_after, "Merging works"
  # end

  test "File contents get parsed" do
    {:ok, cont} = File.read("resources\\advent_of_code_2025\\08\\short.txt")

    ret = EX08Dec2025.parse_file_contents(cont)

    assert ret == [
             [162, 817, 812],
             [57, 618, 57],
             [906, 360, 560],
             [592, 479, 940],
             [352, 342, 300],
             [466, 668, 158],
             [542, 29, 236],
             [431, 825, 988],
             [739, 650, 466],
             [52, 470, 668],
             [216, 146, 977],
             [819, 987, 18],
             [117, 168, 530],
             [805, 96, 715],
             [346, 949, 466],
             [970, 615, 88],
             [941, 993, 340],
             [862, 61, 35],
             [984, 92, 344],
             [425, 690, 689]
           ]
  end
end
