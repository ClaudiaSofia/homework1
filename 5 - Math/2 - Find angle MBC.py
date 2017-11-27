# -*- coding: utf-8 -*-

import math
AB = int(input())
BC = int(input())
hyp=math.hypot(AB,BC)
res=round(math.degrees(math.acos(BC/hyp)))
print(str(int(res))+'°')