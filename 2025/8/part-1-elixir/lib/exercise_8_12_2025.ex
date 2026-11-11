defmodule EX08Dec2025 do
  @moduledoc """
  Day 8: Playground
  Equipped with a new understanding of teleporter maintenance, you confidently step onto the repaired teleporter pad.

  You rematerialize on an unfamiliar teleporter pad and find yourself in a vast underground space which contains a giant playground!

  Across the playground, a group of Elves are working on setting up an ambitious Christmas decoration project. Through careful rigging, they have suspended a large number of small electrical junction boxes.

  Their plan is to connect the junction boxes with long strings of lights. Most of the junction boxes don't provide electricity; however, when two junction boxes are connected by a string of lights, electricity can pass between those two junction boxes.

  The Elves are trying to figure out which junction boxes to connect so that electricity can reach every junction box. They even have a list of all of the junction boxes' positions in 3D space (your puzzle input).

  For example:

  162,817,812
  57,618,57
  906,360,560
  592,479,940
  352,342,300
  466,668,158
  542,29,236
  431,825,988
  739,650,466
  52,470,668
  216,146,977
  819,987,18
  117,168,530
  805,96,715
  346,949,466
  970,615,88
  941,993,340
  862,61,35
  984,92,344
  425,690,689
  This list describes the position of 20 junction boxes, one per line. Each position is given as X,Y,Z coordinates. So, the first junction box in the list is at X=162, Y=817, Z=812.

  To save on string lights, the Elves would like to focus on connecting pairs of junction boxes that are as close together as possible according to straight-line distance. In this example, the two junction boxes which are closest together are 162,817,812 and 425,690,689.

  By connecting these two junction boxes together, because electricity can flow between them, they become part of the same circuit. After connecting them, there is a single circuit which contains two junction boxes, and the remaining 18 junction boxes remain in their own individual circuits.

  Now, the two junction boxes which are closest together but aren't already directly connected are 162,817,812 and 431,825,988. After connecting them, since 162,817,812 is already connected to another junction box, there is now a single circuit which contains three junction boxes and an additional 17 circuits which contain one junction box each.

  The next two junction boxes to connect are 906,360,560 and 805,96,715. After connecting them, there is a circuit containing 3 junction boxes, a circuit containing 2 junction boxes, and 15 circuits which contain one junction box each.

  The next two junction boxes are 431,825,988 and 425,690,689. Because these two junction boxes were already in the same circuit, nothing happens!

  This process continues for a while, and the Elves are concerned that they don't have enough extension cables for all these circuits. They would like to know how big the circuits will be.

  After making the ten shortest connections, there are 11 circuits: one circuit which contains 5 junction boxes, one circuit which contains 4 junction boxes, two circuits which contain 2 junction boxes each, and seven circuits which each contain a single junction box. Multiplying together the sizes of the three largest circuits (5, 4, and one of the circuits of size 2) produces 40.

  Your list contains many junction boxes; connect together the 1000 pairs of junction boxes which are closest together. Afterward, what do you get if you multiply together the sizes of the three largest circuits?

  To play, please identify yourself via one of these services:
  """

  def parse_file_contents(file_string) do
    lines =
      file_string
      |> String.split("\r\n")

    number_strings =
      lines
      |> Enum.map(&String.split(&1, ","))
      |> Enum.filter(&(Enum.count(&1) == 3))

    integer_matrix =
      number_strings
      |> Enum.map(&Enum.map(&1, fn el -> String.to_integer(el) end))
      |> Enum.map(fn [a, b, c] -> {a, b, c} end) # Convert from lists into tuples

    integer_matrix
  end

  @doc """
  The final output was
  28980
  {6, 28980}
  29010
  {5, 29010}
  997
  {4, 997}
  998
  {3, 998}
  """
  def part_1() do
    {:ok, cont} = File.read("resources\\advent_of_code_2025\\08\\part_1.txt")
    result = part_1_inner(cont)
    IO.inspect("result")
    IO.inspect(result)
  end

  def single_custers_from_boxes(boxes) do
    boxes |> Enum.map(&{&1, [&1]}) |> Map.new()
  end

  def part_1_inner(file_contents, n_merges \\ 1000) do
    _ret = file_contents |> String.length()
    boxes = parse_file_contents(file_contents)

    clusters = single_custers_from_boxes(boxes)

    # Connect 1000 boxes
    # multiply the sizes of the 3 largest circuits
    # cluster_results = recursively_merge_clusters_n_times(1001, clusters)
    cluster_results = simple_merge(clusters, n_merges)
    # cluster_results = recursively_merge_clusters_n_times(1001, clusters)
    evaluation = get_score_given_current_set_of_clusters(cluster_results)
    dbg()
  end

  # This is the way that part 1 mentioned merging 
  def simple_merge(single_node_clusters, n_merges \\ 1000) do
    # TODO: I left off here. Unable to merge everything properly. I also
    # misunderstood the task quite badly. But it did feel like i got to practice
    # quite a bit of operations in Elixir at least
    thousand_closest_pairs = shortest_pairs(single_node_clusters) |> Enum.take(n_merges)
    simplify_cluster(single_node_clusters, thousand_closest_pairs)
  end

  def simplify_cluster(cluster_to_update, []) do
    cluster_to_update
  end

  def simplify_cluster(clusters_to_update, [{_dist, cluster_1, cluster_2} | tail]) do
    get_score_given_current_set_of_clusters(clusters_to_update)

    # Debug 
    ############################################
    # IO.inspect("Clusters to update")
    # IO.inspect(
    # clusters_to_update
    # |> Enum.map(&Enum.count(&1))
    # |> Enum.group_by(& &1)
    # |> Enum.map(fn {arg1, arg2} -> {arg1, Enum.count(arg2)} end)
    # |> IO.inspect()
    # )

    ############################################

    # clusters_that_will_be_merged = Enum.filter(clusters_to_update, &(any_overlap_in_cluster(&1)) )
    clusters_that_will_be_merged =
      Enum.filter(
        clusters_to_update,
        fn cluster_to_cuery ->
          modified = cluster_to_cuery -- (cluster_1 ++ cluster_2)
          Enum.count(modified) != Enum.count(cluster_to_cuery)
        end
      )

    nodes_that_will_be_removed = Enum.flat_map(clusters_that_will_be_merged, & &1)
    nodes_to_add = (cluster_1 ++ cluster_2) -- nodes_that_will_be_removed
    new_cluster = nodes_to_add ++ nodes_that_will_be_removed
    IO.inspect(new_cluster)
    new_list_of_clusters = ([new_cluster] ++ clusters_to_update) -- clusters_that_will_be_merged
    simplify_cluster(new_list_of_clusters, tail)
  end

  def get_score_given_current_set_of_clusters(clusters) do
    sorted =
      clusters
      |> Enum.sort_by(&Enum.count(&1), :desc)

    [a, b, c | _tail] = sorted

    (Enum.count(a) * Enum.count(b) * Enum.count(c))
    |> IO.inspect()
  end

  def square_distance(box_1, box_2) do
    Enum.zip(box_1, box_2)
    |> Enum.map(fn {arg1, arg2} -> arg1 - arg2 end)
    |> Enum.map(&(&1 * &1))
    |> Enum.sum()
  end

  def shortest_distance_between_clusters(cluster_1, cluster_2) do
    res =
      for box_1 <- cluster_1 do
        for box_2 <- cluster_2 do
          square_distance(box_1, box_2)
        end
      end

    res |> Enum.map(&Enum.min(&1)) |> Enum.min()
  end

  def shortest_pairs(input_cluser_list) do
    pairs =
      for cluster_1 <- input_cluser_list do
        for cluster_2 <- input_cluser_list, cluster_1 < cluster_2 do
          {shortest_distance_between_clusters(cluster_1, cluster_2), cluster_1, cluster_2}
        end
      end

    pairs |> Enum.flat_map(& &1) |> Enum.sort()
  end

  # This secrion is not needed anymore. But it was a part of my first solution. 
  #################################
  def merge_n_clusters_together(input_cluser_list, 1) do
    # HACK: The only version that may work now. Another faster one should be possible
    shortest_pairs = shortest_pairs(input_cluser_list)
    {_dist, cluster_1, cluster_2} = shortest_pairs |> Enum.min()

    clusters_to_remove = [cluster_1, cluster_2]

    cleaned = input_cluser_list -- clusters_to_remove
    combined_cluster = cluster_1 ++ cluster_2
    [combined_cluster | cleaned]
  end

  def merge_n_clusters_together(input_cluser_list, max_cap) do
    IO.inspect(input_cluser_list)

    shortest_pairs =
      shortest_pairs(input_cluser_list)
      |> Enum.take(max_cap)

    clusters_to_remove =
      shortest_pairs |> Enum.flat_map(fn {_, a, b} -> [a, b] end) |> Enum.take(max_cap)

    # HACK, I am only able to do one for now
    [{_dist, cluster_1, cluster_2} | _tail] = shortest_pairs
    cleaned = input_cluser_list -- clusters_to_remove
    combined_cluster = cluster_1 ++ cluster_2

    ([combined_cluster] ++ cleaned)
    |> IO.inspect()
  end

  def recursive_merge_into(_merge_map, false) do
    {[], %{}}
  end

  def recursive_merge_into(merge_map, merge_into) do
    next_merge_into = Map.get(merge_map, merge_into, false)
    {to_merge_into, visited} = recursive_merge_into(merge_map, next_merge_into)
    new_visited = Map.put(visited, merge_into, true)
    {merge_map[merge_into] ++ to_merge_into, new_visited}
  end

  def recursively_merge_clusters_n_times(0, clusters) do
    clusters
  end

  def recursively_merge_clusters_n_times(count, clusters) do
    new_clusters = merge_n_clusters_together(clusters, 1)
    evaluation = get_score_given_current_set_of_clusters(new_clusters)
    IO.inspect({count, evaluation})
    recursively_merge_clusters_n_times(count - 1, new_clusters)
  end
end
