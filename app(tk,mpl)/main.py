import matplotlib.pyplot as plt

sunny_days = [8,10,7,14,20,18,25,19,18,14,12,7]
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
avg_sunny_days = sum(sunny_days) / len(sunny_days)

def graph(type):
    if type == 'line':
        plt.plot(months, sunny_days, marker='o', color='r', label='Sunny Days')
        plt.title('Sunny Days per Month')
        plt.xlabel('Month')
        plt.ylabel('Sunny Days')
        
        plt.axhline(y=avg_sunny_days, linestyle='--', color='green', label='Average Sunny Days')
        plt.legend()
        plt.show()
    elif type == 'bar':
        plt.bar(months, sunny_days, color='orange')
        plt.title('Sunny Days per Month - Bar Chart')
        plt.xlabel('Month')
        plt.ylabel('Sunny Days')
        plt.show()


graph('line')
graph('bar')