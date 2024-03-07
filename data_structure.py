
def create_tags_appearance_dict(tags_list):
    tagsDict = {}
    for tagsList in tags_list:
        for tag in tagsList:
            if tag[0] == ',':
                processed_tag = tag[2:]
            else:
                processed_tag = tag

            if processed_tag in tagsDict:
                new_value = tagsDict[processed_tag] + 1
                tagsDict.update({processed_tag: new_value})
        else:
            tagsDict.update({processed_tag : 1})
    return tagsDict


def get_separated_lists_toptags_appearance(tagsDict):
    all_tags = []
    top_tags = []
    top_tags_appearance = []
    sum = 0
    for tag,appearance in tagsDict.items():
        sum += 1
        all_tags.append(tag)
        if appearance == 1:
            continue
        top_tags.append(tag)
        top_tags_appearance.append(appearance)
    return top_tags,top_tags_appearance