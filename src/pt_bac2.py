import math

def giai_pt_bac2(a, b, c):
    try:
        if a == 0:
            return "Không phải PT bậc 2"
        delta = b*b - 4*a*c
        if delta < 0:
            return "Vô nghiệm"
        elif delta == 0:
            return -b / (2*a)
        else:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            return (x1, x2)
    except:
        return "Lỗi dữ liệu"