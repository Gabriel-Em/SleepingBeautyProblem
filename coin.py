import random

HEADS = "heads"
TAILS = "tails"
MONDAY = "monday"
TUESDAY = "tuesday"

class SleepingBeautyProblem:
    def __init__(self):
        self.monday_wake_ups = 0
        self.tuesday_wake_ups = 0
        self.total_wake_ups = 0
        self.was_heads_on_wakeup = 0
        self.was_tails_on_wakeup = 0
        self.coin_toss_result_was_heads = 0
        self.coin_toss_result_was_tails = 0

    @staticmethod
    def coin_toss():
        if random.randint(1,2) == 1:
            return HEADS
        return TAILS

    def perform_action_on_toss(self, toss_result):
        if toss_result == HEADS:
            self.coin_toss_result_was_heads += 1
            self.perform_heads_action()
        else:
            self.coin_toss_result_was_tails += 1
            self.perform_tails_action()

    def perform_heads_action(self):
        self.wake_up(MONDAY, HEADS)
        
    def perform_tails_action(self):
        self.wake_up(MONDAY, TAILS)
        self.wake_up(TUESDAY, TAILS)
        
    def wake_up(self, day, toss_result):
        self.total_wake_ups += 1
        
        if day == MONDAY:
            self.monday_wake_ups += 1
        else:
            self.tuesday_wake_ups += 1

        if toss_result == HEADS:
            self.was_heads_on_wakeup += 1
        else:
            self.was_tails_on_wakeup += 1

    def perform_experiment(self, ammount_of_times):
        for i in range(ammount_of_times):
            toss_result = self.coin_toss()
            self.perform_action_on_toss(toss_result)
        
        print(f"Total experiment attempts: {ammount_of_times}")
        print(f"Toss result was HEADS: {self.coin_toss_result_was_heads} [{self.coin_toss_result_was_heads / ammount_of_times * 100:.2f}%]")
        print(f"Toss result was TAILS: {self.coin_toss_result_was_tails} [{self.coin_toss_result_was_tails / ammount_of_times * 100:.2f}%]")
        print(f"Total wake ups: {self.total_wake_ups}")
        print(f"Woke up on MONDAY: {self.monday_wake_ups} [{self.monday_wake_ups / self.total_wake_ups * 100:.2f}%]")
        print(f"Woke up on TUESDAY: {self.tuesday_wake_ups} [{self.tuesday_wake_ups / self.total_wake_ups * 100:.2f}%]")
        print(f"Toss result was HEADS on wakeup: {self.was_heads_on_wakeup} [{self.was_heads_on_wakeup / self.total_wake_ups * 100:.2f}%]")
        print(f"Toss result was TAILS on wakeup: {self.was_tails_on_wakeup} [{self.was_tails_on_wakeup / self.total_wake_ups * 100:.2f}%]")


def main():
    problem = SleepingBeautyProblem()
    problem.perform_experiment(1000000)
    
if __name__ == "__main__":
    main()