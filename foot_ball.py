import datetime as dt
cristano={
    "First_name":"Cristano ",
    "Last_name":"Ronaldo",
     "gender":"Male",
     "Team":"philpines",
     "birthyear":1980,
     "goals":[],
     
}
def addgoals(list_goals,*football_goals):
    list_goals.extend(football_goals)
    
def calculate_age(player_birth_year):
    return dt.datetime.now().year - player_birth_year

cristano_goal= cristano["goals"]
addgoals(cristano_goal,50,60,70,80)
print(cristano_goal)

print(f"Age = {calculate_age(cristano['birthyear'])}")


