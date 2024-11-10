points = []
point_sum = 0
for i in range(int(input("How many task done?\n"))):
    new_point = int(input(f"task {i + 1} points?\n"))
    points.append(new_point)
    point_sum += new_point
    
print("Tehtäviä tehty")
for i in range(len(points)):
    print(f"{i + 1}. {points[i]}p")

print(f"Yhteensä {point_sum}p")