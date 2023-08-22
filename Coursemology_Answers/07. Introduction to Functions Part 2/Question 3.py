def time_difference(start,end):
    diff=(end[0]*3600+end[1]*60+end[2])-(start[0]*3600+start[1]*60+start[2])
    return ( diff//3600 , diff%3600//60 , diff%60 )