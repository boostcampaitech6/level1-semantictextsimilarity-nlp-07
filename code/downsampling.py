import pandas as pd

df = pd.read_csv('../data/train.csv')

df_label_0 = df[df['label'] == 0]
df_label_0_sampled = df_label_0.sample(n=400, random_state=0)
df_label_not_0 = df[df['label'] != 0]
df_reduced = pd.concat([df_label_not_0, df_label_0_sampled]).reset_index(drop=True)
df_shuffled = df_reduced.sample(frac=1, random_state=0).reset_index(drop=True)

save_file_path = '../data/downsampled_train.csv'

df.to_csv(save_file_path, index=False)