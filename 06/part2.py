import math

# We want to find: 
# t_hold * t - t_hold^2 = d_min
# --> 
# t_hold = 1/2 * (t - sqrt(t^2 - 4*d_min))
# t_hold = 1/2 * (t + sqrt(t^2 - 4*d_min))

def find_t_hold_limits(t_max, d_min):
    t_hold_min = math.floor(0.5 * (t_max - (t_max**2 - 4 * d_min)**0.5) + 1)
    t_hold_max = math.ceil(0.5 * (t_max + (t_max**2 - 4 * d_min)**0.5) - 1)
    assert t_hold_min > 0
    assert t_hold_min <= t_hold_max
    return t_hold_min, t_hold_max

def run_on_input():
    t_max, d_min = (46857582, 208141212571410)
    t_hold_min, t_hold_max = find_t_hold_limits(t_max, d_min)
    n_ways = t_hold_max - t_hold_min + 1
    print(n_ways)
    
run_on_input()