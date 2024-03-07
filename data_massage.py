

''' Call these functions after getting the tags and names from "scrap_names_and_tags" function.'''

def get_all_games_tags_lists(games_details):
    i = 0
    tags_lists = []
    for game_details in games_details:
        tags = game_details.div.find_all('span')
        tags_lists.append([])
        for tag in tags:
            tags_lists[i].append(tag.string)
        i += 1  
    return tags_lists 



def get_all_games_names(names):
    games_names = []
    for game_name in names:
        games_names.append(game_name.string)
    return games_names