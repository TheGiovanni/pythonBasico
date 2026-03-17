for i in range(30):
    if i < 1:
        print(f"Día {i + 1}: ${(2**i) / 100} Centavo de dólar")
    elif 1 <= i < 7:
        print(f"Día {i + 1}: ${(2**i) / 100} Centavos de dólar")
    else:
        if i == 29:
            total = (2**i) / 100
            print(f"Día {i + 1}: ${(2**i) / 100} dólares")
        else:
            print(f"Día {i + 1}: ${(2**i) / 100} dólares")