import csv
from src.analytcs.collection import Collection


if __name__ == "__main__":
    collection = Collection(filename="storage/people.csv")

    results = collection.get()
    print(results)
    results.to_csv("results/get_results.csv", index=False, quoting=csv.QUOTE_ALL)

    find = collection.find("sex", "Male")
    print(find)
    find.to_csv("results/filter_results.csv", index=False, quoting=csv.QUOTE_ALL)

    group = collection.group_by(["sex", "age"])
    print(group)
    group.to_csv("results/group_results.csv", index=False, quoting=csv.QUOTE_ALL)

    order = collection.order_by(
        "age", arrange=["id", "age", "sex", "name"], ascending=False
    )
    print(order)
    order.to_csv("results/order_results.csv", index=False, quoting=csv.QUOTE_ALL)
