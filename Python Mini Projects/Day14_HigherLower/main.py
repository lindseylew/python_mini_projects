import random
from game_data import data
import art

print(art.logo)

current_score = 0

def get_random_choices(data_list):
    """Select two random choices from the data list"""
    random_choice_a = random.choice(data_list)
    data_list.remove(random_choice_a)
    random_choice_b = random.choice(data_list)
    data_list.remove(random_choice_b)
    return [random_choice_a, random_choice_b]

def print_choices(choices):
    """Print the choices for the user"""
    print(f"Compare A: {choices[0]['name']}, {choices[0]['description']}, {choices[0]['country']}")
    print(art.vs)
    print(f"Compare B: {choices[1]['name']}, {choices[1]['description']}, {choices[1]['country']}")

def determine_winner(choices):
    """Determine which choice has the highest number of followers"""
    if choices[0]['follower_count'] > choices[1]['follower_count']:
        return 'a', choices[0]['follower_count']
    else:
        return 'b', choices[1]['follower_count']

def game_loop():
    global current_score
    data_list_copy = data.copy()
    used_choices = []

    while True:
        if len(data_list_copy) < 2:
            print("Not enough data to continue the game.")
            break

        random_choices = get_random_choices(data_list_copy)
        print_choices(random_choices)

        winner, highest_followers = determine_winner(random_choices)

        user_pick = input("Who has more followers? Type 'A' or 'B': " ).lower()

        if user_pick == winner:
            current_score += 1
            print(f"You're right! Current score: {current_score}")

            data_list_copy.extend(used_choices)
            used_choices = []

            random_choices[0], random_choices[1] = random_choices[1], get_random_choices(data_list_copy)[0]
            used_choices.extend(random_choices[:1])
        else:
            print(f"Sorry, that's wrong. Final score: {current_score}")
            break
game_loop()
# if user wins round go to next round print feedback and current score
#if user is correct random choice a disappears, random_choice b moves to a

# if user loses end game and print feedback and Final Score