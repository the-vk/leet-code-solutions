# @param {String[]} strs
# @return {Integer}
def maximum_value(strs)    
  strs.map { |x| x.match?(/^\d+$/) ? x.to_i : x.length }.max
end