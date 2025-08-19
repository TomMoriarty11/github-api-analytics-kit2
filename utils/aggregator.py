import pandas as pd

def aggregate_commits_by_week(commit_data):
    dates = [commit['commit']['author']['date'] for commit in commit_data]
    df = pd.DataFrame({'date': pd.to_datetime(dates)})
    df['week'] = df['date'].dt.to_period('W').apply(lambda r: r.start_time)
    return df.groupby('week').size().reset_index(name='commit_count')
