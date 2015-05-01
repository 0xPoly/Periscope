class NetTest:
    '''
    NetTest represents a test that periscope runs. Each NetTest is
    assigned a 'riskLevel' between 0 and 5 - were 0 is the least risky
    and 5 is the most risky..
    '''
    def __init__(self, riskLevel):
        self.riskLevel = riskLevel
