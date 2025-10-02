# @param {Integer} num_bottles
# @param {Integer} num_exchange
# @return {Integer}
def max_bottles_drunk(num_bottles, num_exchange)
  full = num_bottles
  empty = 0
  drunk = 0
  while full > 0
    drunk += full
    empty += full
    full = 0
    while empty >= num_exchange
      empty -= num_exchange
      full += 1
      num_exchange += 1
    end
  end
  drunk
end
