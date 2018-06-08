from geoProject import *
import localization as lx


print('localization entry')


'''
Currently three modes are supported:
1-2D
2-3D
3-Earth1

Also three solvers can be utilized:
1-LSE for least square error
2-LSE_GC for least square error with geometric constraints.
    Geometric constraints force the solutions to be in the intersection areas of all multilateration circles.
3- CCA for centroid method, i.e., the solution will be the centroid of the intersection area.
    If no common intersection area exist, the area with maximum overlap is used.

'''

MODE= '2D'
SOLVER= 'LSE'


P=lx.Project(mode=MODE,solver=SOLVER)


'''
To add anchors to the project use:

P.add_anchor(<name>,<loc>)

where name denote user provided label of the anchor
    and <loc> is the location of the anchor provided in tuple, e.g., (120,60).
'''

anchors = [('first', 0, 0), ('second', 9, 0), ('third', 0, 9), ('fourth', 9, 9)]

for a in range(len(anchors)):
    P.add_anchor(anchors[a][0], (anchors[a][1], anchors[a][2]))


'''
To add target use:

t,label=P.add_target()

t is the target object and label is the package provided label for the target.

Distance measurements must be added to target object like:

t.add_measure(<anchor_label>,<measured_distance>)
'''

targets = {'able': [('first', 4.242), ('second', 8.485), ('third', 6.708), ('fourth',8.485)],
            'baker': [('first',8.485), ('second', 6.708), ('third', 6.708), ('fourth',4.242)],
            'charlie': [('first', 9.486), ('second', 3.0), ('third', 10.816), ('fourth',6)],
            'delta': [('first', 4.242), ('second', 6.708), ('third', 12.369), ('fourth',13.416)],
            'echo': [('first', 4.242), ('second', 12.369), ('third', 6.708), ('fourth',13.416)]}

for k, v in targets.items():
    t,label=P.add_target()
    print('added ' + k + ' and target ' + label)

    # print(targets[k], ' ', len(targets[k]))
    for tt in range(len(v)):
        d = v[tt]
        t.add_measure(d[0],d[1])
        

    P.solve()
    print(label)
    print(t.loc)

print('Done')

'''
Finally running P.solve() will locate all targets. You can access the estimated location of the target t by t.loc.
t.loc is a point object. Point object B has "x","y","z" coordinates available by B.x, B.y, B.z respectively.
'''



# end of file