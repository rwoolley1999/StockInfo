import yfinance as yf

class GetCompany:

    def getCompany(self):
        company_name = input("Enter company name: ")
        print("Finding the information for " + company_name)

        #TODO: WEBSCRAPER TO FIND TICKER NAME FROM COMPANY NAME

        ticker = yf.Ticker(company_name)

        return ticker

    def list(self):
        print("List of services:")
        print("a - Historical data")
        print("b - Company information")
        print("c - Major Holders")
        service = input("Please enter the letter of which service you require: ")
        return service

        return service
