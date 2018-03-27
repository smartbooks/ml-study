# encoding:utf-8
import csv

csv_data = csv.reader(open("data/simple.csv", encoding="utf-8"))

train_data = []
train_label_dist = {}
train_column = []
train_tree = {}
train_data_count = 0


# https://mp.weixin.qq.com/s?__biz=MjM5MTI3MzUwMA==&mid=2650011249&idx=1&sn=7a7eaedff252abe1eba7002b55c87027&chksm=bebf510289c8d81436ed24bc5a58cb7d835871545b13898a870b5e472f249de945c0192ea278&scene=0#rd

def train():
    for row in csv_data:
        if row[0].startswith("#"):
            train_column = [row[0].lstrip('#')]
            train_column.extend(row[1:])
        else:
            train_data.append(row)
            train_label_dist[row[0]] = row[0]

    train_data_count = len(train_data)

    expect_train_num = (len(train_column) - 1) * (len(train_column) - 1) * len(train_label_dist)
    if (train_data_count < expect_train_num):
        print("训练样本不足,模型拟合可能不是最优,当前样本%s,期望样本%s.\n" % (train_data_count, expect_train_num))

    for label in train_label_dist.keys():
        label_num = 0
        for columnIndex in range(len(train_column) - 1):
            column_name = train_column[columnIndex + 1]
            for d1 in train_data:
                column_count = 0
                for d2 in train_data:
                    if d1[0] == label and d1[0] == d2[0] and d1[columnIndex + 1] == d2[columnIndex + 1]:
                        column_count += 1
                if column_count > 0:
                    key = label + "|" + column_name + "|" + d1[columnIndex + 1]
                    train_tree[key] = column_count / train_data_count

        for d in train_data:
            if d[0] == label:
                label_num += 1

        train_tree[label] = label_num / train_data_count

    return train_tree, train_column


def pred(vector, column_meta):
    prop_rs = []
    for label in train_label_dist:
        prop = 1

        for column in range(len(column_meta) - 1):
            key = label + "|" + column_meta[column + 1] + "|" + vector[column]
            if (key in train_tree) == True:
                prop *= train_tree[key]
            else:
                prop *= 0.0000001

        prop *= train_tree[label]
        prop_rs.append([label, prop])

    prop_sum = 0
    for p in prop_rs:
        prop_sum += p[1]

    for p in prop_rs:
        p[1] = p[1] / prop_sum * 100

    return prop_rs


def run():
    model, column_meta = train()

    print("训练数据:", train_data, "\n")

    print("朴素贝叶斯概率表:", model, "\n")

    vector = ["30-40岁", "上海", "金融理财"]

    prop = pred(vector, column_meta)

    print("测试版本:", vector, "\n")

    print("预测概率(百分比):", prop)


run()
