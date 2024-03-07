from user_input import *
from data_massage import *
from data_structure import *
from request import * 
from plot import * 



if __name__ == '__main__':
    # Games names and genre descriptions
    names , games_details = scrap_names_and_tags()
    tags_lists =  get_all_games_tags_lists(games_details)
    games_names =  get_all_games_names(names)
    for tags , name in zip(tags_lists, games_names):
        print('Game name: "{}"\nTags: {}\n'.format(name , tags))
    
    # # Most Appeared Tags
    tagsDict =  create_tags_appearance_dict(tags_lists)
    top_tags,top_tags_appearance =  get_separated_lists_toptags_appearance(tagsDict)
    plot_tags_vs_appearance(top_tags,top_tags_appearance)

    # User interaction
    tag_name = user_select_tag(tagsDict,top_tags,top_tags_appearance)
    appearance = calculate_tag_percentage(tag_name,tagsDict)
    plot_user_input_tag_with_top_tags(top_tags,top_tags_appearance,tag_name,appearance)
 

