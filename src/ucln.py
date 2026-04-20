def ucln(a, b):
    try:
        if a == 0 and b == 0:
            return "Không xác định"
        while b != 0:
            a, b = b, a % b
        return abs(a)
    except:
        return "Lỗi dữ liệu"