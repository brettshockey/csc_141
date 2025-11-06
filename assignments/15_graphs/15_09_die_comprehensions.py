



# Create two six-sided dice
die1 = Die()
die2 = Die()

# Simulate rolling the dice 1000000 times
rolls = 1000000
results = [die1.roll() * die2.roll() for _ in range(rolls)]

# Count the frequency of each product
max_product = die1.num_sides * die2.num_sides
frequencies = [results.count(i) for i in range(1, max_product + 1)]

# Create a bar chart to visualize the results
x_values = list(range(1, max_product + 1))
y_values = frequencies

data = [go.Bar(x=x_values, y=y_values)]

layout = go.Layout(
    title="Simulation of Multiplying Two Six-Sided Dice",
    xaxis=dict(title="Product of Two Dice", tickmode='linear', dtick=1),
    yaxis=dict(title="Frequency"),
)

fig = go.Figure(data=data, layout=layout)

# Save the chart as an HTML file and open it in a web browser
plot(fig, filename="multiplication_simulation.html")