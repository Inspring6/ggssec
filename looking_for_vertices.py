import datetime
from itertools import takewhile
from itertools import product


class LookingForVertices():
    def __init__(self, image):
        self.image = image

    def Extract_put_rectangular(self):
        boundary_coordinates = [[]]
        for i1 in range(len(self.image)):
            for j1 in range(len(self.image[0])):
                if self.image[i1, j1] == 255:
                    boundary_coordinates.append([i1, j1])
                    break
            else:
                continue
            break
        for i2 in range(len(self.image)):
            for j2 in range(len(self.image[0]) - 1, 0, -1):
                if self.image[i2, j2] == 255:
                    boundary_coordinates.append([i2, j2])
                    break
            else:
                continue
            break
        for i3 in range(len(self.image) - 1, 0, -1):
            for j3 in range(len(self.image[0])):
                if self.image[i3, j3] == 255:
                    boundary_coordinates.append([i3, j3])
                    break
            else:
                continue
            break
        for i4 in range(len(self.image) - 1, 0, -1):
            for j4 in range(len(self.image[0]) - 1, 0, -1):
                if self.image[i4, j4] == 255:
                    boundary_coordinates.append([i4, j4])
                    break
            else:
                continue
            break
        return boundary_coordinates

    def Extract_circle(self):
        boundary_coordinates = [[]]
        for i1 in range(len(self.image)):
            for j1 in range(len(self.image[0])):
                if self.image[i1, j1] == 255:
                    break
            else:
                continue
            break
        for i2 in range(len(self.image)):
            for j2 in range(len(self.image[0]) - 1, 0, -1):
                if self.image[i2, j2] == 255:
                    break
            else:
                continue
            break
        ia = int((i1 + i2) / 2)
        ja = int((j1 + j2) / 2)
        boundary_coordinates.append([ia, ja])
        for i3 in range(len(self.image) - 1, 0, -1):
            for j3 in range(len(self.image[0])):
                if self.image[i3, j3] == 255:
                    break
            else:
                continue
            break
        for i4 in range(len(self.image) - 1, 0, -1):
            for j4 in range(len(self.image[0]) - 1, 0, -1):
                if self.image[i4, j4] == 255:
                    break
            else:
                continue
            break
        ib = int((i3 + i4) / 2)
        jb = int((j3 + j4) / 2)
        boundary_coordinates.append([ib, jb])
        for j5 in range(len(self.image[0])):
            for i5 in range(len(self.image)):
                if self.image[i5, j5] == 255:
                    break
            else:
                continue
            break
        for j6 in range(len(self.image[0])):
            for i6 in range(len(self.image) - 1, 0, -1):
                if self.image[i6, j6] == 255:
                    break
            else:
                continue
            break
        ic = int((i5 + i6) / 2)
        jc = int((j5 + j6) / 2)
        boundary_coordinates.append([ic, jc])
        for j7 in range(len(self.image[0]) - 1, 0, -1):
            for i7 in range(len(self.image)):
                if self.image[i7, j7] == 255:
                    break
            else:
                continue
            break
        for j8 in range(len(self.image[0]) - 1, 0, -1):
            for i8 in range(len(self.image) - 1, 0, -1):
                if self.image[i8, j8] == 255:
                    break
            else:
                continue
            break
        id = int((i7 + i8) / 2)
        jd = int((j7 + j8) / 2)
        boundary_coordinates.append([id, jd])
        return boundary_coordinates

    def Extract_polygon(self):
        boundary_coordinates = [[]]
        return boundary_coordinates

    def if_morethan255(self, i, j):
        if self.image[i, j] == 255:
            return False
        else:
            return True

    def Extract_sideway_rectangular_fast(self):
        boundary_coordinates = [[]]
        for i1, j1 in product(range(len(self.image)), range(len(self.image[0]))):
            if self.image[i1, j1] == 255: break
        for i2, j2 in product(range(len(self.image)), range(len(self.image[0]) - 1, 0, -1)):
            if self.image[i2, j2] == 255: break
        ia = int((i1 + i2) / 2)
        ja = int((j1 + j2) / 2)
        boundary_coordinates.append([ia, ja])
        for i3, j3 in product(range(len(self.image) - 1, 0, -1), range(len(self.image[0]))):
            if self.image[i3, j3] == 255: break
        for i4, j4 in product(range(len(self.image) - 1, 0, -1), range(len(self.image[0]) - 1, 0, -1)):
            if self.image[i4, j4] == 255: break
        ib = int((i3 + i4) / 2)
        jb = int((j3 + j4) / 2)
        boundary_coordinates.append([ib, jb])
        for j5, i5 in product(range(len(self.image[0])), range(len(self.image))):
            if self.image[i5, j5] == 255: break
        for j6, i6 in product(range(len(self.image[0])), range(len(self.image) - 1, 0, -1)):
            if self.image[i6, j6] == 255: break
        ic = int((i5 + i6) / 2)
        jc = int((j5 + j6) / 2)
        boundary_coordinates.append([ic, jc])
        for j7, i7 in product(range(len(self.image[0]) - 1, 0, -1), range(len(self.image))):
            if self.image[i7, j7] == 255: break
        for j8, i8 in product(range(len(self.image[0]) - 1, 0, -1), range(len(self.image) - 1, 0, -1)):
            if self.image[i8, j8] == 255: break
        id = int((i7 + i8) / 2)
        jd = int((j7 + j8) / 2)
        boundary_coordinates.append([id, jd])
        return boundary_coordinates

    def Extract_sideway_rectangular_slow(self):
        boundary_coordinates = [[]]
        for i1 in range(len(self.image)):
            for j1 in range(len(self.image[0])):
                if self.image[i1, j1] == 255:
                    break
            else:
                continue
            break
        for i2 in range(len(self.image)):
            for j2 in range(len(self.image[0]) - 1, 0, -1):
                if self.image[i2, j2] == 255:
                    break
            else:
                continue
            break
        ia = int((i1 + i2) / 2)
        ja = int((j1 + j2) / 2)
        boundary_coordinates.append([ia, ja])
        for i3 in range(len(self.image) - 1, 0, -1):
            for j3 in range(len(self.image[0])):
                if self.image[i3, j3] == 255:
                    break
            else:
                continue
            break
        for i4 in range(len(self.image) - 1, 0, -1):
            for j4 in range(len(self.image[0]) - 1, 0, -1):
                if self.image[i4, j4] == 255:
                    break
            else:
                continue
            break
        ib = int((i3 + i4) / 2)
        jb = int((j3 + j4) / 2)
        boundary_coordinates.append([ib, jb])
        for j5 in range(len(self.image[0])):
            for i5 in range(len(self.image)):
                if self.image[i5, j5] == 255:
                    break
            else:
                continue
            break
        for j6 in range(len(self.image[0])):
            for i6 in range(len(self.image) - 1, 0, -1):
                if self.image[i6, j6] == 255:
                    break
            else:
                continue
            break
        ic = int((i5 + i6) / 2)
        jc = int((j5 + j6) / 2)
        boundary_coordinates.append([ic, jc])
        for j7 in range(len(self.image[0]) - 1, 0, -1):
            for i7 in range(len(self.image)):
                if self.image[i7, j7] == 255:
                    break
            else:
                continue
            break
        for j8 in range(len(self.image[0]) - 1, 0, -1):
            for i8 in range(len(self.image) - 1, 0, -1):
                if self.image[i8, j8] == 255:
                    break
            else:
                continue
            break
        id = int((i7 + i8) / 2)
        jd = int((j7 + j8) / 2)
        boundary_coordinates.append([id, jd])
        return boundary_coordinates
