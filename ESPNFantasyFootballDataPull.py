import pandas as pd
from datetime import datetime
from espn_api.football import League

desired_width = 320
pd.set_option('display.width', desired_width)

league = League(league_id=1693265373, year=2024, espn_s2='AEAQ9iOaADgJkgRdupnCAcJk0s4dAvb8NFZ%2BXOSVuJW%2Fd%2FVNZutYZziysRdGuz9hfVhrgGkSlCHwQAO2OfxG8qJ8LD2vzV3zlw9RaQotHz0yDE5f37BvTDdIaF9QdYQtoDQXkdUa%2FedbHQZ%2Fz%2BcttywwvFE8kSyds5SttNpj7YDq82Fq20Kp07R%2FvONVm%2FxqN5VZX9ZU%2Fads6zz24HsiHi8v636yRqtcDR4dsXFU68dUMLdzmJkAx9JTQtGdVdM%2BUjcbqDkCdPqj4100pejmzuryqHlZN4bYYLW2z9m92IPSEg%3D%3D', swid='{3A8578A9-74DD-4DB4-8295-39E210A5042E}')

weekly_perf = pd.DataFrame(columns=['week',
                                    'HomeVsAway',
                                    'team',
                                    'owner',
                                    'tot_score',
                                    'proj_tot_score',
                                    'week_opponent',
                                    'opp_tot_score',
                                    'player',
                                    'player_team',
                                    'main_position',
                                    'weekly_position',
                                    'proj_player_pts',
                                    'player_pts',
                                    'bye_week',
                                    'active',
                                    'player_opponent',
                                    'player_opp_rank',
                                    'injury_status'
                                    ])

week = 1
away_week= 1


while week <= league.current_week:
    boxs_v = league.box_scores(week)
    t = 0
    while t < len(boxs_v):
        i = 0
        while i < len(boxs_v[t].home_lineup):
            add_dict = {'week': week,
                        'HomeVsAway': 'Home',
                        'team': boxs_v[t].home_team.team_name,
                        'owner': boxs_v[t].home_team.owners[0]['displayName'],
                        'tot_score' : boxs_v[t].home_score,
                        'proj_tot_score': boxs_v[t].home_projected,
                        'opp_tot_score': boxs_v[t].away_score,
                        'week_opponent': boxs_v[t].away_team,
                        'player' : boxs_v[t].home_lineup[i].name,
                        'player_team': boxs_v[t].home_lineup[i].proTeam,
                        'main_position': boxs_v[t].home_lineup[i].position,
                        'weekly_position' : boxs_v[t].home_lineup[i].slot_position,
                        'proj_player_pts': boxs_v[t].home_lineup[i].projected_points,
                        'player_pts': boxs_v[t].home_lineup[i].points,
                        'bye_week': boxs_v[t].home_lineup[i].on_bye_week,
                        'active': boxs_v[t].home_lineup[i].active_status,
                        'player_opponent': boxs_v[t].home_lineup[i].pro_opponent,
                        'player_opp_rank': boxs_v[t].home_lineup[i].pro_pos_rank,
                        'injury_status' : boxs_v[t].home_lineup[i].injuryStatus}
            weekly_perf.loc[len(weekly_perf)] = add_dict
            i=i+1
        t = t + 1
    week = week + 1


while away_week <= league.current_week:
    boxs_v = league.box_scores(away_week)
    t = 0
    print(1)
    while t < len(boxs_v):
        i = 0
        print(2)
        while i < len(boxs_v[t].away_lineup):
            add_dict = {'week': away_week,
                        'HomeVsAway': 'Away',
                        'team': boxs_v[t].away_team.team_name,
                        'owner': boxs_v[t].away_team.owners[0]['displayName'],
                        'tot_score' : boxs_v[t].away_score,
                        'proj_tot_score': boxs_v[t].away_projected,
                        'opp_tot_score': boxs_v[t].home_score,
                        'week_opponent': boxs_v[t].home_team,
                        'player' : boxs_v[t].away_lineup[i].name,
                        'player_team': boxs_v[t].away_lineup[i].proTeam,
                        'main_position': boxs_v[t].away_lineup[i].position,
                        'weekly_position' : boxs_v[t].away_lineup[i].slot_position,
                        'proj_player_pts': boxs_v[t].away_lineup[i].projected_points,
                        'player_pts': boxs_v[t].away_lineup[i].points,
                        'bye_week': boxs_v[t].away_lineup[i].on_bye_week,
                        'active': boxs_v[t].away_lineup[i].active_status,
                        'player_opponent': boxs_v[t].away_lineup[i].pro_opponent,
                        'player_opp_rank': boxs_v[t].away_lineup[i].pro_pos_rank,
                        'injury_status' : boxs_v[t].away_lineup[i].injuryStatus}
            print(3)
            weekly_perf.loc[len(weekly_perf)] = add_dict
            i=i+1
        t = t + 1
    away_week = away_week + 1





weekly_perf['Snapshot_Date'] = datetime.today()

weekly_perf.to_csv(r"C:/Users/samhi/OneDrive\Desktop/FriendsLeagueData.csv")


print('Done')
