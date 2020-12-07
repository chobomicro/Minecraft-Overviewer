worlds["overworld"] = "E:/copy of live server/world"
worlds["nether"] = "E:/copy of live server/world_nether"
worlds["end"] = "E:/copy of live server/world_the_end"
nether_smooth_lighting = [Base(), EdgeLines(), Nether(), SmoothLighting(strength=0.5)]
end_smooth_lighting = [Base(), EdgeLines(), SmoothLighting(strength=0.5)]

def playerIcons(poi):
    if poi['id'] == 'Player':
        poi['icon'] = "https://overviewer.org/avatar/%s" % poi['EntityId']
        return "Last known location for %s" % poi['EntityId']

renders["overworld"] = {
    "world": "overworld",
    "title": "overworld",
    "rendermode": smooth_lighting,
    "dimension": "overworld",
    "markers": [dict(name="Players", filterFunction=playerIcons)]
}

renders["cave"] = {
    "world": "overworld",
    "title": "cave",
    "rendermode": cave,
    "dimension": "overworld",
    "markers": [dict(name="Players", filterFunction=playerIcons)]
}


renders["nether"] = {
    "world": "nether",
    "title": "nether",
    "rendermode": nether_smooth_lighting,
    "dimension": "nether",
    "markers": [dict(name="Players", filterFunction=playerIcons)]
}

renders["end"] = {
    "world": "end",
    "title": "end",
    "rendermode": end_smooth_lighting,
    "dimension": "end",
    "markers": [dict(name="Players", filterFunction=playerIcons)]
}

outputdir = "E:/mcmap"