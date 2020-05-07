Program Skills
Practice using lists
Exploring built-in Python sorting functions
(Or writing your own if you want to)
Greedy algorithms

Summary
You have been hired at a high-profile Wall Street ‘Company X’ where time is money. You are eager to make a mark and on the first day of your job you are presented with a problem. Your Boss’ PA (personal assistant) is not able to keep up with the unending stream of meeting requests from various stakeholders. The meeting requests come via email and everyone expects to be either included in the schedule for the day or be given a courtesy reply asking for a reschedule to next day. It so happens that the Boss is not very particular who gets into the schedule if following conditions are met:

Maximum number of meeting requests are met, i.e., given a list of meeting schedules, the PA must be able to accommodate maximum number of people.
No two meetings must overlap. However, start time of one meeting may be same as end of another.
The PA has asked for your help as manually sorting through the stream of schedule requests is proving too much. You should make a Python program that takes in a list containing a number of meeting requests and creates the perfect schedule meeting the Boss’s requirements. You will employ what is known in Computer Science as a Greedy Algorithm for Interval Scheduling (Links to an external site.) to solve this problem. The Algorithm is summarized below:

Step 1. Cut a hole in a box. Sort all the meeting requests by their end times, with the meetings ending early coming first.

Step 2. Start from an empty main schedule and add the first meeting request in the list of sorted list. Then from the sorted list start adding meeting requests to the main schedule by checking whether the start time of the current schedule is greater than the finish time of the previous schedule added and discarding it if that is not the case.

Step 3. Return the main schedule created in Step 2. This will be the Perfect Schedule accommodating maximum number of people. Note that there may be more than one solution to the same problem, we are just interested in getting one of them.

Program Requirements
To implement the Greedy Algorithm for Interval Scheduling, you will write at least four (4) functions with the following names and behaviors (Please ensure that the names match EXACTLY as is):

sort_schedule(requests) – takes in a list of meeting requests (see below for details), sorts them by their ending times, and returns the sorted list.
is_available(request, curr_sched) – takes in an individual meeting request and the current schedule list, and returns True if and only if that meeting request will fit in the schedule, False otherwise.
get_perfect_schedule(sorted) – takes in a sorted list of meeting requests and returns a list of accepted meeting requests, compiled using the Greedy Algorithm for Interval Scheduling.
main(requests) – takes in a list of meeting requests and returns the perfect schedule created by calling other functions in the program.
Be careful to match these names and behaviors exactly. You may implement additional helper functions if you like, but you must have the specified functions.

1. Sort schedule
Meeting requests are themselves short lists, and look like this:

['Meeting Name', start_time, end_time]
where start_time and end_time are floats representing hours on a 24-hour clock. That is, 15.0 means 3pm, and 8.5 means 8:30am. This function's parameter will contain a list of these lists (whoa, listception).

Implementing sorting algorithms can be good coding practice, but that's not the point of this assignment – Python provides a very simple implementation to sort lists of lists by a specific index of the meeting request, using the itemgetter function from the operator module.

>>> from operator import itemgetter
>>> sorted([[1, 2], [2, 10], [3, 1]], key=itemgetter(1))
=> [[3, 1], [1, 2], [2, 10]]
Here's some sample output, but you should be able to test this function yourself pretty easily.

>>> sort_schedule([['Meeting1', 8, 10], ['Meeting2', 8, 8.5], ['Meeting3', 15, 16], ['Meeting4', 13, 14], ['Meeting5', 12, 13], ['Meeting6', 9, 12], ['Meeting7', 8, 9]])
=> [['Meeting2', 8, 8.5], ['Meeting7', 8, 9], ['Meeting1', 8, 10], ['Meeting6', 9, 12], ['Meeting5', 12, 13], ['Meeting4', 13, 14], ['Meeting3', 15, 16]]
2. Is available?
This function is a helper function! It will take in a meeting request and the current schedule as lists and return True if the meeting fits in the schedule; False if it doesn't.

>>> request = ['MeetingX', 11.5, 12]
>>> is_available(request, [['Meeting1', 8, 9], ['Meeting7', 9, 11], ['Meeting2', 12, 13], ['Meeting6', 13, 14], ['Meeting3', 15, 16]])
=> True
>>> request = ['MeetingX', 11.5, 13]
>>> is_available(request, [['Meeting1', 8, 9], ['Meeting7', 9, 11], ['Meeting2', 12, 13], ['Meeting6', 13, 14], ['Meeting3', 15, 16]])
=> False
3. Get perfect schedule
This function should follow the algorithm stated in the Summary section above to create a perfect schedule from a list of meetings that you may assume to be already sorted.

>>> get_perfect_schedule([['Meeting2', 8, 8.5], ['Meeting7', 8, 9], ['Meeting1', 8, 10], ['Meeting6', 9, 12], ['Meeting5', 12, 13], ['Meeting4', 13, 14], ['Meeting3', 15, 16]])
==> [['Meeting2', 8, 8.5], ['Meeting6', 9, 12], ['Meeting5', 12, 13], ['Meeting4', 13, 14], ['Meeting3', 15, 16]]
4. Main function
This is the main entry point for your program. This function makes calls to all other functions in your program (except is_available(), which you can use in your perfect schedule maker or independently).

The input to this function is a list of schedule requests of the following form:

[ [‘request_name’, start_time, end_time], ...]
For example,

[ ['Meeting with Deb', 8, 10], ['Talk with Tracy, 8.5, 12], ['Teleconference with Jim', 9, 13], ['Discussion with Gary', 15, 16], ['Coffee with Alexi’, 17, 18] ]
The start_times and end times will follow 24hr clock format, so 15 means 3 PM. Also, they can only be increments of half hour, i.e., 8.5 means 8:30 AM. No other time divisions will be present.

First, the function calls the sort_schedule() function to get a list of meeting requests. Then this sorted list is passed to the get_perfect_schedule() function. This function then returns the Perfect Schedule.

>>> main([['Meeting1', 8, 10], ['Meeting2', 8, 8.5], ['Meeting3', 15, 16], ['Meeting4', 13, 14], ['Meeting5', 12, 13], ['Meeting6', 9, 12], ['Meeting7', 8, 9]])
==> [['Meeting2', 8, 8.5], ['Meeting6', 9, 12], ['Meeting5', 12, 13], ['Meeting4', 13, 14], ['Meeting3', 15, 16]]
