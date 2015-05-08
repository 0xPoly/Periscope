class NetTest:
    '''
    NetTest represents a test that periscope runs. Each NetTest is
    assigned a 'riskLevel' between 1 and 5 - were 1 is the least risky
    and 5 is the most risky..
    '''
    def __init__(self):
        self.name = ''
        self.riskLevel = 5
        self.description = ''

class TestManager:
    '''
    All NetTest Objects are managed here
    '''
    # Short Name, Risk Level, Description
    testList = [['Official Website Probe', 1, 'Detect whether TorProject.org is Accessible'],
                ['Directory Authorities', 2,
                'Try to download consensus from the Tor Directory Authorities']]
    NetTestList = []

    def __init__(self):
        for test in self.testList:
            x = NetTest()
            x.name = test[0]
            x.riskLevel = test[1]
            x.description = test[2]
            NetTestList.append(x)

    def netTestsByRisk(self, riskLevel):
        '''returns a list of NetTests at or below the specificed risk level'''
        availableTests = []
        for test in self.NetTestList:
            if  test.risklevel <= riskLevel:
               self.availableTests.append(test)
        return availableTests


