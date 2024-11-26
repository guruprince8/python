class DataSet:
    """
        Class used to load the names data set by state
        Link https://www.ssa.gov/oact/babynames/limits.html used a reference point
    """
    def __init__(self):
        self.filepath = "/Users/guru/Desktop/professional/Datasets/namesbystate/"
        self.files = {
            "AK": self.filepath + "AK.TXT",
            "AL": self.filepath + "AL.TXT"
        }

    def getnamesbystate(self, state_name: str, apply_sort: bool):
        """
        Function to load names dataset by state
        :param state_name:
        :param apply_sort:
        :return:
        """
        names = []
        try:
            file = open(self.files[state_name])
            for line in file:
                split = line.split(",")
                names.append(split[3])
        except Exception as e:
            print("Error is", e)
        return names
