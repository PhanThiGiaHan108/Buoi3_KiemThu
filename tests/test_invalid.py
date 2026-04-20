from src.chu_vi_hcn import chu_vi_hcn
from src.dien_tich_hcn import dien_tich_hcn
from src.pt_bac2 import giai_pt_bac2
from src.so_ngay import so_ngay
from src.so_nguyen_to import la_so_nguyen_to
from src.tong_xen_ke import tong_xen_ke
from src.ucln import ucln
from src.tong_giai_thua import tong_giai_thua

def test_chu_vi_invalid():
    assert chu_vi_hcn(-1, 3) == "Không hợp lệ"

def test_dien_tich_invalid():
    assert dien_tich_hcn(0, 3) == "Không hợp lệ"

def test_pt_bac2_invalid():
    assert giai_pt_bac2(0, 2, 1) == "Không phải PT bậc 2"

def test_so_ngay_invalid():
    assert so_ngay(13, 2023) == "Không hợp lệ"

def test_nguyen_to_invalid():
    assert la_so_nguyen_to(-5) == False

def test_tong_xen_ke_invalid():
    assert tong_xen_ke(0) == "Không hợp lệ"

def test_ucln_invalid():
    assert ucln(0, 0) == "Không xác định"

def test_tong_giai_thua_invalid():
    assert tong_giai_thua(-1) == "Không hợp lệ"