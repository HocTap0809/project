import heapq

class Node:
    def __init__(self, ten, chi_phi_g, chi_phi_h, cha=None):
        self.ten = ten
        self.chi_phi_g = chi_phi_g
        self.chi_phi_h = chi_phi_h
        self.chi_phi_f = chi_phi_g + chi_phi_h
        self.cha = cha

    def __lt__(self, other):
        return self.chi_phi_f < other.chi_phi_f

def thuat_toan_a_star(do_thi, bat_dau, ket_thuc, heuristic):
    danh_sach_mo = []
    danh_sach_dong = set()

    nut_bat_dau = Node(bat_dau, 0, heuristic[bat_dau])
    heapq.heappush(danh_sach_mo, nut_bat_dau)

    while danh_sach_mo:
        nut_hien_tai = heapq.heappop(danh_sach_mo)

        if nut_hien_tai.ten == ket_thuc:
            duong_di = []
            while nut_hien_tai:
                duong_di.append(nut_hien_tai.ten)
                nut_hien_tai = nut_hien_tai.cha
            return duong_di[::-1]

        danh_sach_dong.add(nut_hien_tai.ten)

        for nuoc_lanh_gieng, chi_phi in do_thi[nut_hien_tai.ten].items():
            if nuoc_lanh_gieng in danh_sach_dong:
                continue

            chi_phi_g = nut_hien_tai.chi_phi_g + chi_phi
            chi_phi_h = heuristic[nuoc_lanh_gieng]
            nut_moi = Node(nuoc_lanh_gieng, chi_phi_g, chi_phi_h, nut_hien_tai)

            co_the_them = True
            for nut in danh_sach_mo:
                if nut.ten == nuoc_lanh_gieng and nut.chi_phi_f <= nut_moi.chi_phi_f:
                    co_the_them = False
                    break

            if co_the_them:
                heapq.heappush(danh_sach_mo, nut_moi)

    return None

if __name__ == "__main__":
    do_thi = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    heuristic = {
        'A': 7,
        'B': 6,
        'C': 2,
        'D': 0
    }

    bat_dau = 'A'
    ket_thuc = 'D'

    ket_qua = thuat_toan_a_star(do_thi, bat_dau, ket_thuc, heuristic)
    if ket_qua:
        print(f"Đường đi ngắn nhất từ {bat_dau} đến {ket_thuc}: {' -> '.join(ket_qua)}")
    else:
        print(f"Không tìm được đường đi từ {bat_dau} đến {ket_thuc}")
