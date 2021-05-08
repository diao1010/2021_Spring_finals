import pandas as pd
import matplotlib.pyplot as plt


def get_max_lap(df: pd.DataFrame) -> pd.DataFrame:
    """
    get the number of laps in each race
    (use positionOrder == 1 and stop == 1)
    :param df: input dataframe
    :return: processed dataframe
    >>> input_df = pd.DataFrame({"raceId":[1,1,2,2,3], "year":[2011,2011,2018,2018,2020], "laps":[25,58,59,15, 60],\
    "positionOrder":[4,1,1,4,1], "stop":[1,1,1,1,1]})
    >>> get_max_lap(input_df)
       raceId  year  laps
    0       1  2011    58
    1       2  2018    59
    2       3  2020    60
    """
    return df[(df['positionOrder'] == 1) & (df['stop'] == 1)].reset_index(drop=True)[['raceId', 'year', 'laps']]


def count_proportion(df_pit: pd.DataFrame, df_race: pd.DataFrame, decimal: int) -> pd.DataFrame:
    """
    add column with the proportion during the total laps in each race
    :param decimal:
    :param df_pit: pit dataframe
    :param df_race: race dataframe
    :return:
    >>> df = pd.DataFrame({"raceId":[1,2,3], "lap":[25, 15, 29]})
    >>> race = pd.DataFrame({"raceId":[1,2,3], "laps":[50, 60, 58]})
    >>> count_proportion(df,race, 2)
       raceId  lap  laps  proportion
    0       1   25    50        0.50
    1       2   15    60        0.25
    2       3   29    58        0.50
    """
    df_new = df_pit.merge(df_race[['raceId', 'laps']], on='raceId', how='left', suffixes=('_once', '_total'))
    df_new['proportion'] = round(df_new['lap'] / df_new['laps'], decimal)
    return df_new


def select_finished_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    drop data rows with unfinished status
    :param df: input dataframe
    :return: modified dataframe
    >>> input_df = pd.DataFrame({"raceId":[1,1,2,2], "statusId":[1,2,11,3]})
    >>> select_finished_data(input_df)
    >>> print(input_df)
       raceId  statusId
    0       1         1
    2       2        11
    """
    status_in = [1, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    return df.drop(df[~df['statusId'].isin(status_in)].index, inplace=True)


def plot_line_chart(df: pd.DataFrame, stop: int, plot_title):
    """
    This function the x and y co-ordinates to plot a line graph
    :param df: input dataframe ready for plotting
    :param stop: pit stop times
    :param plot_title: title for the line graph
    :return: plt
    """
    fig, ax = plt.subplots(figsize=(10, 5))
    if stop == 1:
        df.plot(x='proportion', y='laps', ax=ax)
    elif stop >= 2:
        # first stop
        x1 = df[df['stop'] == 1]['proportion']
        y1 = df[df['stop'] == 1]['laps']
        plt.plot(x1, y1, label='first time')
        # second stop
        x2 = df[df['stop'] == 2]['proportion']
        y2 = df[df['stop'] == 2]['laps']
        plt.plot(x2, y2, label='second time')
        if stop >= 3:
            ax.set_ylim([0, 100])
            x3 = df[df['stop'] == 3]['proportion']
            y3 = df[df['stop'] == 3]['laps']
            # plotting the line 3 points
            plt.plot(x3, y3, label='third time')
            if stop == 4:
                ax.set_ylim([0, 100])
                x4 = df[df['stop'] == 4]['proportion']
                y4 = df[df['stop'] == 4]['laps']
                # plotting the line 4 points
                plt.plot(x4, y4, label='forth time')
    ax.set(xlabel='Proportion of total laps',
           ylabel='Race Count',
           title=plot_title)
    plt.legend()
    return plt


def df_group_plot(df: pd.DataFrame) -> pd.DataFrame:
    """
    before plotting, clean the dataframe first
    :param df: dataframe
    :return: clean df
    """
    return df.groupby(by=['stop', 'proportion']).count().reset_index()


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
    pitstop_df = pd.DataFrame(columns=["raceId", "driverId", "stop"])
    for line in range(0, len(pitstop_table)):
        df_stop = pitstop_df.loc[(pitstop_df["raceId"] == int(pitstop_table.loc[line, "raceId"])) & (
                pitstop_df["driverId"] == int(pitstop_table.loc[line, "driverId"])), ["stop"]]
        if len(df_stop) > 0:
            stop_list = df_stop.values.tolist()
            if int(pitstop_table.loc[line, "stop"]) > stop_list[0][0]:
                pitstop_df.loc[(pitstop_df["raceId"] == int(pitstop_table.loc[line, "raceId"])) & (
                        pitstop_df["driverId"] == int(pitstop_table.loc[line, "driverId"])), "stop"] = int(
                    pitstop_table.loc[line, "stop"])
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
