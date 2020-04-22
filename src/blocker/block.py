import pandas as pd
import numpy as np

def block(left_tuples, right_tuples):
    df_left = pd.read_json(left_tuples)
    df_right = pd.read_json(right_tuples)

    block_factor = 1

    df_left.rename(columns='l_{}'.format, inplace=True)
    df_right.rename(columns='r_{}'.format, inplace=True)

    df_left["block_factor"] = np.random.randint(0, block_factor, df_left.shape[0])
    df_right["block_factor"] = np.random.randint(0, block_factor, df_right.shape[0])

    of = df_left.merge(df_right, left_on="block_factor", right_on="block_factor")
    of = of[['l_name', 'r_name']]
    of = of[of.apply(lambda x: jaccard_score(ngrams(x['l_name'],3),ngrams(x['r_name'],3)) > 0.7, axis=1)]

    return of

def ngrams(inp, n):
    output = []
    if len(inp) < 3:
        output.append(inp)
    for i in range(len(inp)-n+1):
        output.append(inp[i:i+n])
    output = [''.join(x) for x in output]
    return output

def jaccard_score(list1, list2):
    intersection = len(list(set(list1).intersection(list2)))
    union = (len(list1) + len(list2)) - intersection
    return float(intersection) / union
