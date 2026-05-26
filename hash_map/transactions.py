'''
transactions
comma sep string name,time(min),city

invalid:
"alice,50,sf"
"alice,60,ny"

2 transactions with the same name that are 60 or less apart in different cities

return array of strings
'''

def get_invalid_transasctions(transactions: list[str]) -> list[str]:
    res = []

    transactions.sort()

    cur_user = ""
    invalid_transacts = set()

    def add_invalids():
        for i in invalid_transacts:
            res.append(transactions[i])

    for i, transact_str in enumerate(transactions):
        user, time, city= transact_str.split(",")
        time = int(time)
        if user != cur_user and invalid_transacts:
            add_invalids()
            invalid_transacts = set()

        j = i - 1
        while j >= 0 and transactions[j].split(",")[0] == user:
            _, compare_time, compare_city = transactions[j].split(",")
            compare_time = int(compare_time)
            if compare_city == city or abs(compare_time-time) >= 60:
                j -= 1
                continue

            invalid_transacts.add(i)
            invalid_transacts.add(j)

            j -= 1 

    if invalid_transacts:
        add_invalids()
        invalid_transacts = set()

    return res


def main():
    transacts = ["alice,110,ny","alice,120,sf","ben,10,clt", "ben,20,sf"]
    print(get_invalid_transasctions(transacts))

if __name__ == "__main__":
    main()
