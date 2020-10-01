# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def learn() -> None:
    from sklearn.ensemble import RandomForestClassifier
    clf = RandomForestClassifier(random_state=0)
    x = [[1, 2, 3], [11, 12, 13]]  # 2 samples, 3 features
    y = [0, 1]  # classes of each sample
    clf.fit(x, y)
    RandomForestClassifier(random_state=0)
    print(clf)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    learn()
    print_hi('Damiano')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
