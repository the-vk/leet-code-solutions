# @param {Integer[][]} points
# @return {Integer}
def max_width_of_vertical_area(points)
  points = points.map {|v| v[0] }.sort
  area = Array.new(points.length - 1) { 0 }
  (0...area.length).each do |i|
    area[i] = points[i+1] - points[i]
  end
  area.max
end
