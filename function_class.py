import numpy as np
import matplotlib.pyplot as plt
import copy
import math


class polygon_block_meshing:
    def __init__(self, plots, m, n):
        self.plots = plots
        self.m = m
        self.n = n
        # self.k = k
        self.ctem_num = m * n

    def mesh(self, k):
        m = self.m
        n = self.n
        # plots = self.plots
        plots = self.group()
        arrx = np.random.random((m, n))
        arry = np.random.random((m, n))

        arrx[0] = np.linspace(plots[0][0], plots[1][0], m)
        arry[0] = np.linspace(plots[0][1], plots[1][1], n)
        for j in range(0, m):
            arrx[j][-1] = np.linspace(plots[1][0], plots[2][0], m)[j]
            arry[j][-1] = np.linspace(plots[1][1], plots[2][1], n)[j]

        arrx[-1][:] = np.linspace(plots[3][0], plots[2][0], m)
        arry[-1][:] = np.linspace(plots[3][1], plots[2][1], n)
        for j in range(0, m):
            arrx[j][0] = np.linspace(plots[0][0], plots[3][0], m)[j]
            arry[j][0] = np.linspace(plots[0][1], plots[3][1], n)[j]

        self.iteration(arrx, arry, k)
        self.picture(arrx, arry)
        jiedian_infor = np.vstack((arrx, arry))
        return jiedian_infor

    def group(self):
        plots = rank(self.plots)
        return plots

    def iteration(self, arx, ary, k):

        canshu = 0

        n = arx.shape[0]
        m = arx.shape[1]
        # print(arx.shape)
        # print(n, m)
        a = np.random.random((n, m))
        r = np.random.random((n, m))

        # 绘制动态图
        fig = plt.figure()
        plt.title('error')

        ax = fig.add_subplot(1, 1, 1)
        ax.set_title('title test', fontsize=12, color='r')

        plt.xlabel('迭代次数')
        plt.ylabel('error')

        y1 = []
        x1 = []

        for z in range(0, k * 100):

            arx_before = copy.deepcopy(arx[1:n - 1, 1:m - 1])
            ary_before = copy.deepcopy(ary[1:n - 1, 1:m - 1])

            for i in range(1, n - 1):
                for j in range(1, m - 1):
                    a[i][j] = ((arx[i][j + 1] - arx[i][j - 1]) ** 2 + (ary[i][j + 1] - ary[i][j - 1]) ** 2) / 4
                    r[i][j] = ((arx[i + 1][j] - arx[i - 1][j]) ** 2 + (ary[i + 1][j] - ary[i - 1][j]) ** 2) / 4
                    arx[i][j] = 1 / (2 * (a[i][j] + r[i][j])) * (
                            a[i][j] * (arx[i + 1][j] + arx[i - 1][j]) + r[i][j] * (arx[i][j + 1] + arx[i][j - 1]))
                    ary[i][j] = 1 / (2 * (a[i][j] + r[i][j])) * (
                            a[i][j] * (ary[i + 1][j] + ary[i - 1][j]) + r[i][j] * (ary[i][j + 1] + ary[i][j - 1]))

            # 判断迭代收敛，终止循环
            arx_precision = abs((arx_before - arx[1:n - 1, 1:m - 1]) / arx_before)
            ary_precision = abs((ary_before - ary[1:n - 1, 1:m - 1]) / ary_before)

            # arx_precision.mean()
            # ary_precision.mean()

            print(arx_precision.mean(), ary_precision.mean())
            if arx_precision.max() < 0.0001 and ary_precision.max() < 0.0001:
                canshu += 1

            if z != 0:
                y1.append((arx_precision.max() + ary_precision.max()) / 2)
                x1.append(z)
                ax.cla()  # 清除键
                ax.bar(x1, label='error', height=y1, width=1)
                ax.legend()
                plt.pause(0.001)

            if canshu == 1:
                print(z)
                break

        return arx, ary

    def picture(self, arx, ary):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        plt.plot(arx, ary, color='r')
        plt.plot(np.transpose(arx), np.transpose(ary), color='b')
        plt.show()


class ellipse_block_meshing:
    def __init__(self, center, plot_long, b, n, m):
        self.center = center
        self.plot_long = plot_long
        self.a = math.sqrt((center[0] - plot_long[0]) ** 2 + (center[1] - plot_long[1]) ** 2)
        self.b = b
        self.n = n
        self.m = m

    def iteration(self, arx, ary, k):
        n = arx.shape[0]
        m = arx.shape[1]
        a = np.random.random((n, m))
        r = np.random.random((n, m))

        fig = plt.figure()
        plt.title('error')

        ax = fig.add_subplot(1, 1, 1)
        ax.set_title('title test', fontsize=12, color='r')

        y1 = []
        x1 = []

        for z in range(0, k * 100):
            arx_before = copy.deepcopy(arx[1:n - 1, 1:m - 1])
            ary_before = copy.deepcopy(ary[1:n - 1, 1:m - 1])
            for i in range(1, n - 1):
                for j in range(1, m - 1):
                    a[i][j] = ((arx[i][j + 1] - arx[i][j - 1]) ** 2 + (ary[i][j + 1] - ary[i][j - 1]) ** 2) / 4
                    r[i][j] = ((arx[i + 1][j] - arx[i - 1][j]) ** 2 + (ary[i + 1][j] - ary[i - 1][j]) ** 2) / 4
                    arx[i][j] = 1 / (2 * (a[i][j] + r[i][j])) * (
                            a[i][j] * (arx[i + 1][j] + arx[i - 1][j]) + r[i][j] * (arx[i][j + 1] + arx[i][j - 1]))
                    ary[i][j] = 1 / (2 * (a[i][j] + r[i][j])) * (
                            a[i][j] * (ary[i + 1][j] + ary[i - 1][j]) + r[i][j] * (ary[i][j + 1] + ary[i][j - 1]))

            # 判断迭代收敛，终止循环
            arx_precision = abs((arx_before - arx[1:n - 1, 1:m - 1]) / arx_before)
            ary_precision = abs((ary_before - ary[1:n - 1, 1:m - 1]) / ary_before)

            # arx_precision.mean()
            # ary_precision.mean()
            y1.append((arx_precision.max() + ary_precision.max()) / 2)
            x1.append(z)
            ax.cla()  # 清除键
            ax.bar(x1, label='error', height=y1, width=1)
            ax.legend()
            plt.pause(0.001)
            # print(arx_precision.mean(),ary_precision.mean())
            if arx_precision.max() < 0.001 and ary_precision.max() < 0.001:
                print(arx_precision.max())
                print(ary_precision.max())
                break

        return arx, ary

    def mesh(self, k):
        r2 = 0
        center, a, b = self.center, self.a, self.b
        n = self.n
        m = self.m
        arrx = np.linspace(-a, b, m * n).reshape(m, n) + center[0]
        arry = np.linspace(0, b, m * n).reshape(m, n) + center[1]
        for i in range(0, m):
            if i == 0:
                for j in range(0, n):
                    jiaodu = np.pi / (n - 1) * j
                    arrx[i][j] = np.cos(jiaodu) * a + center[0]
                    arry[i][j] = np.sin(jiaodu) * b + center[1]
            elif i == m - 1:
                for j in range(0, n):
                    jiaodu = np.pi / (n - 1) * j
                    arrx[i][j] = np.cos(jiaodu) * r2 + center[0]
                    arry[i][j] = np.sin(jiaodu) * r2 + center[1]
            else:
                arrx[i][0] = (a - r2) / (m - 1) * (m - 1 - i) + r2 + center[0]
                arry[i][0] = 0 + center[1]
                arrx[i][n - 1] = -(a - r2) / (m - 1) * (m - 1 - i) - r2 + center[0]
                arry[i][n - 1] = 0 + center[1]
        arx, ary = ellipse_block_meshing.iteration(self, arrx, arry, k)
        ellipse_block_meshing.picture(self, arx, ary)
        arx = np.vstack((arx, arx))
        ary = np.vstack((ary, 2 * center[1] - ary))
        jiedian_infor = np.vstack((arx, ary))
        return jiedian_infor

    def picture(self, arx, ary):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        arx_ = arx
        ary_ = 2 * self.center[1] - ary
        plt.plot(arx, ary, color='r')
        plt.plot(arx_, ary_, color='r')
        plt.plot(np.transpose(arx), np.transpose(ary), color='b')
        plt.plot(np.transpose(arx_), np.transpose(ary_), color='b')
        plt.show()


# 迭代
def iteration(arx, ary):
    n = arx.shape[0]
    m = arx.shape[1]
    a = np.random.random((n, m))
    r = np.random.random((n, m))
    for k in range(0, 100):
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                a[i][j] = ((arx[i][j + 1] - arx[i][j - 1]) ** 2 + (ary[i][j + 1] - ary[i][j - 1]) ** 2) / 4
                r[i][j] = ((arx[i + 1][j] - arx[i - 1][j]) ** 2 + (ary[i + 1][j] - ary[i - 1][j]) ** 2) / 4
                arx[i][j] = 1 / (2 * (a[i][j] + r[i][j])) * (
                        a[i][j] * (arx[i + 1][j] + arx[i - 1][j]) + r[i][j] * (arx[i][j + 1] + arx[i][j - 1]))
                ary[i][j] = 1 / (2 * (a[i][j] + r[i][j])) * (
                        a[i][j] * (ary[i + 1][j] + ary[i - 1][j]) + r[i][j] * (ary[i][j + 1] + ary[i][j - 1]))
    return (arx, ary)


def rank(plots):
    plots = np.array(plots)
    center = plots.mean(axis=0)
    jiaodu = np.ones((plots.shape[0], 1), dtype='f')
    for i in range(0, plots.shape[0]):
        if (plots[i][1] > center[1]) and (plots[i][0] > center[0]):
            jiaodu[i] = np.arctan((center[1] - plots[i][1]) / (center[0] - plots[i][0]))
        elif (plots[i][1] > center[1]) & (plots[i][0] < center[0]):
            jiaodu[i] = np.arctan(abs((center[1] - plots[i, 1]) / (center[0] - plots[i, 0]))) + np.pi / 2
        elif (plots[i][1] < center[1]) & (plots[i][0] < center[0]):
            jiaodu[i] = np.arctan(abs((center[1] - plots[i, 1]) / (center[0] - plots[i, 0]))) + np.pi / 2 * 2
        elif (plots[i][1] < center[1]) & (plots[i][0] > center[0]):
            jiaodu[i] = np.arctan(abs((center[1] - plots[i, 1]) / (center[0] - plots[i, 0]))) + np.pi / 2 * 3
        elif plots[i][0] == center[0] and plots[i][1] > center[1]:
            jiaodu[i] = 0
        elif plots[i][0] == center[0] and plots[i][1] < center[1]:
            jiaodu[i] = np.pi
        elif plots[i][1] == center[1] and plots[i][0] > center[0]:
            jiaodu[i] = np.pi / 2
        elif plots[i][1] == center[1] and plots[i][0] < center[0]:
            jiaodu[i] = np.pi * 3 / 2
    plot = plots[np.argsort(jiaodu, axis=0)]
    plot_sque = np.squeeze(plot)
    return plot_sque


def block(plots):
    # plots = np.array(plots)
    num_plots = np.shape(plots)[0]
    if num_plots == 4:
        num_group = 1
        return plots, num_group
    elif num_plots % 2 == 0 and num_plots != 4:
        num_group = int((num_plots - 4) / 2 + 1)
        group_plots_init = plots[:4].copy()
        for i in range(1, num_group):
            group_plots_transient = np.array([plots[0], plots[2 * i + 1], plots[2 * i + 2], plots[2 * i + 3]])
            group_plots_transient = np.vstack((group_plots_init, group_plots_transient))
            group_plots_init = group_plots_transient.copy()
        group_plots_init = group_plots_init.reshape((num_group, 4, 2))
        return group_plots_init, num_group
    elif num_plots % 2 != 0:
        num_group = int((num_plots + 1 - 4) / 2 + 1)
        group_plots_init = plots[:4].copy()
        if num_group > 2:
            for i in range(1, num_group - 2):
                group_plots_transient = np.array([plots[0], plots[2 * i + 1], plots[2 * i + 2], plots[2 * i + 3]])
                group_plots_transient = np.vstack((group_plots_init, group_plots_transient))
                group_plots_init = group_plots_transient.copy()
            plots = np.array([plots[0], plots[-4], plots[-3], plots[-2], plots[-1]])
            ploti = (plots[2] + plots[3]) / 2
            group_plots_transient = np.array([plots[0], plots[1], plots[2], ploti])
            group_plots_transient = np.vstack((group_plots_init, group_plots_transient))
            group_plots_init = group_plots_transient.copy()
            group_plots_transient = np.array([plots[0], ploti, plots[2], plots[4]])
            group_plots_transient = np.vstack((group_plots_init, group_plots_transient))
            group_plots_init = group_plots_transient.copy()
            group_plots_init = group_plots_init.reshape((num_group, 4, 2))
            return group_plots_init, num_group
        else:
            ploti = (plots[2] + plots[3]) / 2
            group_plots_init = np.array([plots[0], plots[1], plots[2], ploti])
            group_plots_transient = np.array([plots[0], ploti, plots[3], plots[4]])
            group_plots_transient = np.vstack((group_plots_init, group_plots_transient))
            group_plots_init = group_plots_transient.copy()
            group_plots_init = group_plots_init.reshape((num_group, 4, 2))
            return group_plots_init, num_group


def ementqulity(arx, ary):
    x_areas = np.array([])
    y_areas = np.array([[]])
    for j in range(0, arx.shape[0] - 1):
        x_areas = np.array([])
        for i in range(0, arx.shape[1] - 1):
            print(i)
            a = np.sqrt((arx[j][i] - arx[j][i + 1]) ** 2 + (ary[j][i] - ary[j][i + 1]) ** 2)
            c = np.sqrt((arx[j + 1][i] - arx[j + 1][i + 1]) ** 2 + (ary[j + 1][i] - ary[j + 1][i + 1]) ** 2)
            b = np.sqrt((arx[j + 1][i] - arx[j][i]) ** 2 + (ary[j + 1][i] - ary[j][i]) ** 2)
            d = np.sqrt((arx[j + 1][i + 1] - arx[j][i + 1]) ** 2 + (ary[j + 1][i + 1] - ary[j][i + 1]) ** 2)
            e = np.sqrt((arx[j][i] - arx[j + 1][i + 1]) ** 2 + (ary[j][i] - ary[j + 1][i + 1]) ** 2)
            f = np.sqrt((arx[j][i + 1] - arx[j + 1][i]) ** 2 + (ary[j][i + 1] - ary[j + 1][i]) ** 2)
            tem_x_areas = np.sqrt(4 * e ** 2 * f ** 2 - (a ** 2 - b ** 2 + c ** 2 - d ** 2) ** 2) / 4
            x_areas = np.hstack((x_areas, tem_x_areas))
            # print(tem_x_areas)

        if j == 0:
            areas = copy.copy(x_areas)
        else:
            areas = np.vstack((areas, x_areas))

        # print('1')
    return areas


# 图形重绘
def drawing(jiedian):
    arx = jiedian[:int(jiedian.shape[0] / 2)]
    ary = jiedian[int(jiedian.shape[0] / 2):]
    plt.plot(arx, ary, color='r')
    plt.plot(np.transpose(arx), np.transpose(ary), color='b')
    plt.show()
