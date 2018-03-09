import numpy as np

def matrix_to_values(matrix):
    diags = [matrix[::-1,:].diagonal(i) for i in range(-matrix.shape[0]+1,matrix.shape[1])]
    diags.extend(matrix.diagonal(i) for i in range(matrix.shape[1]-1,-matrix.shape[0],-1))
    (ret_row_b, ret_row_w) = count_lines(matrix)
    (ret_col_b, ret_col_w) = count_lines(matrix.transpose())
    (ret_diag_b, ret_diag_w) = count_lines(diags)
    ret_b = [x + y + z for (x, y), z in zip(zip(ret_row_b, ret_col_b), ret_diag_b)]
    ret_w = [x + y + z for (x, y), z in zip(zip(ret_row_w, ret_col_w), ret_diag_w)]
    ret_b[0] = ret_b[0]//4
    ret_w[0] = ret_w[0]//4
    return (ret_b, ret_w)


def count_lines(rows):
    ret_b = [0,0,0,0,0,0,0,0,0,0,0]
    ret_w = [0,0,0,0,0,0,0,0,0,0,0]
    cur_b = 0
    cur_w = 0
    for row in rows:
        threat_lvl_b = 1
        threat_lvl_w = 1
        for value in row:
            if value == 1:
                ret_b[0] = ret_b[0] + 1
                cur_b = cur_b + 1
                if cur_w > 1:
                    i = select_index(cur_w, threat_lvl_w + 1)
                    ret_w[i] = ret_w[i] + 1
                cur_w = 0
                threat_lvl_w = 1
            elif value == 2:
                ret_w[0] = ret_w[0] + 1
                cur_w = cur_w + 1
                if cur_b > 1:
                    i = select_index(cur_b, threat_lvl_b + 1)
                    ret_b[i] = ret_b[i] + 1
                cur_b = 0
                threat_lvl_b = 1
            else:
                if cur_w > 1:
                    i = select_index(cur_w, threat_lvl_w)
                    ret_w[i] = ret_w[i] + 1
                if cur_b > 1:
                    i = select_index(cur_b, threat_lvl_b)
                    ret_b[i] = ret_b[i] + 1
                cur_w = 0
                cur_b = 0
                threat_lvl_b = 0
                threat_lvl_w = 0
        if cur_w > 1:
            i = select_index(cur_w, threat_lvl_w + 1)
            ret_w[i] = ret_w[i] + 1
        if cur_b > 1:
            i = select_index(cur_b, threat_lvl_b + 1)
            ret_b[i] = ret_b[i] + 1
        cur_w = 0
        cur_b = 0
        threat_lvl_b = 0
        threat_lvl_w = 0
    return (ret_b, ret_w)

def select_index(cur, threat_lvl):
    if cur > 4:
        return 10
    else:
        return 3*(cur-2) + threat_lvl + 1

def test_it():
    matrix2 =  np.array([[1,0,2,1,0],
                [1,1,0,2,2],
                [1,2,0,0,0],
                [1,0,1,2,0]])
    print(matrix2)
    print(matrix_to_values(matrix2))
