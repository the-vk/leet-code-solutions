# @param {Integer} n
# @return {Boolean}
def is_ugly(n)
    return false if n == 0
    [2, 3, 5].each do |f|
      while n % f == 0
        n = n / f
      end
    end
    n == 1
end