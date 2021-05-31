class RobotGraphy :
    """ To check robot location on 5X4 grid map.
    Use iRobotLoc to determine exact cordinate of iRobot.
    Internally it use updateLocation to process data and
    retrun robot location.
    """

    def __init__(self, start, limit):
        self.start = start
        self.limit = limit

    def updateLocation(self, robot_loc, cmd, limit):

        if cmd == 'E'and robot_loc[1] < limit[1]:
            robot_loc = tuple( [robot_loc[0], robot_loc[1]+1, cmd])
            return robot_loc

        elif cmd == 'S' and robot_loc[0] < limit[0]:
            robot_loc = tuple( [robot_loc[0]+1, robot_loc[1], cmd])
            return robot_loc

        elif cmd == 'N' and robot_loc[0] < limit[0] and robot_loc[0] > 0:
            robot_loc = tuple( [robot_loc[0]-1, robot_loc[1], cmd])
            return robot_loc

        elif cmd == 'W' and robot_loc[1] < limit[1] and robot_loc[1] > 0:
            robot_loc = tuple( [robot_loc[0], robot_loc[1]-1, cmd])
            return robot_loc

        return robot_loc

    def iRobotLoc(self, commands):

        robot_loc = self.start

        for cmd in commands:
            if robot_loc[2] == cmd:
                continue

            elif cmd =='M':
                cmd = robot_loc[2]

            robot_loc = self.updateLocation(robot_loc, cmd, limit)

        return robot_loc

cmds = "MSMMEMMSESE"
cmds2 = "MSMMEMM"
start = (0, 0, 'S')
limit = (5, 4, 'M')

rg = RobotGraphy(start, limit)

rslt = rg.iRobotLoc(cmds)

print(rslt)
