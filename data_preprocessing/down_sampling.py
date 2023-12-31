import pandas as pd


def down_sample(config, data_name="train_path"):
    df = pd.read_csv(config["your_path"]+config["process_paths"][data_name])
    df_label_0 = df[df['label'] == 0]
    df_label_0_sampled = df_label_0.sample(n=400, random_state=0)
    df_label_not_0 = df[df['label'] != 0]
    df_reduced = pd.concat([df_label_not_0, df_label_0_sampled]).reset_index(drop=True)
    df_down = df_reduced.sample(frac=1, random_state=0).reset_index(drop=True)

    return df_down