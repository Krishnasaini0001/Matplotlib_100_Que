import matplotlib.pyplot as plt

sources = ["Google", "Aratai", "YouTube", "Direct", "Other"]
traffic = [40, 20, 15, 15, 10]

plt.pie(
    traffic,
    labels=sources,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Website Traffic Sources")
plt.show()