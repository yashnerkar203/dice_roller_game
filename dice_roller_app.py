import random


def roll_dice(num_dice):
    dice_values = []
    for _ in range(num_dice):
        dice_values.append(random.randint(1, 6))
    return dice_values


def print_dice(dice_values):
    dice_visuals = [
        [
            "+-------+",
            "|       |",
            "|   {}   |",
            "|       |",
            "+-------+"
        ],
        [
            "+-------+",
            "|       |",
            "|   {}   |",
            "|       |",
            "+-------+"
        ],
        [
            "+-------+",
            "|       |",
            "|   {}   |",
            "|       |",
            "+-------+"
        ],
        [
            "+-------+",
            "|       |",
            "|   {}   |",
            "|       |",
            "+-------+"
        ],
        [
            "+-------+",
            "|       |",
            "|   {}   |",
            "|       |",
            "+-------+"
        ],
        [
            "+-------+",
            "|       |",
            "|   {}   |",
            "|       |",
            "+-------+"
        ]
    ]
    for i in range(len(dice_values)):
        dice_visual = dice_visuals[dice_values[i] - 1]
        dice_visual[2] = dice_visual[2].format(dice_values[i])
        for line in dice_visual:
            print(line, end=' ')
        print()


def main():
    print("Welcome to the Dice Rolling App!")

    while True:
        num_dice = int(input("How many dice do you want to roll? "))

        dice_values = roll_dice(num_dice)

        print("\nRolling the dice...")
        print_dice(dice_values)

        print("Total:", sum(dice_values))

        play_again = input("Do you want to roll the dice again? (y/n): ")
        if play_again.lower() != 'y':
            break


if __name__ == '__main__':
    main()
