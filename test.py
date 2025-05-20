import requests

def main():
    print("== Exercise Search ==")
    search = input("Search term (or leave empty): ").strip()
    sort = input("Sort by (asc/desc or leave empty): ").strip()

    params = {}
    if search:
        params['search'] = search
    if sort:
        params['sort'] = sort

    try:
        response = requests.get("http://localhost:5001/exercises", params=params)
        print("\n== Results ==\n")
        print(response.text)
    except requests.exceptions.RequestException as e:
        print("Failed to contact the microservice.")
        print(e)

if __name__ == "__main__":
    main()