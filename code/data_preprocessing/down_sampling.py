import pandas as pd


def down_sample(config):
    train_df = pd.read_csv(config["paths"]["train_path"])

    df_label_0 = train_df[train_df['label'] == 0]
    df_label_0_sampled = df_label_0.sample(n=400, random_state=0)
    df_label_not_0 = train_df[train_df['label'] != 0]
    df_reduced = pd.concat([df_label_not_0, df_label_0_sampled]).reset_index(drop=True)

    df = df_reduced.sample(frac=1, random_state=0).reset_index(drop=True)

    return df