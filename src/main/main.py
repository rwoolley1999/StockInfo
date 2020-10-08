from src.services.GetService import GetService

def main():
    print("Starting application...")

    getServiceObj = GetService()

    getServiceObj.getService()

    print("Ending application...")

if __name__ == '__main__':
    main()
