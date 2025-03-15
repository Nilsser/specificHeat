#error of delta-t
def delta_t(d_temp_g, d_init_temp):
    return (d_temp_g**2 + d_init_temp**2)**0.5

#error of gradient T'
def gradient(d_temp_2, t_2, t_start, d_temp_g,):
    return ((d_temp_2/(t_2-t_start))**2 + (d_temp_g/(t_2-t_start))**2 )**0.5

#error of Integral F
def f(t_g,t_start,delta_t_g,d_delta_t):
    return (t_g-t_start) * (delta_t_g**2 + d_delta_t**2)**0.5


def c_tot(energy_input,gradient,integral,delta_t_g,d_delta_t,d_gradient,d_integral):
    return (
    (
        energy_input * (gradient * integral - delta_t_g**2) / (delta_t_g**2 - gradient * integral)**2 * d_delta_t
    )**2
    + (
        integral * energy_input * delta_t_g * d_gradient / (delta_t_g**2 - gradient * integral)**2
    )**2
    + (
        gradient * energy_input * delta_t_g * d_integral / (delta_t_g**2 - gradient * integral)**2
    )**2
    )**0.5

def probe(d_c_tot,d_c_add):
    return (d_c_tot**2 + d_c_add**2)**0.5

def c_m(meta,c_probe,d_m,d_c_probe):
    return ( 
    (-meta['M']*c_probe*  d_m  /(meta['weight'])**2)**2
    +
    (meta['M']/meta['weight']*d_c_probe)**2 
    )**0.5