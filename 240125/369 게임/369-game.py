def play_369_game(n):
    results = []
    for number in range(1, n+1):
        if number % 3 == 0 or '3' in str(number) or '6' in str(number) or '9' in str(number):
            results.append('0')
        else:
            results.append(str(number))
    return ' '.join(results)

n = int(input())
game_results = play_369_game(n)
print(game_results,end=" ")