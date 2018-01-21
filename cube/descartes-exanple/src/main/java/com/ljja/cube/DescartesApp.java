package com.ljja.cube;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * 参考链接:
 * http://blog.csdn.net/buptdavid/article/details/45918647
 * https://www.cnblogs.com/zhijianliutang/archive/2012/02/16/2355058.html
 * <p>
 * 宽表结构:
 * [事实],[度量],[地区维度],[时间维度],[类别维度],[机型维度]
 * tid,price,[sum,count,avg,max,min,mean,std],[国家,省份,城市,区县],[时,日,周,月,季,年],[一级分类,二级分类,三级分类,四级分类],[机型]
 * <p>
 * 计算过程:
 * cube_cubeid:
 * 000000001_000000001:price_sum,price_count,price_avg,price_max,price_min,price_mean,price_std
 * 000000001_000000002:price_sum,price_count,price_avg,price_max,price_min,price_mean,price_std
 * 000000001_000000003:price_sum,price_count,price_avg,price_max,price_min,price_mean,price_std
 * <p>
 * 查询过程:
 * SELECT price_sum,price_avg FROM cube WHERE 省份='北京' AND 年份=2017 AND 一级分类='水果'
 * <p>
 * 分解过程A:
 * key LIKE 'cube%hash("2017")%hash("北京")%hash("水果")%'
 * <p>
 * 分解过程B:
 * table_name:cube + dim_column
 */
public class DescartesApp {

    public static void main(String[] args) {
        List<String> list1 = new ArrayList<>();
        list1.add("国家");
        list1.add("省份");
        list1.add("城市");
        list1.add("区县");

        List<String> list2 = new ArrayList<>();
        list2.add("时");
        list2.add("日");
        list2.add("周");
        list2.add("月");
        list2.add("季");
        list2.add("年");

        List<String> list3 = new ArrayList<>();
        list3.add("一级分类");
        list3.add("二级分类");
        list3.add("三级分类");
        list3.add("四级分类");

        List<String> list4 = new ArrayList<>();
        list4.add("机型");

        List<List<String>> dimValue = new ArrayList<>();
        dimValue.add(list1);
        dimValue.add(list2);
        dimValue.add(list3);
        dimValue.add(list4);

        List<List<String>> recursiveResult = new ArrayList<>();
        // 递归实现笛卡尔积
        recursive(dimValue, recursiveResult, 0, new ArrayList<>());

        System.out.println("递归实现笛卡尔乘积: 共 " + recursiveResult.size() + " 个结果");
        for (List<String> list : recursiveResult) {
            for (String string : list) {
                System.out.print(string + "|");
            }
            System.out.println();
        }

        //List<List<String>> circulateResult = new ArrayList<>();
        //circulate(dimValue, circulateResult);
        //System.out.println("循环实现笛卡尔乘积: 共 " + circulateResult.size() + " 个结果");
        //for (List<String> list : circulateResult) {
        //    for (String string : list) {
        //        System.out.print(string + " ");
        //    }
        //    System.out.println();
        //}
    }

    /**
     * 递归实现dimValue中的笛卡尔积，结果放在result中
     *
     * @param dimValue 原始数据
     * @param result   结果数据
     * @param layer    dimValue的层数
     * @param curList  每次笛卡尔积的结果
     */
    private static void recursive(List<List<String>> dimValue, List<List<String>> result, int layer, List<String> curList) {
        if (layer < dimValue.size() - 1) {
            if (dimValue.get(layer).size() == 0) {
                recursive(dimValue, result, layer + 1, curList);
            } else {
                for (int i = 0; i < dimValue.get(layer).size(); i++) {
                    List<String> list = new ArrayList<String>(curList);
                    list.add(dimValue.get(layer).get(i));
                    recursive(dimValue, result, layer + 1, list);
                }
            }
        } else if (layer == dimValue.size() - 1) {
            if (dimValue.get(layer).size() == 0) {
                result.add(curList);
            } else {
                for (int i = 0; i < dimValue.get(layer).size(); i++) {
                    List<String> list = new ArrayList<>(curList);
                    list.add(dimValue.get(layer).get(i));
                    result.add(list);
                }
            }
        }
    }

    /**
     * 循环实现dimValue中的笛卡尔积，结果放在result中
     *
     * @param dimValue 原始数据
     * @param result   结果数据
     */
    private static void circulate(List<List<String>> dimValue, List<List<String>> result) {
        int total = 1;
        for (List<String> list : dimValue) {
            total *= list.size();
        }
        String[] myResult = new String[total];

        int itemLoopNum = 1;
        int loopPerItem = 1;
        int now = 1;
        for (List<String> list : dimValue) {
            now *= list.size();

            int index = 0;
            int currentSize = list.size();

            itemLoopNum = total / now;
            loopPerItem = total / (itemLoopNum * currentSize);
            int myIndex = 0;

            for (String ignored : list) {
                for (int i = 0; i < loopPerItem; i++) {
                    if (myIndex == list.size()) {
                        myIndex = 0;
                    }

                    for (int j = 0; j < itemLoopNum; j++) {
                        myResult[index] = (myResult[index] == null ? "" : myResult[index] + ",") + list.get(myIndex);
                        index++;
                    }
                    myIndex++;
                }

            }
        }

        List<String> stringResult = Arrays.asList(myResult);
        for (String string : stringResult) {
            String[] stringArray = string.split(",");
            result.add(Arrays.asList(stringArray));
        }
    }

}
