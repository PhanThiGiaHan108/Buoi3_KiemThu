from src.chu_vi_hcn import chu_vi_hcn
from src.dien_tich_hcn import dien_tich_hcn
from src.pt_bac2 import giai_pt_bac2
from src.so_ngay import so_ngay
from src.so_nguyen_to import la_so_nguyen_to
from src.tong_xen_ke import tong_xen_ke
from src.ucln import ucln
from src.tong_giai_thua import tong_giai_thua

def test_chu_vi():
    assert chu_vi_hcn(5, 3) == 16

def test_dien_tich():
    assert dien_tich_hcn(5, 3) == 15

def test_pt_bac2():
    assert giai_pt_bac2(1, -3, 2) == (2.0, 1.0)

def test_so_ngay():
    assert so_ngay(2, 2024) == 29

def test_nguyen_to():
    assert la_so_nguyen_to(17) == True

def test_tong_xen_ke():
    assert tong_xen_ke(5) == 3

def test_ucln():
    assert ucln(6, 9) == 3

def test_tong_giai_thua():
    assert tong_giai_thua(3) == 9