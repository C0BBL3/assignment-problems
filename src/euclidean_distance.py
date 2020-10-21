import math

arr = [[ 1 , 'Shortbread'  ,     0.14     ,       0.14     ,      0.28     ,     0.44      ],
[ 2  , 'Shortbread'  ,     0.10     ,       0.18     ,      0.28     ,     0.44      ],
[ 3  , 'Shortbread'  ,     0.12     ,       0.10     ,      0.33     ,     0.45      ],
[ 4  , 'Shortbread'  ,     0.10     ,       0.25     ,      0.25     ,     0.40      ],
[ 5  , 'Sugar'       ,     0.00     ,       0.10     ,      0.40     ,     0.50      ],
[ 6  , 'Sugar'       ,     0.00     ,       0.20     ,      0.40     ,     0.40      ],
[ 7  , 'Sugar'       ,     0.10     ,       0.08     ,      0.35     ,     0.47      ],
[ 8  , 'Sugar'       ,     0.00     ,       0.05     ,      0.30     ,     0.65      ],
[ 9  , 'Fortune'     ,     0.20     ,       0.00     ,      0.40     ,     0.40      ],
[ 10 , 'Fortune'     ,     0.25     ,       0.10     ,      0.30     ,     0.35      ],
[ 11 , 'Fortune'     ,     0.22     ,       0.15     ,      0.50     ,     0.13      ],
[ 12 , 'Fortune'     ,     0.15     ,       0.20     ,      0.35     ,     0.30      ],
[ 13 , 'Fortune'     ,     0.22     ,       0.00     ,      0.40     ,     0.38      ]]
def dist(arr_1, arr_2): return math.sqrt(sum([(value-arr_2[i]) ** 2 for i, value in enumerate(arr_1)]))
print([dist([0.1,0.15,0.3,0.45], bad[2:]) for bad in arr])

