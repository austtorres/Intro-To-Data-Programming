from operator import itemgetter
def sort_schedule(requests):
    """This function sorts the schedule requests by end time"""
    return sorted(requests, key=itemgetter(2))




def is_available(request, curr_sched):
    """Checks if requests fit into schedule without overlapping"""
    for meeting in curr_sched:

        #if any start times overlap then the requested time is not available
        if (request[1] >= meeting[1] and request[1] < meeting[2]) or (meeting[1] >= request[1] and meeting[1] < request[2]):
            return False

        #otherwise if any of the two end times overlap, then the requested time is unavailable
        elif (request [2] <= meeting[2] and request[2] > meeting [1]) or (meeting[2] <= request[2] and meeting[2] > request[1]):

            return False

    return True




def get_perfect_schedule(sorted):
    """creates a perfect schedule from a list of meetings using greedy algorithm for interval scheduling"""

    perfect_schedule = [sorted[0]]
    I = 1
    #checks if sorted meeting time is available
    while I < len(sorted):

        if is_available(sorted[I], perfect_schedule):

            #if available, the time/meeting is added to the schedule
             perfect_schedule.append(sorted[I]) 
        I += 1
        
    return perfect_schedule


def main(request):
    """sorts schedule and generates a perfect schedule with list of meetings and times"""

    #creating perfect schedule by placing functions into variables
    final_schedule = sort_schedule(request)
    final_schedule = get_perfect_schedule(final_schedule)

    return final_schedule
