def totalDigitsOfNumber(n):
    total = 0;
    giai_thua =1;

    while (n > 0):
        i= n%10
        for i in range(2, n + 1):
                   giai_thua = giai_thua * i;
        total = total + giai_thua;
        n = int(n / 10);
    return total;


n = int(input("Nhập số nguyên dương n = "));
print("Tổng giai thua các chữ số của", n, "là", totalDigitsOfNumber(n));
