defmodule Smoketest do
  @moduledoc """
  Documentation for `Smoketest`.
  """

  # require OtherModule
  @doc """
  Hello world.

  ## Examples
      iex> Smoketest.hello()
      :world

  """
  def hello do
  OtherModule.myfoo()
  :baz = OtherModule.baz(67)

    :world
  end
end
