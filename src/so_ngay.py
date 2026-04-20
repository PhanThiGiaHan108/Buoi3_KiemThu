def so_ngay(thang, nam):
    try:
        if thang < 1 or thang > 12:
            return "Không hợp lệ"

        if thang in [1,3,5,7,8,10,12]:
            return 31
        elif thang in [4,6,9,11]:
            return 30
        else:
            if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0):
                return 29
            return 28
    except:
        return "Lỗi dữ liệu"