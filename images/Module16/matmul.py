import numpy as np
import matplotlib.pyplot as plt

def get_randmat(M, N):
    A = np.random.rand(M, N)*10
    A = np.array(np.round(A), dtype=int)
    return A

def draw_mat_row(A, x0, y0, row, fac = 0.5):
    for y in range(A.shape[0]):
        for x in range(A.shape[1]):
            c = 'C0'
            if y == row:
                c = 'C1'
            plt.text(fac*x+x0, fac*y+y0, "{}".format(A[y, x]), color=c)

def draw_mat_col(A, x0, y0, col, fac = 0.5):
    for y in range(A.shape[0]):
        for x in range(A.shape[1]):
            c = 'C0'
            if x == col:
                c = 'C1'
            plt.text(fac*x+x0, fac*y+y0, "{}".format(A[y, x]), color=c)

def draw_mat_elem(A, x0, y0, row, col, fac = 0.5):
    for y in range(A.shape[0]):
        for x in range(A.shape[1]):
            if A[y, x] > -1:
                c = 'C0'
                if y == row and x == col:
                    c = 'C1'
                plt.text(fac*x+x0, fac*y+y0, "{}".format(A[y, x]), color=c)



def make_mulanim(M, K, N, fac=0.5, seed=0):
    np.random.seed(seed)
    A = get_randmat(M, K)
    B = get_randmat(K, N)
    AB = -1*np.ones((M, N), dtype=int)
    idx = 0
    for i in range(M):
        for j in range(N):
            plt.clf()
            AB[i, j] = np.sum(A[i, :]*B[:, j])
            s = ""
            for k in range(A.shape[1]):
                s += "{}*{}".format(A[i, k], B[k, j])
                if k < A.shape[1]-1:
                    s += "+"
            s += " = {}".format(AB[i, j])
            draw_mat_row(A, 0, 1, i, fac)
            plt.text(fac*(A.shape[1]+0.5), 1+fac*A.shape[0]/5, "x")
            draw_mat_col(B, (A.shape[1]+2)*fac, 1, j, fac)
            plt.text((A.shape[1]+B.shape[1]+2)*fac, 1+fac*A.shape[0]/5, "=")
            draw_mat_elem(AB, (A.shape[1]+B.shape[1]+4)*fac, 1, i, j, fac)
            plt.xlim([0, fac*(A.shape[1]+B.shape[1]+AB.shape[1]+4)])
            plt.ylim([0, (max(A.shape[0], B.shape[0])+1)*fac+1])
            plt.gca().invert_yaxis()
            plt.axis("off")
            plt.title(s)
            plt.savefig("{}.png".format(idx), dpi=150)
            idx += 1

#make_mulanim(5, 3, 4, 1)

make_mulanim(2, 4, 3, 1, 2)