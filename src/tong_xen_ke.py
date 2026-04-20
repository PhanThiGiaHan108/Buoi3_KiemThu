def tong_xen_ke(n):
    try:
        if n <= 0:
            return "Không hợp lệ"
        s = 0
        for i in range(1, n+1):
            if i % 2 == 0:
                s -= i
            else:
                s += i
        return s
    except:
        return "Lỗi dữ liệu"