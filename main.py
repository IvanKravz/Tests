
def geo_log(lists):
    for visit in lists:
        place = list(visit.values())
        for city, country in place:
            if country == "Россия":
                yield visit

def ids(lists):
    dict = {}
    for key, values in lists.items():
        for id in values:
            dict.setdefault(id, None)
    dict_list = list(dict.keys())
    return dict_list

def stats_public(lists):
    max_view = max(lists.values())
    for channel, views in lists.items():
        if views == max_view:
            return channel





