
"""Files tests simple file read related operations"""

class SimpleFile(object):
    """SimpleFile tests using file read api to do some simple math"""
    def __init__(self, file_path):
        self.numbers = []
        """
        TODO: reads the file by path and parse content into two
        dimension array (numbers)
        """
        f = open(file_path)
        holder = f.read()
        self.splitByRow = holder.split("\n")
        self.numbers = [space.split(' ') for space in self.splitByRow]

    def get_mean(self, line_number):
        """
        get_mean retrieves the mean value of the list by line_number (starts
        with zero)
        """
        return self.get_sum(line_number)/(1.0 * len(self.numbers[0]))
        
        
    
    def get_max(self, line_number):
        """
        get_max retrieves the maximum value of the list by line_number (starts
        with zero)
        """
        maximum = self.numbers[0][0]
        for x in self.numbers[line_number]:
            if(x > maximum):
                maximum = x
        return int(maximum)

    def get_min(self, line_number):
        """
        get_min retrieves the minimum value of the list by line_number (starts
        with zero)
        """
        minimum = self.numbers[0][0]
        
        for x in self.numbers[line_number]:
            if(x < minimum):
                minimum = x
        
        return int(minimum)

    def get_sum(self, line_number):
        """
        get_sum retrieves the sumation of the list by line_number (starts with
        zero)
        """
        mySum = 0
        for x in self.numbers[line_number]:
            mySum += int(x)

        return mySum
