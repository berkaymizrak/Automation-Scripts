import time
import keyboard
import pyautogui


class Progress:
    def __init__(self):
        self.difference_now = time.time()

    def progress(self, count, total, now, message='In progress...', ):
        remaining_time = self.time_definition(
            int((total / (count / (time.time() - now))) - (time.time() - now))
        )
        passed_time = self.time_definition(int(time.time() - now))
        print(
            "\r{} |{}{}| {}% | {} | {} left."
                .format(
                message,
                "█" * int(25 * count / total),
                " " * (25 - int(25 * count / total)),
                int(100 * count / total),
                passed_time,
                remaining_time
            ),
            flush=True,
            end=""
        )

    def time_definition(self, time_input):
        try:
            time_input = int(time_input)
        except:
            pass
        if time_input >= 60 * 60 * 24:
            remaining = time_input % (60 * 60 * 24)
            day = int(time_input / (60 * 60 * 24))
            hour = int(remaining / (60 * 60))
            minute = int(int(remaining / 60) % 60)
            second = int(remaining % 60)

            if day > 99:
                final_time_string = '99+ day %s h %s min %s s' % (hour, minute, second)
            else:
                if not second:
                    if not minute:
                        if not hour:
                            final_time_string = '%s day' % (day)
                        else:
                            final_time_string = '%s day %s h' % (day, hour)
                    else:
                        final_time_string = '%s day %s h %s min' % (day, hour, minute)
                else:
                    final_time_string = '%s day %s h %s min %s s' % (day, hour, minute, second)
        elif time_input >= 60 * 60:
            remaining = time_input % (60 * 60)
            hour = int(time_input / (60 * 60))
            minute = int(remaining / 60)
            second = int(remaining % 60)
            if not second:
                if not minute:
                    final_time_string = '%s h' % (hour)
                else:
                    final_time_string = '%s h %s min' % (hour, minute)
            else:
                final_time_string = '%s h %s min %s s' % (hour, minute, second)
        elif time_input >= 60:
            minute = int(time_input / 60)
            second = int(time_input % 60)
            if not second:
                final_time_string = '%s min' % (minute)
            else:
                final_time_string = '%s min %s s' % (minute, second)
        else:
            final_time_string = '%s s' % (time_input)
        return final_time_string


def wait_function(wait_time, pressed_key='q'):
    progress = Progress()
    now = time.time()
    time.sleep(0.1)
    pause_time = int(wait_time / 0.05)
    for i in range(pause_time):
        if keyboard.is_pressed(pressed_key):
            return True
        time.sleep(0.05)
        progress.progress(i + 1, pause_time, now, message='Counting down...')
    print()
    return False


def clear_input(times):
    for i in range(times):
        pyautogui.write('\b')


def wait_in_progess(pause_time):
    print()
    print('Paused! Waiting for %s second.' % pause_time)
    progress = Progress()
    now = time.time()
    time.sleep(0.1)
    for i in range(pause_time):
        time.sleep(1)
        progress.progress(i + 1, pause_time, now, message='Counting down...')
    print()
