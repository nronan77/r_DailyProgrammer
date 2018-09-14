import sys

class Schedule:
    def __init__(self):
        self.events = []

    def add_event(self, name, time):
        event = Event(name, time)
        self.events.append(event)

    def list_events(self):
        for event in self.events:
            print(f'Event: {event.name} Time: {event.time}')

    def delete_event(self, event_name):
        for event in self.events:
            if event.name == event_name:
                self.events.remove(event)

class Event:
    def __init__(self, name, time):
        self.name = name
        self.time = time

def show_help():
    help_string = 'COMMANDS:\n' \
                  '     HELP: Displays possible commands and their usage(s).\n' \
                  '\n' \
                  '     ADD: Add an event to the schedule with the specified name and time.\n' \
                  '      [EVENT_NAME]: Name of the event\n' \
                  '      [EVENT_TIME]: Time of the event\n' \
                  '         Usage: ADD -EVENT_NAME -EVENT_TIME\n' \
                  '         Example: ADD -Birthday -10\n' \
                  '\n' \
                  '     DELETE: Deletes event with the specified name.\n' \
                  '      [EVENT_NAME]: Name of the event\n' \
                  '         Usage: DELETE -EVENT_NAME\n' \
                  '         Example: DELETE -Birthday Party\n' \
                  '\n' \
                  '     EDIT: Edits details of the desired event.\n' \
                  '      [EVENT_NAME]: Name of the event\n' \
                  '      (NEW_NAME): New name for event\n' \
                  '      (NEW_TIME): New time for the event\n' \
                  '         Usages:\n' \
                  '          EDIT EVENT_NAME -NEW_NAME -NEW_TIME\n' \
                  '          EDIT EVENT_NAME -NEW_NAME\n' \
                  '          EDIT EVENT_NAME -NEW_TIME\n' \
                  '         Examples:\n' \
                  '          EDIT -Lunch Date -Brunch Date -12\n' \
                  '          EDIT -Work Conference -Aerobics\n' \
                  '          EDIT -Important Meeting -19\n' \
                  '\n' \
                  '     LIST: Lists the schedule\'s current events.' \

    print(help_string)


if __name__ == '__main__':
    schedule = Schedule()

    for arg in sys.argv:
        if arg == 'ADD':
            schedule.add_event()
        elif arg.upper() == 'HELP':
            show_help()
        elif arg.upper() == 'LIST':
            schedule.list_events()
        elif arg.upper() == 'DELETE':
            schedule.delete_event()
        else:
            pass
