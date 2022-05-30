import sys

sys.stdout = open('eval_input.txt', 'w')

import random


for _ in range(50):

    data = ''
    # 스펙의 범위
    spec_num = random.randint(7, 10)
    cost = random.randint(10,100)
    data += str(cost)
    data += '\n'
    data += str(spec_num)
    data += '\n'

    for s in range(spec_num):
        data += str(random.randint(1, 10))
        data += ' '

    data += '\n'

    comp_num = random.randint(5, 10)
    data += str(comp_num)
    data += '\n'

    sample_list = list()
    for i in range(spec_num):
        sample_list.append(i)

    for c in range(comp_num):
        # 회사 당 요구 스펙 정의
        per_comp_spec = random.randint(2, spec_num)

        data += ' '.join([str(x) for x in random.sample(sample_list, per_comp_spec)])
        if c != comp_num-1:
            data += '\n'

    print(data)
sys.stdout.close()