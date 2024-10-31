import os
import matplotlib.pyplot as plt


class CO2Data:
    """
    Use this class to get all the latest (2016) data about countries.
    Never again you will have to use magic constants because of the very
    clear naming of the fields in this struct.
    """

    def __init__(self, data: list[str]):
        self.tons = int(data.pop(0).replace(',', ''))
        self.change = float(data.pop(0).strip('%'))
        self.population = int(data.pop(0).replace(',', ''))
        self.per_capita = float(data.pop(0))
        self.share = float(data.pop(0).strip('%'))

    # For debugging
    def __str__(self):
        return f"[{self.tons} t, {self.change}%, {self.population}, \
{self.per_capita}, {self.share}%]"


if not os.path.exists("co2_emissions.csv"):
    print("Please rename your CO2 Emissions file to: co2_emissions.csv")
    print("and try again")
    exit()

with open("co2_emissions.csv", mode="r") as file:
    lines = file.readlines()
    # Pop the annoying header
    lines.pop(0)
    lines.pop(0)
    # Pop the last empty line
    lines.pop()

results = {}
for line in lines:
    line = str(line).strip('\n').split(';')
    # Pop the number
    line.pop(0)
    # Get the key and remove it
    country = line.pop(0)
    # Map that blob
    results[country] = CO2Data(line)

# Time to use this shit

# 1. Countries and their emissions (bar chart)
# (a) prep work
countries = list(results.keys())
countries.append("Others")
emissions = [x.share for x in results.values()]
emissions.append(100.0 - sum(emissions))
# Print and take the piss that python subtracts floats worse
# than my HP 9825 tabletop calculator.
# How does it pick up floating point errors on numbers below 100?
# It's used in so much math and still fails to outperform the 1970s
print(emissions)

# And after this rant fix it (I gave up on performance on day 1)
emissions.pop()
emissions.append(round(100.0 - sum(emissions), 2))
print(emissions)

# (b) actual plot
plt.figure(figsize=(16, 9))
bar_plot = plt.bar(countries, emissions, color="grey")
for bar in bar_plot:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height, f'{height}%',
             ha='center', va='bottom')

plt.grid(axis='y')
plt.xticks(rotation=45, ha="right")
plt.title("CO2 emissions share by countries")
plt.ylabel("% Share of CO2 emissions")

# (c) save it
plt.savefig("co2_emission_share.png")
plt.savefig("co2_emission_share.pdf")
plt.savefig("co2_emission_share.webp")

# 2. Tons of CO2 and population
# (a) setup
countries = list(results.keys())
values_tons = [x.tons for x in results.values()]
values_population = [x.population for x in results.values()]

# (b) plotting
fig, ax1 = plt.subplots(figsize=(20, 9))

ax1.bar(countries, values_tons, color="skyblue", label="Tons of CO2")
ax1.tick_params(axis='y', labelcolor="skyblue")
ax1.set_ylabel("CO2 emissions in tons", color="black")

ax2 = ax1.twinx()
ax2.plot(countries, values_population, color="salmon", marker='o',
         label="Population")
ax2.tick_params(axis='y', labelcolor="salmon")


plt.grid(axis='y')
plt.title("CO2 emissions and population by countries")
plt.legend()
plt.tight_layout()

# (c) save it
plt.savefig("co2_emission_population.png")
plt.savefig("co2_emission_population.pdf")
plt.savefig("co2_emission_population.webp")

# Display that stuff
plt.show()
