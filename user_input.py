def user_select_tag(tagsDict,top_tags,top_tags_appearance):
    print('Choose a tag from the list to calculate the % of this tag from the game list.')
    all_tags = tagsDict.keys()
    print(all_tags)
    tag_name = input()
    while(tag_name not in all_tags):
        print("Try again!")
        tag_name = input()
    return tag_name


def calculate_tag_percentage(tag_name,tagsDict):
    appearance =  tagsDict[tag_name]
    sum = len(tagsDict)
    percentage = (appearance/sum) * 100
    print('The tag {} appeared {}% from the games list tags.'.format(tag_name,percentage))
    return appearance