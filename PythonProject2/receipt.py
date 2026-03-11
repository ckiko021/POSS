def generate_receipt(cart, total):

    with open("receipt.txt", "w") as f:

        f.write("PYTHON POS RECEIPT\n")
        f.write("----------------------\n")

        for item in cart:
            name, price = item
            f.write(f"{name} - {price}\n")

        f.write("----------------------\n")
        f.write(f"TOTAL: {total}\n")

    print("Receipt generated")