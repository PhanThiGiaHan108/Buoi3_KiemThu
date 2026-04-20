def chu_vi_hcn(a, b):
    try:
        if a <= 0 or b <= 0:
            return "Không hợp lệ"
        return 2 * (a + b)
    except:
        return "Lỗi dữ liệu"