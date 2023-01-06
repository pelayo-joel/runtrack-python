def DistanceForWC(steps, height):
    totalDistance = (((height * steps) * 2) * 7) / 100
    return print(f"Assuming the guard goes to the WC once per day, he'll travel {totalDistance}m a week")

nSteps = int(input("Number of steps : "))
stepsHeight = int(input("Height of steps in cm : "))
DistanceForWC(nSteps, stepsHeight)
