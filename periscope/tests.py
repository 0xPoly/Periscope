class NetTest:
    '''
    NetTest represents a test that periscope runs. Each NetTest is
    assigned a 'riskLevel' between 1 and 5 - were 1 is the safest
    and 5 is the most dangerous.
    '''
    def __init__(self):
        self.name = ''
        self.riskLevel = 5
        self.description = ''

class TestManager:
    '''
    All NetTest Objects are managed here
    '''
    def __init__(self):
        self.testList = \
        [['Official Website Probe', 1, 'Detect whether TorProject.org and mirrors are Accessible'],
        ['Directory Authorities', 2,'Try to download consensus from the Tor Directory Authorities'],
        ['Relays', 3, 'Attempt to connect to relays'],
        ['Bridges',4, 'Attempt to connect to bridges'],
        ['PCAP',5, 'Record network packets if censorship detected']]
        self.NetTestList = []

        for test in self.testList:
            x = NetTest()
            x.name = test[0]
            x.riskLevel = test[1]
            x.description = test[2]
            self.NetTestList.append(x)

    def netTestsByRisk(self, riskLevel):
        '''returns a list of NetTests at or below the specificed risk level'''
        self.availableTests = []
        for test in self.NetTestList:
            if  test.riskLevel <= int(riskLevel):
               self.availableTests.append(test)
        return self.availableTests


