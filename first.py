# https://www.cnblogs.com/dragonir/p/6224313.html
# maze
import numpy as np
net = np.array([[-1, -1, -1, -1, 0, -1], [-1, -1, -1, 0, -1, 100], [-1 , -1, -1, 0, -1, -1], [-1, 0, 0, -1, 0, -1], [0, -1, -1, 0, -1, 100], [-1, 0, -1, -1, 0, 100]])
# 代表了即时reward值
# 创建初始Q矩阵
q_tab=np.zeros((6, 6), int)
initial_state = 0
gamma = 0.8
for i in range(10000):
    current_state = initial_state
    # 选择可行的动作,用action_num来记录当前状态可采取的动作数
    action_num = 0
    action_list = []
    for j in range(6):
        if net[current_state][j] >= 0:
            action_num += 1
            action_list.append(j)
    rand_act = action_list[np.random.randint(0, action_num)]
    # 下面进入了状态 rand_act,选取rand_act状态下对应q值最大的动作
    q_max = 0
    index = 0
    for l in range(6):
        if q_tab[rand_act][l] >= q_max:
            q_max = q_tab[rand_act][l]
            index = l
    # 选取了最大的q_NextState_AllActions对应的最大的q值，并用index指出了其在q表中的位置
    # 更新q表
    if rand_act == 5 :
        q_tab[current_state][rand_act]=100
    else:
        q_tab[current_state][rand_act] = net[current_state][rand_act] + gamma * q_max
    initial_state = rand_act
    print("-"*20,"\n")
    print("q_table of the %d iteration" %i)
    print("\n", q_tab)


print("**"*10,"\n",q_tab)