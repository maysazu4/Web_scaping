import matplotlib.pyplot as plt



def plot_tags_vs_appearance(tags,appearance):
    plt.bar(tags,appearance,color ='maroon', width = 0.6)
    plt.ylabel('appearances')
    plt.xlabel('tags')
    plt.show()


def plot_user_input_tag_with_top_tags(top_tags,top_tags_appearance,tag_name,appearance):
    top_tags.append(tag_name)
    top_tags_appearance.append(appearance)
    plot_tags_vs_appearance(top_tags,top_tags_appearance)