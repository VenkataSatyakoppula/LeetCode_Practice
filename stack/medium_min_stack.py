class MinStack(object):

    def __init__(self):
        self.mini = []
        self.stack_data = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack_data.append(val)
        val = min(val,self.mini[-1] if self.mini else val)
        self.mini.append(val)

    def pop(self):
        """
        :rtype: None
        """
        self.stack_data.pop()
        self.mini.pop()

        

    def top(self):
        """
        :rtype: int
        """
        return self.stack_data[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.mini[-1]
