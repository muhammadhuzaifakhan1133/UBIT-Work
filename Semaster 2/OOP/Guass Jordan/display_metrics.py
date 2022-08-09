def displayMetrics(metrics):
    NR = len(metrics)
    NC = len(metrics[0])
    for row in range(NR):
        for col in range(NC):
            print(f"{metrics[row][col]:8.2f}", end="\t")
        print()