from src.analytcs.DataFrame import DataFrame


if __name__ == "__main__":
    df = DataFrame(filename="storage/people.csv")
    print(df.get())
    print(df.find("Sex", "Male"))
    print(df.group_by(["Sex", "Age"]))
    print(df.order_by("Age", ascending=False))
