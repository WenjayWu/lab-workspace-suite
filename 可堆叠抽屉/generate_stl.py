"""
可堆叠抽屉 STL 生成脚本
使用纯 Python 生成 ASCII STL，无需第三方依赖。
单位：毫米 (mm)

设计参数：
  外宽 300mm x 外深 200mm x 盒高 70mm
  壁厚 3mm
  面板 304mm x 82mm x 4mm，带拉手
  堆叠卡槽：顶部凹槽深3mm，底部凸脊高2.5mm
"""

import os, math

# ── 尺寸参数 ──────────────────────────────────────────────
W  = 300.0   # 外宽
D  = 200.0   # 外深
HB = 70.0    # 盒体高度
HP = 82.0    # 面板高度
T  = 3.0     # 壁厚
PT = 4.0     # 面板厚度
HD = 15.0    # 拉手深度
HH = 8.0     # 拉手高度
HW = 100.0   # 拉手宽度
SD = 3.0     # 堆叠卡槽深度
SI = 8.0     # 卡槽内缩
RH = 2.5     # 底部凸脊高度


class Vec3:
    __slots__ = ('x', 'y', 'z')
    def __init__(self, x=0, y=0, z=0):
        self.x, self.y, self.z = float(x), float(y), float(z)
    def __sub__(self, o):  return Vec3(self.x-o.x, self.y-o.y, self.z-o.z)
    def __xor__(self, o):  # cross product
        return Vec3(self.y*o.z - self.z*o.y,
                     self.z*o.x - self.x*o.z,
                     self.x*o.y - self.y*o.x)
    def normalized(self):
        l = math.sqrt(self.x**2 + self.y**2 + self.z**2) or 1
        return Vec3(self.x/l, self.y/l, self.z/l)

class Triangle:
    __slots__ = ('v1', 'v2', 'v3', 'n')
    def __init__(self, v1, v2, v3):
        self.v1, self.v2, self.v3 = v1, v2, v3
        self.n = (v2 - v1) ^ (v3 - v1)

class MeshBuilder:
    def __init__(self):
        self.triangles = []

    def add_quad(self, v1, v2, v3, v4):
        self.triangles.append(Triangle(v1, v2, v3))
        self.triangles.append(Triangle(v1, v3, v4))

    def add_box(self, x, y, z, w, h, d):
        x0, x1 = x - w/2, x + w/2
        y0, y1 = y, y + h
        z0, z1 = z - d/2, z + d/2
        v = [
            Vec3(x0,y0,z0), Vec3(x1,y0,z0), Vec3(x1,y1,z0), Vec3(x0,y1,z0),
            Vec3(x0,y0,z1), Vec3(x1,y0,z1), Vec3(x1,y1,z1), Vec3(x0,y1,z1),
        ]
        self.add_quad(v[0], v[1], v[2], v[3])  # front  -Z
        self.add_quad(v[5], v[4], v[7], v[6])  # back   +Z
        self.add_quad(v[4], v[0], v[3], v[7])  # left   -X
        self.add_quad(v[1], v[5], v[6], v[2])  # right  +X
        self.add_quad(v[3], v[2], v[6], v[7])  # top    +Y
        self.add_quad(v[4], v[5], v[1], v[0])  # bottom -Y

    def export_stl(self, path, name="mesh"):
        with open(path, 'w') as f:
            f.write(f"solid {name}\n")
            for t in self.triangles:
                n = t.n.normalized()
                f.write(f"  facet normal {n.x} {n.y} {n.z}\n")
                f.write("    outer loop\n")
                for v in (t.v1, t.v2, t.v3):
                    f.write(f"      vertex {v.x} {v.y} {v.z}\n")
                f.write("    endloop\n")
                f.write("  endfacet\n")
            f.write(f"endsolid {name}\n")
        print(f"  -> {path} ({len(self.triangles)} triangles)")


def build_drawer_box():
    m = MeshBuilder()
    # bottom
    m.add_box(0, 0, 0, W, T, D)
    # back wall
    m.add_box(0, T, 0, W, HB, T)
    # left wall
    m.add_box(-W/2+T/2, T, 0, T, HB, D-T)
    # right wall
    m.add_box(W/2-T/2, T, 0, T, HB, D-T)

    slotW = W - SI*2
    slotD = D - SI*2
    # top stacking groove (border ridge around top edge)
    m.add_box(0, HB+T, -D/2+T+slotD/2, slotW, SD, T)
    m.add_box(0, HB+T, D/2-T-slotD/2, slotW, SD, T)
    m.add_box(-W/2+T/2, HB+T, 0, T, SD, slotD)
    m.add_box(W/2-T/2, HB+T, 0, T, SD, slotD)

    # bottom stacking ridges
    m.add_box(0, -RH, -D/2+T+slotD/2, slotW-1, RH, T-0.5)
    m.add_box(0, -RH, D/2-T-slotD/2, slotW-1, RH, T-0.5)
    m.add_box(-W/2+T/2, -RH, 0, T-0.5, RH, slotD)
    m.add_box(W/2-T/2, -RH, 0, T-0.5, RH, slotD)

    return m


def build_panel():
    m = MeshBuilder()
    pw = W + 4
    ph = HP
    # front panel face
    m.add_box(0, 0, D/2 + PT/2, pw, ph, PT)

    # handle bar
    m.add_box(0, ph/2 - HH/2, D/2 + PT + HD/2, HW, HH, HD)
    # handle supports
    sw = 6
    m.add_box(-HW/2+8, ph/2 - HH/2, D/2 + PT + HD/2, sw, HH, HD)
    m.add_box(HW/2-8, ph/2 - HH/2, D/2 + PT + HD/2, sw, HH, HD)

    return m


def build_assembly():
    m = MeshBuilder()
    box = build_drawer_box()
    panel = build_panel()
    m.triangles.extend(box.triangles)
    m.triangles.extend(panel.triangles)
    return m


def main():
    out_dir = os.path.dirname(os.path.abspath(__file__))

    print("生成可堆叠抽屉 STL 文件...")
    print("尺寸: 300x200x80mm, 壁厚3mm")

    m1 = build_drawer_box()
    m1.export_stl(os.path.join(out_dir, "抽屉盒.STL"), "drawer_box")

    m2 = build_panel()
    m2.export_stl(os.path.join(out_dir, "抽屉面板.STL"), "drawer_panel")

    m3 = build_assembly()
    m3.export_stl(os.path.join(out_dir, "可堆叠抽屉-整体.STL"), "drawer_assembly")

    print("\n完成！共生成3个STL文件，可直接导入切片软件进行3D打印。")


if __name__ == "__main__":
    main()
