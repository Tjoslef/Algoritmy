import numpy as np

def stat(strg):
    if not strg.strip():
        return ""
    else:
        # Split and parse the input string into a list of lists of integers
        team = np.array([list(map(int, player.split("|"))) for player in strg.split(", ")])

        # Initialize the player array to store the total minutes for each player
        player = np.zeros(team.shape[0])

        # Calculate the total minutes for each player
        for row in range(len(team)):
            hours_to_minutes = round(team[row, 0] * 60,5)
            minutes = round(team[row, 1],5)
            seconds_to_minutes = team[row, 2] / 60
            player[row] = round(hours_to_minutes + minutes + seconds_to_minutes,5)

        # Calculate Range, Median, and Mean
        Range = np.max(player) - np.min(player)
        Median = np.median(player)
        Mean = np.mean(player)

        # Calculate fractional parts to convert to seconds
        def convert_to_seconds(value):
            fractional_part = value - int(value)
            return int(round((fractional_part * 60),2))

        # Calculate seconds for Range, Median, and Mean
        seconds_range = convert_to_seconds(Range)
        seconds_mean = convert_to_seconds(Mean)
        seconds_median = convert_to_seconds(Median)

        # Format the results
        formatted_result = (f"Range: {int(Range // 60.00):02d}|{int(Range % 60.00):02d}|{seconds_range:02d} "
                            f"Average: {int(Mean // 60.00):02d}|{int(Mean % 60.00):02d}|{seconds_mean:02d} "
                            f"Median: {int(Median // 60.00):02d}|{int(Median % 60.00):02d}|{seconds_median:02d}")
    
        return formatted_result
print(stat(""))

# Test cases



