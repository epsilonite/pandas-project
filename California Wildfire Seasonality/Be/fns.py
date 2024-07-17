# Dependencies
import math as m
import shapely as shp

# Haversine distance equation
def haversine_distance(x1,y1,x2,y2):
    r = 6371 # mean radius of earth in km
    n = 1 - m.cos(m.radians(y2-y1)) + m.cos(m.radians(y1))*m.cos(m.radians(y2))*(1-m.cos(m.radians(x2-x1)))
    return 2*r *m.asin(m.sqrt(n/2))

def acre2km2(n):
    return 0.00404685642*n

def haversine_bearing(x,y,d,a):
    R = 6371 # mean radius of earth in km
    lat = m.asin( m.sin(m.radians(y))*m.cos(d/6371) + m.cos(m.radians(y))*m.sin(d/R)*m.cos(a) )
    lon = m.radians(x) + m.atan2( m.sin(a)*m.sin(d/R)*m.cos(m.radians(y)), m.cos(d/R) - m.sin(m.radians(y))*m.sin(lat) )
    return [(m.degrees(lon)+540)%360-180,m.degrees(lat)]

def polycircle(x,y,r):
    coords = []
    for i in range(0,16):
        p = shp.geometry.Point(haversine_bearing(x,y,r,i*m.pi/8))
        coords.append((p.x, p.y))
    return shp.geometry.Polygon(coords)

def polysquare(x,y,r,s):
    return shp.geometry.box( (x-r)/s, (y-r)/s, (x+r)/s, (y+r)/s )

def box_radius(arr):
    return haversine_distance(arr[0],arr[1],arr[2],arr[3])/2

def roundby(x,n,r=0):
    return (round(n*x+r)-r)/n

def GPMindex(x1,x2):
    return round(10*(x1-x2))

def GPMcoord():
    lon = [x/100 for x in range(-12445,-11405+5,10)]
    lat = [y/100 for y in range(3245,4205+5,10)]
    return [lon,lat]

def CAbounds(i=None):
    x1 = -124.482003000119
    x2 = -114.131210999644
    y1 = 32.5288320002052
    y2 = 42.0095030001829
    if i == None:
        return [x1,y1,x2,y2]
    elif i == 0:
        return [int(roundby(x1-10**(-i)/2,10**i)),
                int(roundby(y1-10**(-i)/2,10**i)),
                int(roundby(x2+10**(-i)/2,10**i)),
                int(roundby(y2+10**(-i)/2,10**i))]
    else:
        return [roundby(x1-10**(-i)/2,10**i),
                roundby(y1-10**(-i)/2,10**i),
                roundby(x2+10**(-i)/2,10**i),
                roundby(y2+10**(-i)/2,10**i)]