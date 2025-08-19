def profile_repo_data(repo_data):
    return {
        "total_commits": len(repo_data),
        "first_commit": repo_data[0]['commit']['author']['date'],
        "last_commit": repo_data[-1]['commit']['author']['date'],
        "authors": list(set([c['commit']['author']['name'] for c in repo_data]))
    }
