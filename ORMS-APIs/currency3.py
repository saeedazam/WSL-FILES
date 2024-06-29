import requests

def main():
    base = input("First currency: ")
    other = input("Second currency: ")
    res = requests.get("https://api.fixer.io/latest",
                        params={"base": base, "symbols": other})
    if res.status_code != 200:
        raise Exception("Error: API request failed.")
    data = res.json()
    rate = data["rates"][other]
    print(f"1 {base} is equal to {rate} {other}")

if __name__ == "__main__":
    main()
