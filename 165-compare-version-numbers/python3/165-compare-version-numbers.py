class Solution:
  def compareVersion(self, version1: str, version2: str) -> int:
    ver1, ver2 = [[int(v) for v in x.split('.')] for x in [version1, version2]] 
    
    n = max(len(ver1), len(ver2))

    for i in range(n):
      v1 = ver1[i] if i < len(ver1) else 0
      v2 = ver2[i] if i < len(ver2) else 0

      if v1 == v2:
        continue
      return -1 if v1 < v2 else 1
    return 0
