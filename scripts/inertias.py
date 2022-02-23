def cylinder(m,h,r):
    '''inputs: mass, height and radius.
    Output: Inertias of the diagonal [ixx, iyy,izz]'''
    ixx = (1/12)*m*(3*r**2 + h**2)
    iyy = (1/12)*m*(3*r**2 + h**2)
    izz = (1/12)*m*r**2
    return [ixx, iyy, izz]

def box(m,x,y,z):
    '''inputs: mass, x, y, z
    Output: Inertias of the diagonal [ixx, iyy,izz]'''
    ixx = (1/12)*m*(y**2 + z**2)
    iyy = (1/12)*m*(x**2 + z**2)
    izz = (1/12)*m*(x**2 + y**2)
    return [ixx, iyy, izz]