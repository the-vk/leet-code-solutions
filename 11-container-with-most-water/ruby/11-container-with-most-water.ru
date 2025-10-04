# @param {Integer[]} height
# @return {Integer}
def max_area(height)
  ans = l = 0
  r = height.length - 1
  while r > l
    ans = [ans, [height[l], height[r]].min * (r - l)].max
    if height[l] > height[r]
      r -= 1
    else
      l += 1
    end
  end
  ans
end
