
def cheese_shop(kind, *args, **kwargs):
    print("Normal argument")
    print(kind)

    print("\n")

    for arg in args:
        print(arg)

    print("List of arguments")
    for arg in args:
        print(arg)

    print("\n")

    # list of keywords
    print("List of key:value pair ")
    for kw in kwargs:
        print(kw, ":", kwargs[kw])


   


cheese_shop("limburger","kenya", "uganda", comment="its very runny sir", good="its really rainy", shop_keepr ="Micheal")