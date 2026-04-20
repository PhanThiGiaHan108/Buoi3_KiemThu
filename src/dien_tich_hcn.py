def dien_tich_hcn(a, b):
    try:
        if a <= 0 or b <= 0:
            return "Không hợp lệ"
        return a * b
    except:
        return "Lỗi dữ liệu"