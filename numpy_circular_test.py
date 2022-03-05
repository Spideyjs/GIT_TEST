import numpy as np


m = 32  # 源数据长度
m1 = np.uint8(np.random.randint(8, size=m))
row_length = 8
column_length = int(m/row_length)
j = 2  # 循环移位位数


mG_former = np.reshape(m1, (column_length, row_length))
mG_latter = np.zeros([column_length, 1], np.uint8)
mG = np.c_[mG_former, mG_latter]


# 对mG进行循环移位操作
mG1 = mG[..., -j:]
mG2 = mG[..., :-j-1]

# 方法1：移位后先转成单行数据流再拼接
m_circl1_former = np.reshape(mG1, (1, j*column_length))
m_circl1_latter = np.reshape(mG2, (1, (row_length - j)*column_length))
m_circl1_1 = np.c_[m_circl1_former, m_circl1_latter]

# 方法2：移位后先拼接转再成单行数据流
mG3 = np.c_[mG1, mG2]
m_circl1_2 = np.reshape(mG3, (1, m))

# print(m1)
print(mG)
# print(mG1)
# print(mG2)
print(mG3)
print(m_circl1_former)
print(m_circl1_latter)
print(m_circl1_1)
print(m_circl1_2)
