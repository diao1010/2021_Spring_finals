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


