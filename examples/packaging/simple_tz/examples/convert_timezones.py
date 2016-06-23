"""
An example of converting timezones
"""

from simple_tz import tz

def test_simple_tz_na_timezones():
    """Convert EST to/from PST"""
    ny_time = '2016-01-01 18:00:00'
    bc_time = '2016-01-01 15:00:00'

    ny_to_bc = tz.convert(ny_time, from_tz='EST', to_tz='PST')
    bc_to_ny = tz.convert(bc_time, from_tz='PST', to_tz='EST')

    if ny_to_bc == bc_time:
       print('They are the same time') 

test_simple_tz_na_timezones()
