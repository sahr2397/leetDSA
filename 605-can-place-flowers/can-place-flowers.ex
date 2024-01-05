defmodule Solution do
  @spec can_place_flowers(flowerbed :: [integer], n :: integer) :: boolean
  def can_place_flowers(flowerbed, n) do
    chunks = Enum.chunk_every([0] ++ flowerbed ++ [0], 3, 1, :discard)
    solve(chunks, n)
  end

  defp solve(_, 0), do: true

  defp solve([], _), do: false

  defp solve([_], n) when n > 1, do: false

  defp solve([[0,0,0]], 1), do: true

  defp solve([[0, 0, 0], h2 | rest], n) do
    solve([[1 | tl(h2)] | rest], n - 1)
  end

  defp solve([_ | rest], n), do: solve(rest, n)
end