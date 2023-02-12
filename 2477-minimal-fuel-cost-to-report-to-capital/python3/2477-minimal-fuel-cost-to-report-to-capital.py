class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
      nodes = {}
      for c1, c2 in roads:
        e = nodes.get(c1, set())
        e.add(c2)
        nodes[c1] = e
        e = nodes.get(c2, set())
        e.add(c1)
        nodes[c2] = e
      return self.visit(nodes, 0, seats)[1]

    def visit(self, nodes, n, seats):
      down = []
      for c in nodes.get(n, set()):
        nodes.get(c).remove(n)
        down.append(self.visit(nodes, c, seats))
      
      rep = 1
      fuel = 0
      
      for r_rep, r_fuel in down:
        rep += r_rep
        fuel += r_fuel
      
      if n != 0:
        fuel += math.ceil(rep/seats)
      
      res = (rep, fuel)
      return res
