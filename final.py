import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def get_max_lap(df: pd.DataFrame) -> pd.DataFrame:
    """
    get the number of laps in each race
    (use positionOrder == 1 and stop == 1)
    :param df: input dataframe
    :return: processed dataframe
    """
    return df[(df['positionOrder'] == 1) & (df['stop'] == 1)].reset_index(drop=True)[['raceId', 'year', 'laps']]


def count_proportion(df_pit: pd.DataFrame, df_race: pd.DataFrame) -> pd.DataFrame:
    """
    add column with the proportion during the total laps in each race
    :param df_pit: pit dataframe
    :param df_race: race dataframe
    :return:
    """
    df_new = df_pit.merge(df_race[['raceId', 'laps']], on='raceId', how='left', suffixes=('_once', '_total'))
    df_new['proportion'] = round(df_new['lap'] / df_new['laps'], 1)
    return df_new


def read_data(file):
    """
    this function is used to turn csv file into dataframe
    :param file: input csv file name
    :return: dataframe of the input csv file
    """
    df = pd.read_csv(file)
    return df


def delete_data(df, column, value):
    """
    this function is used to delete rows in dataframe if column equals to the given value
    :param df: input dataframe that need to delete specific columns
    :param column: columns used to check whether the row should be deleted
    :param value: input value that row will be deleted if contains it
    :return: dataframe that specific columns are deleted
    >>> df = pd.DataFrame({"position":["1","2","4","5"],"stop":[1,2,3,4]})
    >>> delete_data(df, "position", "5")
      position  stop
    0        1     1
    1        2     2
    2        4     3
    """
    index_name = df[df[column] == value].index
    df.drop(index=index_name, inplace=True)
    return df


def get_total_pitstop(pitstop_table):
    """
    this function is used to get total pit stop
    :param pitstop_table: input dataframe that need to find the total pit stop rows
    :return: dataframe that only contains the total pit stop of each driver and race
    >>> df = pd.DataFrame({"raceId":[1,1,1],"driverId":[1,1,1], "stop":[1,2,3]})
    >>> get_total_pitstop(df)
      raceId driverId stop
    0      1        1    3
    """
    pitstop_df = pd.DataFrame(columns=["raceId","driverId","stop"])
    for line in range(0,len(pitstop_table)):
        df_stop = pitstop_df.loc[(pitstop_df["raceId"] == int(pitstop_table.loc[line, "raceId"])) & (pitstop_df["driverId"] == int(pitstop_table.loc[line, "driverId"])), ["stop"]]
        if len(df_stop) > 0:
            stop_list = df_stop.values.tolist()
            if int(pitstop_table.loc[line, "stop"]) > stop_list[0][0]:
                pitstop_df.loc[(pitstop_df["raceId"] == int(pitstop_table.loc[line, "raceId"])) & (pitstop_df["driverId"] == int(pitstop_table.loc[line, "driverId"])), "stop"] = int(pitstop_table.loc[line, "stop"])
        else:
            pitstop_df = pitstop_df.append(
                {"raceId": int(pitstop_table.loc[line, "raceId"]), "driverId": int(pitstop_table.loc[line, "driverId"]),
                 "stop": int(pitstop_table.loc[line, "stop"])}, ignore_index=True)
    return pitstop_df


def join_table(table_a, table_b, key_list):

    joined_table = table_a.merge(table_b, on=key_list)
    return joined_table


def turn_column_num(df, column):
    df[column] = df[column].astype(int)
    return df


if __name__ == '__main__':
    pitstops_file = read_data("data/pit_stops.csv")
    results_file = read_data("data/results.csv")
    clean_result = delete_data(results_file, "position", "\\N")
    num_result = turn_column_num(clean_result, "position")
    total_pitstop = get_total_pitstop(pitstops_file)
    result_pitstop = join_table(total_pitstop, num_result, ["raceId", "driverId"])
    result_stop = result_pitstop[["stop", "position"]]
    result_stop.boxplot(by="stop")
    plt.show()
    one_stop = result_pitstop.loc[result_stop["stop"] == 1]
    one_stop["position"].value_counts().plot(x="asdd", y="qwe")
    two_stop = result_pitstop.loc[result_stop["stop"] == 2]
    two_stop["position"].value_counts().plot(x="asdd", y="qwe")
    three_stop = result_pitstop.loc[result_stop["stop"] == 3]
    three_stop["position"].value_counts().plot(x="asdd", y="qwe")
    plt.show()