物流中心货运问题
----------------

#### 主要流程及进展

1. 根据载重量和客户所需货物量，选出单车运输可选的客户组合。 done

    注：每一个方案是一个客户集合
2. 对每一个客户组合中的客户进行排序，根据到达时间要求，选出可行的运输序列。

    1. 给出特定客户组合的全排列，使用 itertools, done
    2. 对于一个序列，判断是否可行。

3. 对所有可行运输序列，计算运行路径，获取最佳方案


#### 判断序列是否可行

关键在于按时到达
