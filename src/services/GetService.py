from input.GetCompany import GetCompany

class GetService:

    def __init__(self):
        self.getCompanyObj = GetCompany()

    def getService(self):
        ticker = self.getCompanyObj.getCompany()
        if self.getCompanyObj.list() == "a":
            period_data = input("Please enter the period data is required (e.g. 1mo, max): ")
            hist = ticker.history(period=period_data)
            print(hist)
        elif self.getCompanyObj.list() == "b":
            info = ticker.info
            print(info)
        elif self.getCompanyObj.list() == "c":
            holders = ticker.major_holders
            print(holders)
        else:
            print("Please enter a valid service letter")
            # change this to an exception
