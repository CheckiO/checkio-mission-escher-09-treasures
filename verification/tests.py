"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": [{'golden coin': {'price': 100, 'weight': 50, 'amount': 200}, 'silver coin': {'price': 10, 'weight': 20, 'amount': 1000}, 'ruby': {'price': 1000, 'weight': 200, 'amount': 2}}, 5],
            "answer": ['golden coin: 92', 'ruby: 2']
        },
        {
            "input": [{'golden coin': {'price': 100, 'weight': 50, 'amount': 100}, 'silver coin': {'price': 10, 'weight': 20, 'amount': 100}, 'ruby': {'price': 1000, 'weight': 200, 'amount': 1}}, 7.5],
            "answer": ['golden coin: 100', 'silver coin: 100', 'ruby: 1']
        }
    ],
    "Extra": [
        {
            "input": [{'golden coin': {'price': 100, 'weight': 50, 'amount': 100}, 'silver coin': {'price': 10, 'weight': 20, 'amount': 100}, 'ruby': {'price': 1000, 'weight': 200, 'amount': 3}}, 0.6],
            "answer": ['ruby: 3']
        },
        {
            "input": [{'golden coin': {'price': 100, 'weight': 10, 'amount': 100}, 'silver coin': {'price': 10, 'weight': 10, 'amount': 100}, 'ruby': {'price': 1000, 'weight': 200, 'amount': 5}}, 1.8],
            "answer": ['golden coin: 100', 'ruby: 4']
        },
        {
            "input": [{'golden coin': {'price': 50, 'weight': 50, 'amount': 1000}, 'silver coin': {'price': 10, 'weight': 20, 'amount': 100}, 'ruby': {'price': 1000, 'weight': 200, 'amount': 1}}, 1],
            "answer": ['golden coin: 16', 'ruby: 1']
        },
        {
            "input": [{'golden coin': {'price': 100, 'weight': 50, 'amount': 1}, 'silver coin': {'price': 10, 'weight': 20, 'amount': 1}, 'ruby': {'price': 1000, 'weight': 200, 'amount': 1}}, 9.95],
            "answer": ['golden coin: 1', 'silver coin: 1', 'ruby: 1']
        },
        {
            "input": [{'golden coin': {'price': 100, 'weight': 10, 'amount': 100}, 'silver coin': {'price': 30, 'weight': 15, 'amount': 500}, 'ruby': {'price': 1000, 'weight': 150, 'amount': 2}}, 9.9],
            "answer": ['golden coin: 100', 'silver coin: 500', 'ruby: 2']
        },
        {
            "input": [{'golden coin': {'price': 250, 'weight': 10, 'amount': 300}, 'silver coin': {'price': 30, 'weight': 5, 'amount': 500}, 'ruby': {'price': 2000, 'weight': 150, 'amount': 10}}, 3.6],
            "answer": ['golden coin: 300', 'ruby: 4']
        },
        {
            "input": [{'golden coin': {'price': 250, 'weight': 10, 'amount': 30}, 'silver coin': {'price': 30, 'weight': 5, 'amount': 200}, 'ruby': {'price': 10000, 'weight': 250, 'amount': 7}}, 2.75],
            "answer": ['golden coin: 30', 'silver coin: 140', 'ruby: 7']
        },
        {
            "input": [{'golden coin': {'price': 125, 'weight': 25, 'amount': 30}, 'silver coin': {'price': 30, 'weight': 10, 'amount': 50}, 'ruby': {'price': 5000, 'weight': 150, 'amount': 7}}, 1.15],
            "answer": ['golden coin: 4', 'ruby: 7']
        }

    ]
}
