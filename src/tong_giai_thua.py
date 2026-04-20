def giai_thua(n):
    if n == 0:
        return 1
    return n * giai_thua(n - 1)

def tong_giai_thua(n):
    try:
        if n < 0:
            return "Không hợp lệ"
        s = 0
        for i in range(1, n+1):
            s += giai_thua(i)
        return s
    except:
        return "Lỗi dữ liệu"